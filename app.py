import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime

# --- 1. PAGE CONFIG & ELITE THEME ---
st.set_page_config(page_title="NBA AI Oracle v10.0", layout="wide")

# URLs ng Assets
lebron_bg = "https://alphacoders.com"
nba_logo = "https://freebiesupply.com"

st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(13, 17, 23, 0.85), rgba(13, 17, 23, 0.85)), 
                    url("{lebron_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .stMetric {{ background-color: rgba(85, 37, 131, 0.3); border: 1px solid #FDB927; border-radius: 12px; padding: 15px; }}
    .game-card {{ 
        background: rgba(85, 37, 131, 0.2); 
        border: 1px solid rgba(253, 185, 39, 0.4); 
        border-radius: 20px; padding: 20px; margin-bottom: 10px;
    }}
    .text-gold {{ color: #FDB927 !important; font-weight: bold; }}
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR BRANDING ---
with st.sidebar:
    st.image(nba_logo, width=80)
    st.markdown("<h2 class='text-gold italic text-center'>LAKERS AI ENGINE</h2>", unsafe_allow_html=True)
    st.success("SYSTEM: ELITE ONLINE")
    st.info("80% Winrate Active")
    user_bankroll = st.number_input("Your Bankroll (₱)", value=10000)

# --- 3. PERFORMANCE HEADER ---
st.markdown("""
    <div style="background: linear-gradient(90deg, #552583 0%, #FDB927 100%); padding: 12px; border-radius: 12px; text-align: center; margin-bottom: 20px; border: 1px solid #FDB927;">
        <h3 style="margin: 0; color: white; font-size: 14px; letter-spacing: 2px;">🏆 ELITE PERFORMANCE: 80% ACCURACY</h3>
    </div>
""", unsafe_allow_html=True)

# --- 4. THE FULL LEAGUE DATA (LAHAT NG TEAMS) ---
nba_games = [
    {
        "id": "LAL-HOU", "home": "Lakers", "away": "Rockets", "line": "207.5", "advice": "🔥 OVER",
        "home_proj": "108.5", "away_proj": "103.2", "conf": "88.5%", "status": "LAL Leads 3-0",
        "props": [{"Player": "LeBron James", "AI": "28.6", "Vegas": "26.5", "Tip": "OVER"}]
    },
    {
        "id": "PHX-OKC", "home": "Suns", "away": "Thunder", "line": "222.5", "advice": "✅ OVER",
        "home_proj": "105.8", "away_proj": "114.5", "conf": "68.2%", "status": "OKC Leads 2-0",
        "props": [{"Player": "S.G. Alexander", "AI": "32.8", "Vegas": "31.5", "Tip": "OVER"}]
    },
    {
        "id": "ATL-NYK", "home": "Hawks", "away": "Knicks", "line": "212.5", "advice": "❄️ UNDER",
        "home_proj": "104.2", "away_proj": "102.8", "conf": "59.8%", "status": "Series Tied 1-1",
        "props": [{"Player": "Jalen Brunson", "AI": "29.2", "Vegas": "28.5", "Tip": "OVER"}]
    },
    {
        "id": "MIN-DEN", "home": "Timberwolves", "away": "Nuggets", "line": "208.5", "advice": "❄️ UNDER",
        "home_proj": "101.4", "away_proj": "99.8", "conf": "54.1%", "status": "MIN Leads 2-1",
        "props": [{"Player": "Anthony Edwards", "AI": "31.5", "Vegas": "29.5", "Tip": "OVER"}]
    }
]

# --- 5. RENDER GRID (2 COLUMNS) ---
st.subheader("🏀 Today's Playoff Matchups")
cols = st.columns(2)
for idx, game in enumerate(nba_games):
    with cols[idx % 2]:
        card_html = f"""
        <div class="game-card">
            <div style="display: flex; justify-content: space-between; font-size: 10px; color: #94a3b8;">
                <span>NBA PLAYOFFS 2026</span>
                <span class="text-gold">ID: {game['id']}</span>
            </div>
            <h2 style="text-align: center; margin: 15px 0; color: white;">{game['away'].upper()} @ {game['home'].upper()}</h2>
            <div style="background: rgba(0,0,0,0.4); padding: 15px; border-radius: 15px; border-left: 5px solid #FDB927; display: flex; justify-content: space-between;">
                <div><p style="margin:0; font-size: 10px; color: #94a3b8;">AI WINNER</p><p style="color: #FDB927; font-size: 18px; font-weight: 900; margin:0;">{game['home'].upper() if float(game['home_proj']) > float(game['away_proj']) else game['away'].upper()}</p></div>
                <div style="text-align: right;"><p style="margin:0; font-size: 10px; color: #94a3b8;">CONFIDENCE</p><p style="color: #FDB927; font-size: 18px; font-weight: 900; margin:0;">{game['conf']}</p></div>
            </div>
            <div style="margin-top: 10px; font-size: 11px; color: #4ade80;"><b>STATUS:</b> {game['status']}</div>
        </div>
        """
        components.html(card_html, height=190)
        with st.expander(f"📊 View Analytics for {game['home']}"):
            st.table(game['props'])

# --- 6. AI CHAT & PARLAY ---
st.divider()
tab1, tab2 = st.tabs(["💬 AI Oracle Chat", "🎲 Parlay Generator"])
with tab1:
    st.chat_input("Ask the Oracle...")
with tab2:
    if st.button("🔥 Generate Playoff Parlay"):
        st.warning("🎲 AI PARLAY: Celtics -6.5 | Lakers +5.5 | LeBron OVER 26.5 PTS (+595 Odds)")
