import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import requests
from bs4 import BeautifulSoup

from nba_api.stats.static import teams
from nba_api.stats.endpoints import LeagueDashTeamStats, ScoreboardV2

# ================= CONFIG =================
st.set_page_config(page_title="AI Bet Pro", layout="wide")

# ================= PWA =================
st.markdown("""
<link rel="manifest" href="/static/manifest.json">
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/static/sw.js');
}
</script>
""", unsafe_allow_html=True)

# ================= STYLE =================
st.markdown("""
<style>
body {background: linear-gradient(135deg,#020617,#0f172a); color:white;}
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
}
.green {color:#22c55e;}
</style>
""", unsafe_allow_html=True)

# ================= DATA =================
@st.cache_data(ttl=3600)
def get_teams():
    return teams.get_teams()

@st.cache_data(ttl=1800)
def get_team_stats(season):
    try:
        df = LeagueDashTeamStats(
            season=season,
            per_mode_detailed="PerGame",
            timeout=10
        ).get_data_frames()[0]

        return dict(zip(df["TEAM_ID"], df["PTS"]))
    except:
        return {}

def get_ppg(team_id):
    stats = get_team_stats("2025-26")
    return stats.get(team_id, 112)

# ================= LIVE GAMES =================
@st.cache_data(ttl=120)
def get_live_games():
    try:
        today = pd.Timestamp.today().strftime("%Y-%m-%d")
        sb = ScoreboardV2(game_date=today, day_offset=0)
        df = sb.get_data_frames()[0]

        games = []
        for _, row in df.iterrows():
            home = str(row.get("HOME_TEAM_NAME",""))
            away = str(row.get("VISITOR_TEAM_NAME",""))
            if home and away:
                games.append((home, away))

        if games:
            return games
    except:
        pass

    return [
        ("Boston Celtics","Miami Heat"),
        ("Lakers","Warriors")
    ]

# ================= INJURY =================
@st.cache_data(ttl=600)
def get_injuries():
    try:
        url = "https://www.cbssports.com/nba/injuries/"
        res = requests.get(url, timeout=8)
        soup = BeautifulSoup(res.text,"html.parser")

        names = []
        for x in soup.select("tr"):
            txt = x.get_text()
            if "Out" in txt or "Questionable" in txt:
                names.append(txt[:40])

        return names[:10]
    except:
        return ["No major injuries"]

# ================= AI =================
def predict(home_ppg, away_ppg):
    h = home_ppg + 2
    a = away_ppg
    prob = (h/(h+a))*100
    return round(prob,1), round(h), round(a)

def explanation(home, away, h_ppg, a_ppg):
    r = []
    if h_ppg > a_ppg:
        r.append(f"{home} mas mataas scoring")
    else:
        r.append(f"{away} mas mataas scoring")
    r.append("May home advantage")
    return r

def star_player(ppg):
    pts = round(ppg * 0.28,1)
    mins = round(pts * 1.2)
    return pts, mins

# ================= UI =================
st.title("🏀 AI BET PRO")

page = st.selectbox("Menu",["Dashboard","Prediction","Live"])

team_list = get_teams()
names = [t["full_name"] for t in team_list]

# ================= DASHBOARD =================
if page == "Dashboard":
    st.markdown("### 📊 Overview")

    fig = go.Figure()
    fig.add_trace(go.Scatter(y=[1,2,3,2,5]))
    st.plotly_chart(fig,use_container_width=True)

# ================= PREDICTION =================
elif page == "Prediction":

    home = st.selectbox("Home",names)
    away = st.selectbox("Away",names)

    if st.button("RUN AI"):

        h_id = [t for t in team_list if t["full_name"]==home][0]["id"]
        a_id = [t for t in team_list if t["full_name"]==away][0]["id"]

        h_ppg = get_ppg(h_id)
        a_ppg = get_ppg(a_id)

        prob, hs, as_ = predict(h_ppg,a_ppg)

        reasons = explanation(home,away,h_ppg,a_ppg)

        pts,mins = star_player(max(h_ppg,a_ppg))

        st.markdown(f"""
        <div class="card">
        <h3>{home} vs {away}</h3>

        🏆 Winner: <span class="green">{home if hs>as_ else away}</span><br>
        📊 Confidence: {prob}%<br>
        🧮 Score: {hs} - {as_}

        <br>
        🔍 {"<br>".join(reasons)}

        <br><br>
        ⭐ Star Player:
        {pts} pts | {mins} mins
        </div>
        """,unsafe_allow_html=True)

# ================= LIVE =================
elif page == "Live":

    games = get_live_games()

    for g in games:
        st.markdown(f"""
        <div class="card">
        {g[0]} vs {g[1]}
        </div>
        """,unsafe_allow_html=True)

# ================= INJURY =================
st.sidebar.markdown("### 🏥 Injuries")
for i in get_injuries():
    st.sidebar.write("❌",i)
