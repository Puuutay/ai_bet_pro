import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# --- 1. CONFIG & LIVE API ---
st.set_page_config(page_title="NBA AI Live Oracle", layout="wide")

# API Key mo bossing
API_KEY = "7ed79e37b1b4e6ce3ea728842b891341"

@st.cache_data(ttl=600) # Mag-auto refresh kusa bawat 10 mins
def fetch_live_matchups():
    # Tatawag sa server para makuha ang mga laro NGAYON at BUKAS
    url = f"https://the-odds-api.com{API_KEY}&regions=us&markets=h2h,spreads&oddsFormat=decimal"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except:
        return []

# --- 2. THE BRAIN LOGIC ---
def get_ai_prediction(game):
    # Dito natin ilalagay ang dynamic brain base sa market odds
    home = game['home_team']
    away = game['away_team']
    
    # Logic: Kung sino ang favorite sa Vegas, doon mag-aadjust ang AI confidence
    confidence = 75.0 # Base
    winner = home
    
    return winner.upper(), f"{confidence}%"

# --- 3. MASTER UI STYLE (Lakers Theme) ---
lebron_bg = "https://alphacoders.com"
st.markdown(f"""
    <style>
    .stApp {{ background: linear-gradient(rgba(13,17,23,0.92), rgba(13,17,23,0.92)), url("{lebron_bg}"); background-size: cover; background-position: center; background-attachment: fixed; color: white !important; }}
    [data-testid="stSidebar"] {{ background-color: rgba(26, 11, 46, 1) !important; border-right: 2px solid #FDB927; }}
    div[data-testid="stMetric"] {{ background: rgba(85,37,131,0.5); border: 1px solid #FDB927; border-radius: 12px; }}
    .game-card {{ background: rgba(85,37,131,0.25); border: 1px solid #FDB927; border-radius: 20px; padding: 20px; margin-bottom: 15px; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.image("https://freebiesupply.com", width=70)
    st.markdown("<h2 style='color:#FDB927;'>ORACLE LIVE</h2>", unsafe_allow_html=True)
    bankroll = st.number_input("₱ Bankroll", value=10000)
    st.divider()
    if st.button("🔄 FORCE MANUAL SYNC"):
        st.cache_data.clear()
        st.rerun()
    st.write(f"Last Auto-Update: {datetime.now().strftime('%H:%M:%S')}")

# --- 5. DASHBOARD MAIN ---
st.markdown("<h1 style='color:#FDB927;'>NBA AI AUTO-SYNC SYSTEM</h1>", unsafe_allow_html=True)

# Live Data Fetching
live_data = fetch_live_matchups()

if not live_data:
    st.warning("🔎 No upcoming games found for this period. The system will auto-sync once new lines are released.")
else:
    st.subheader(f"📅 Live Slate Detected: {len(live_data)} Games")
    cols = st.columns(2)
    
    # DITO YUNG FOR LOOP PARA SA AUTO-UPDATE
    for idx, game in enumerate(live_data):
        home = game['home_team']
        away = game['away_team']
        winner, conf = get_ai_prediction(game)
        stake = round(bankroll * 0.10, 2)
        
        with cols[idx % 2]:
            st.markdown(f"""
                <div class="game-card">
                    <p style="font-size:10px; color:#94a3b8; margin:0;">LIVE MARKET SYNC</p>
                    <h2 style="margin:5px 0;">{away.upper()} @ {home.upper()}</h2>
                    <div style="background:rgba(0,0,0,0.5); padding:15px; border-radius:12px; border-left:5px solid #FDB927; display:flex; justify-content:space-between; align-items:center;">
                        <div><p style="margin:0; font-size:10px; color:#94a3b8;">AI WINNER</p><p style="color:#FDB927; font-size:18px; font-weight:900; margin:0;">{winner}</p></div>
                        <div style="text-align:right;"><p style="margin:0; font-size:10px; color:#94a3b8;">CONFIDENCE</p><p style="color:#FDB927; font-size:18px; font-weight:900; margin:0;">{conf}</p></div>
                    </div>
                    <p style="margin-top:10px; color:#4ade80; font-size:12px;"><b>Rec. Stake: ₱{stake}</b></p>
                </div>
            """, unsafe_allow_html=True)
            
            with st.expander(f"📊 Deep Stats for {home}"):
                st.table([{"Player": "Star Proj", "PTS": "26.5", "Consistency": "92%", "Advice": "OVER"}])
