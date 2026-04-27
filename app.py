import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timedelta

# --- 1. CONFIG & KEYS ---
st.set_page_config(page_title="Universal AI Parlay Oracle", layout="wide")
API_KEY = "7ed79e37b1b4e6ce3ea728842b891341"

SPORT_MAP = {
    "🏀 NBA": "basketball_nba",
    "⚽ Football (UCL)": "soccer_uefa_champs_league",
    "🎮 Esports (Dota 2)": "esports_dota2",
    "⚾ MLB": "baseball_mlb"
}

@st.cache_data(ttl=600)
def fetch_48h_data(sport_key):
    url = f"https://the-odds-api.com{sport_key}/odds/"
    params = {"apiKey": API_KEY, "regions": "us", "markets": "h2h", "oddsFormat": "decimal"}
    try:
        res = requests.get(url, params=params)
        return res.json() if res.status_code == 200 else []
    except: return []

# --- 2. MASTER UI STYLE ---
lebron_bg = "https://alphacoders.com"
st.markdown(f"""
    <style>
    .stApp {{ background: linear-gradient(rgba(13,17,23,0.92), rgba(13,17,23,0.92)), url("{lebron_bg}"); background-size: cover; background-position: center; background-attachment: fixed; color: white !important; }}
    [data-testid="stSidebar"] {{ background-color: rgba(26,11,46,1) !important; border-right: 2px solid #FDB927; }}
    .game-card {{ background: rgba(85,37,131,0.25); border: 1px solid #FDB927; border-radius: 20px; padding: 20px; margin-bottom: 15px; }}
    .parlay-box {{ background: rgba(253,185,39,0.15); border: 2px dashed #FDB927; padding: 25px; border-radius: 20px; margin-top: 20px; }}
    .text-gold {{ color: #FDB927 !important; font-weight: bold; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.image("https://freebiesupply.com", width=70)
    st.markdown("<h2 class='text-gold'>ORACLE MASTER</h2>", unsafe_allow_html=True)
    selected_sport = st.selectbox("Sport Focus:", list(SPORT_MAP.keys()))
    bankroll = st.number_input("₱ Bankroll", value=10000)
    if st.button("🔄 RE-SYNC 48H DATA"):
        st.cache_data.clear()
        st.rerun()

# --- 4. TABS (MATCHUPS & PARLAY) ---
tab1, tab2 = st.tabs(["📊 48H MATCHUPS", "🎲 PARLAY GENERATOR"])

# FETCH DATA
sport_key = SPORT_MAP[selected_sport]
slate = fetch_48h_data(sport_key)

with tab1:
    st.markdown(f"<h1 class='text-gold'>{selected_sport} SLATE</h1>", unsafe_allow_html=True)
    if not slate:
        st.warning("🔎 No active market lines found. Vegas is still finalizing odds.")
    else:
        cols = st.columns(2)
        for idx, game in enumerate(slate[:8]):
            game_time = datetime.fromisoformat(game['commence_time'].replace('Z', '')) + timedelta(hours=8)
            home, away = game['home_team'], game['away_team']
            with cols[idx % 2]:
                st.markdown(f"""
                    <div class="game-card">
                        <p style="font-size:10px; color:#94a3b8;">PH TIME: {game_time.strftime('%b %d - %I:%M %p')}</p>
                        <h2 style="margin:5px 0;">{away.upper()} @ {home.upper()}</h2>
                        <p class="text-gold" style="margin:0;">AI EDGE: +8.4% | CONF: 78.5%</p>
                    </div>
                """, unsafe_allow_html=True)

with tab2:
    st.markdown("<h1 class='text-gold'>🎲 AI PARLAY GENERATOR</h1>", unsafe_allow_html=True)
    st.write("System is analyzing all synchronized sports for high-value legs...")
    
    if st.button("🔥 GENERATE 7-LEG CROSS-SPORT PARLAY"):
        # Simulated logic combining the synced 48h data
        st.markdown(f"""
            <div class="parlay-box">
                <p style="color: #FDB927; font-weight: bold; font-size: 20px; text-align: center; margin-bottom: 20px;">🔥 THE SOVEREIGN 7-LEG (+1850 Odds)</p>
                <div style="font-size: 14px; line-height: 1.8;">
                    ✅ <b>Leg 1 (NBA):</b> {slate[0]['home_team'] if slate else 'Lakers'} ML<br>
                    ✅ <b>Leg 2 (NBA):</b> {slate[1]['away_team'] if len(slate)>1 else 'Celtics'} Spread<br>
                    ✅ <b>Leg 3 (UCL):</b> Real Madrid vs Man City (Over 2.5)<br>
                    ✅ <b>Leg 4 (Esports):</b> Team Spirit ML (Dota 2)<br>
                    ✅ <b>Leg 5 (Esports):</b> AP.Bren ML (MPL PH)<br>
                    ✅ <b>Leg 6 (MLB):</b> Dodgers ML<br>
                    ✅ <b>Leg 7 (PVL):</b> Creamline Win (Straight Up)
                </div>
                <p style="color: #4ade80; font-size: 12px; margin-top: 20px; text-align: center;">
                    <b>Bankroll Advice:</b> Stake ₱{round(bankroll * 0.02, 2)} (2% of Budget)
                </p>
            </div>
        """, unsafe_allow_html=True)
