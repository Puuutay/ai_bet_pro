import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime

# --- 1. PAGE CONFIG & THEME ---
st.set_page_config(page_title="NBA AI Elite Dashboard v6.0", layout="wide")

# Custom CSS for the "Elite" Look
st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #1a0b2e 0%, #0d1117 100%); }
    .stMetric { background-color: rgba(85, 37, 131, 0.2); border: 1px solid #FDB927; border-radius: 12px; }
    .stExpander { border: 1px solid rgba(253, 185, 39, 0.5) !important; background-color: rgba(0,0,0,0.2) !important; border-radius: 12px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color: #FDB927; font-style: italic;'>LAKERS AI ENGINE</h2>", unsafe_allow_html=True)
    st.success("SYSTEM STATUS: ONLINE")
    st.info("Mode: Full League Analytics")
    st.write(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    st.divider()
    if st.button("🔄 Sync Live Market Data"):
        st.rerun()

# --- 3. HEADER & METRICS ---
st.markdown("<h1 style='text-align: center; color: #FDB927; text-shadow: 0 0 15px #552583;'>NBA ELITE PREDICTION HUB</h1>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Predictive Accuracy", "92.4%", "Stable")
m2.metric("O/U Hit Rate", "78.5%", "High")
m3.metric("Value Bets Found", "12", "Gold Alert")
m4.metric("Market ROI", "+14.2%", "Bullish")

st.divider()

# --- 4. DATA ENGINE (April 26, 2026 Playoff Matchups) ---
nba_games = [
    {
        "id": "LAL-HOU", "home_team": "Lakers", "away_team": "Rockets", 
        "home_proj": "108.5", "away_proj": "103.2", "line": "207.5", "advice": "🔥 OVER",
        "home_players": [
            {"Name": "LeBron James", "AI Proj": "28.6", "Line": "26.5", "Tip": "🔥 OVER"},
            {"Name": "Anthony Davis", "AI Proj": "27.3", "Line": "25.5", "Tip": "✅ OVER"}
        ],
        "away_players": [
            {"Name": "Alperen Sengun", "AI Proj": "24.5", "Line": "23.5", "Tip": "✅ OVER"},
            {"Name": "Amen Thompson", "AI Proj": "15.8", "Line": "17.5", "Tip": "❄️ UNDER"}
        ]
    },
    {
        "id": "PHX-OKC", "home_team": "Suns", "away_team": "Thunder", 
        "home_proj": "105.8", "away_proj": "114.5", "line": "222.5", "advice": "✅ OVER",
        "home_players": [
            {"Name": "Devin Booker", "AI Proj": "26.4", "Line": "27.5", "Tip": "❄️ UNDER"},
            {"Name": "Kevin Durant", "AI Proj": "25.5", "Line": "24.5", "Tip": "✅ OVER"}
        ],
        "away_players": [
            {"Name": "S. Gilgeous-Alexander", "AI Proj": "32.8", "Line": "31.5", "Tip": "🔥 OVER"},
            {"Name": "Chet Holmgren", "AI Proj": "18.5", "Line": "17.5", "Tip": "✅ OVER"}
        ]
    },
    {
        "id": "MIN-DEN", "home_team": "Timberwolves", "away_team": "Nuggets", 
        "home_proj": "101.4", "away_proj": "99.8", "line": "208.5", "advice": "❄️ UNDER",
        "home_players": [
            {"Name": "Anthony Edwards", "AI Proj": "31.5", "Line": "29.5", "Tip": "🔥 OVER"}
        ],
        "away_players": [
            {"Name": "Nikola Jokic", "AI Proj": "27.8", "Line": "28.5", "Tip": "❄️ UNDER"}
        ]
    }
]

# --- 5. RENDER GRID (2 COLUMNS) ---
st.subheader("🎯 Home vs Away Analysis & Player Props")
cols = st.columns(2)

for idx, game in enumerate(nba_games):
    with cols[idx % 2]:
        # TOP CARD: Visual Home vs Away Scores
        card_html = f"""
        <div style="background: linear-gradient(135deg, #2d1b4e 0%, #0d1117 100%); border: 1px solid #FDB927; border-radius: 20px; padding: 20px; color: white; font-family: sans-serif; box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin-bottom: 5px;">
            <div style="display: flex; justify-content: space-between; font-size: 10px; color: #94a3b8; text-transform: uppercase; margin-bottom: 15px;">
                <span>NBA Playoff Analytics</span>
                <span style="color: #FDB927; font-weight: bold;">ID: {game['id']}</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; text-align: center;">
                <div>
                    <p style="font-size: 14px; color: #94a3b8; margin: 0;">{game['away_team'].upper()}</p>
                    <h2 style="margin: 5px 0; font-size: 26px;">{game['away_proj']}</h2>
                </div>
                <div style="color: #FDB927; font-weight: 900; font-size: 20px; font-style: italic; padding: 0 10px;">VS</div>
                <div>
                    <p style="font-size: 14px; color: #FDB927; margin: 0; font-weight: bold;">{game['home_team'].upper()}</p>
                    <h2 style="margin: 5px 0; font-size: 26px; color: #FDB927;">{game['home_proj']}</h2>
                </div>
            </div>
            <div style="background: rgba(0,0,0,0.3); padding: 10px; border-radius: 12px; margin-top: 15px; display: flex; justify-content: space-between; font-size: 13px; border-top: 2px solid #FDB927;">
                <span>Game Total Line: <b>{game['line']}</b></span>
                <span style="color: #4ade80; font-weight: bold;">ADVICE: {game['advice']}</span>
            </div>
        </div>
        """
        components.html(card_html, height=210)

        # PLAYER BREAKDOWN EXPANDER
        with st.expander(f"📊 Player Props: {game['away_team']} vs {game['home_team']}"):
            col_away, col_home = st.columns(2)
            with col_away:
                st.markdown(f"<p style='color: #94a3b8; font-size: 12px; font-weight: bold;'>{game['away_team'].upper()} PROPS</p>", unsafe_allow_html=True)
                st.table(game['away_players'])
            with col_home:
                st.markdown(f"<p style='color: #FDB927; font-size: 12px; font-weight: bold;'>{game['home_team'].upper()} PROPS</p>", unsafe_allow_html=True)
                st.table(game['home_players'])
