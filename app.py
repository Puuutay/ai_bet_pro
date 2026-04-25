import streamlit as st
import plotly.graph_objects as go
from nba_api.stats.static import teams
from nba_api.stats.endpoints import LeagueDashTeamStats

st.set_page_config(page_title="AI Bet Pro", layout="wide")

# --- PWA links (safe kahit di gumana ang install prompt) ---
st.markdown("""
<link rel="manifest" href="/static/manifest.json">
<meta name="theme-color" content="#020617">
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/static/sw.js');
}
</script>
""", unsafe_allow_html=True)

# --- Simple UI ---
st.markdown("""
<style>
.block-container {padding:0.6rem;}
body {background: linear-gradient(135deg,#020617,#0f172a); color:white;}
header, footer {visibility:hidden;}
.card {background: rgba(255,255,255,0.06); padding:14px; border-radius:14px; margin-bottom:10px;}
.stButton>button {width:100%; height:48px; border-radius:12px; background:#22c55e; color:white; font-weight:bold;}
.bottom {position:fixed; bottom:0; left:0; right:0; background:#020617; padding:10px; border-top:1px solid rgba(255,255,255,.1);}
.spacer {height:80px;}
.green{color:#22c55e;}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def get_teams():
    return teams.get_teams()

@st.cache_data
def get_ppg(team_id):
    df = LeagueDashTeamStats(per_mode_detailed="PerGame").get_data_frames()[0]
    return float(df[df["TEAM_ID"]==team_id]["PTS"].values[0])

def predict(h,a):
    h+=2
    prob=(h/(h+a))*100
    return round(prob,1), h, a

def ev(prob,odds):
    return (prob/100*odds)-1

st.markdown('<div class="card"><b>🏀 AI BET PRO</b></div>', unsafe_allow_html=True)

page = st.selectbox("Menu",["Dashboard","Prediction","Autopilot","Portfolio"])

team_list = get_teams()
names = [t["full_name"] for t in team_list]

if page=="Dashboard":
    c1,c2,c3=st.columns(3)
    c1.metric("Win Rate","62%")
    c2.metric("ROI","+15%")
    c3.metric("Bets","120")

    fig=go.Figure()
    fig.add_trace(go.Scatter(y=[1,3,2,5,4],mode="lines+markers"))
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig,use_container_width=True)

elif page=="Prediction":
    home=st.selectbox("Home",names)
    away=st.selectbox("Away",names)

    if st.button("RUN AI"):
        h_id=[t for t in team_list if t["full_name"]==home][0]["id"]
        a_id=[t for t in team_list if t["full_name"]==away][0]["id"]

        h_ppg=get_ppg(h_id)
        a_ppg=get_ppg(a_id)

        prob,h,a=predict(h_ppg,a_ppg)
        odds=1.9
        e=ev(prob,odds)

        st.session_state.r={
            "match":f"{home} vs {away}",
            "prob":prob,
            "winner":home if h>a else away,
            "odds":odds,
            "ev":e
        }

    if "r" in st.session_state:
        r=st.session_state.r
        st.markdown(f"""
        <div class="card">
        <b>{r['match']}</b><br>
        Winner: <span class="green">{r['winner']}</span><br>
        Confidence: {r['prob']}%<br>
        EV: {round(r['ev'],3)}
        </div>
        """, unsafe_allow_html=True)

    stake=st.number_input("Stake",100)
    st.markdown(f'<div class="bottom">₱{stake} → ₱{round(stake*1.9,2)}</div>', unsafe_allow_html=True)
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

elif page=="Autopilot":
    st.markdown("### 🤖 Autopilot")
    if "r" in st.session_state:
        r=st.session_state.r
        st.success("GOOD BET" if r["prob"]>65 and r["ev"]>0 else "SKIP")

elif page=="Portfolio":
    bankroll=st.number_input("Bankroll",5000)
    if "r" in st.session_state:
        r=st.session_state.r
        stake=bankroll*0.02
        st.markdown(f'<div class="card">{r["match"]}<br>Stake: ₱{round(stake,2)}</div>', unsafe_allow_html=True)
