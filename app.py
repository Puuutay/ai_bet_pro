import streamlit as st
import plotly.graph_objects as go
from nba_api.stats.static import teams
from nba_api.stats.endpoints import LeagueDashTeamStats

st.set_page_config(page_title="AI Bet Pro", layout="wide")

# ================= PWA =================
st.markdown("""
<link rel="manifest" href="/static/manifest.json">
<meta name="theme-color" content="#020617">
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/static/sw.js');
}
</script>
""", unsafe_allow_html=True)

# ================= UI =================
st.markdown("""
<style>
.block-container {padding:0.6rem;}
body {background: linear-gradient(135deg,#020617,#0f172a); color:white;}
header, footer {visibility:hidden;}

.card {
    background: rgba(255,255,255,0.05);
    padding:14px;
    border-radius:14px;
    margin-bottom:10px;
}

.stButton > button {
    width:100%;
    height:50px;
    border-radius:12px;
    background:linear-gradient(90deg,#22c55e,#16a34a);
    color:white;
    font-size:16px;
    font-weight:bold;
}

.bottom-bar {
    position:fixed;
    bottom:0;
    left:0;
    right:0;
    background:#020617;
    padding:10px;
    border-top:1px solid rgba(255,255,255,0.1);
}

.spacer {height:80px;}

.green {color:#22c55e;}
.red {color:#ef4444;}
</style>
""", unsafe_allow_html=True)

# ================= DATA =================
@st.cache_data(ttl=3600)
def get_teams():
    return teams.get_teams()

@st.cache_data(ttl=3600)
def get_all_ppg():
    try:
        df = LeagueDashTeamStats(
            per_mode_detailed="PerGame",
            timeout=5
        ).get_data_frames()[0]

        return dict(zip(df["TEAM_ID"], df["PTS"]))
    except:
        return {}

def get_ppg(team_id):
    data = get_all_ppg()

    if team_id in data:
        return float(data[team_id])

    # fallback values (safe)
    fallback = {
        1610612738: 117,
        1610612737: 115,
        1610612747: 113,
        1610612744: 116,
        1610612756: 114,
    }

    return fallback.get(team_id, 112)

def predict(h, a):
    h += 2
    prob = (h/(h+a))*100
    return round(prob,1), h, a

def calc_ev(prob, odds):
    return (prob/100 * odds) - 1

# ================= HEADER =================
st.markdown('<div class="card"><b>🏀 AI BET PRO</b></div>', unsafe_allow_html=True)

# ================= NAV =================
page = st.selectbox("Menu", ["Dashboard","Prediction","Autopilot","Portfolio"])

team_list = get_teams()
names = [t["full_name"] for t in team_list]

# ================= DASHBOARD =================
if page == "Dashboard":
    c1,c2,c3 = st.columns(3)
    c1.metric("Win Rate","62%")
    c2.metric("ROI","+15%")
    c3.metric("Bets","120")

    fig = go.Figure()
    fig.add_trace(go.Scatter(y=[1,3,2,5,4],mode="lines+markers"))
    fig.update_layout(template="plotly_dark")

    st.plotly_chart(fig,use_container_width=True)

# ================= PREDICTION =================
elif page == "Prediction":
    home = st.selectbox("Home Team", names)
    away = st.selectbox("Away Team", names)

    if st.button("🚀 RUN AI"):
        h_id = [t for t in team_list if t["full_name"]==home][0]["id"]
        a_id = [t for t in team_list if t["full_name"]==away][0]["id"]

        h_ppg = get_ppg(h_id)
        a_ppg = get_ppg(a_id)

        prob,h,a = predict(h_ppg,a_ppg)
        odds = 1.9
        ev = calc_ev(prob,odds)

        st.session_state.result = {
            "match": f"{home} vs {away}",
            "prob": prob,
            "winner": home if h>a else away,
            "odds": odds,
            "ev": ev
        }

    if "result" in st.session_state:
        r = st.session_state.result
        st.markdown(f"""
        <div class="card">
        <b>{r['match']}</b><br>
        Winner: <span class="green">{r['winner']}</span><br>
        Confidence: {r['prob']}%<br>
        EV: {round(r['ev'],3)}
        </div>
        """, unsafe_allow_html=True)

    stake = st.number_input("Stake", value=100)

    st.markdown(f"""
    <div class="bottom-bar">
    💰 ₱{stake} → ₱{round(stake * 1.9,2)}
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# ================= AUTOPILOT =================
elif page == "Autopilot":
    st.markdown("### 🤖 Autopilot")

    if "result" in st.session_state:
        r = st.session_state.result

        if r["prob"] > 65 and r["ev"] > 0:
            st.success("✅ GOOD BET")
        else:
            st.warning("❌ SKIP")

# ================= PORTFOLIO =================
elif page == "Portfolio":
    bankroll = st.number_input("Bankroll", value=5000)

    if "result" in st.session_state:
        r = st.session_state.result
        stake = bankroll * 0.02

        st.markdown(f"""
        <div class="card">
        {r['match']}<br>
        Stake: ₱{round(stake,2)}
        </div>
        """, unsafe_allow_html=True)
