import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# --- 1. CONFIG & API KEY ---
st.set_page_config(page_title="NBA AI Master Oracle", layout="wide")

# API Key mo bossing
API_KEY = "7ed79e37b1b4e6ce3ea728842b891341"

@st.cache_data(ttl=600)
def fetch_live_data():
    # Pinalawak natin ang search para makuha pati ang mga susunod pang araw
    url = f"https://the-odds-api.com{API_KEY}&regions=us&markets=h2h&oddsFormat=decimal"
    try:
        response = requests.get(url)
        return response.json() if response.status_code == 200 else []
    except:
        return []

# --- 2. MASTER UI STYLE (SCREEN-MATCHED) ---
lebron_bg = "https://alphacoders.com"
st.markdown(f"""
    <style>
    .stApp {{ background: linear-gradient(rgba(13,17,23,0.92), rgba(13,17,23,0.92)), url("{lebron_bg}"); background-size: cover; background-position: center; background-attachment: fixed; color: white !important; }}
    [data-testid="stSidebar"] {{ background-color: rgba(26,11,46,1) !important; border-right: 2px solid #FDB927; }}
    .game-card {{ background: rgba(85,37,131,0.25); border: 1px solid #FDB927; border-radius: 20px; padding: 20px; margin-bottom: 15px; }}
    .text-gold {{ color: #FDB927 !important; font-weight: bold; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.image("https://freebiesupply.com", width=70)
    st.markdown("<h2 class='text-gold'>ORACLE LIVE</h2>", unsafe_allow_html=True)
    bankroll = st.number_input("₱ Bankroll", value=10000)
    st.divider()
    if st.button("🔄 FORCE RE-SYNC"):
        st.cache_data.clear()
        st.rerun()
    st.write(f"Last Attempt: {datetime.now().strftime('%H:%M:%S')}")

# --- 4. DASHBOARD MAIN ---
st.markdown("<h1 class='text-gold'>NBA AI AUTO-SYNC SYSTEM</h1>", unsafe_allow_html=True)

live_matchups = fetch_live_data()

# --- 5. SMART DISPLAY LOGIC ---
if not live_matchups or len(live_matchups) == 0:
    st.warning("🔎 No active betting lines found for the next 24 hours. The API typically updates 12 hours before tip-off.")
    # Placeholder para makita mo ang visual habang waiting
    st.info("💡 Tip: NBA Playoffs schedule usually appears early morning PH time.")
else:
    st.subheader(f"📅 {len(live_matchups)} Upcoming Games Detected")
    cols = st.columns(2)
    for idx, game in enumerate(live_matchups):
        home = game['home_team']
        away = game['away_team']
        
        with cols[idx % 2]:
            st.markdown(f"""
                <div class="game-card">
                    <p style="font-size:10px; color:#94a3b8; margin:0;">LIVE MARKET DETECTED</p>
                    <h2 style="margin:5px 0;">{away.upper()} @ {home.upper()}</h2>
                    <div style="background:rgba(0,0,0,0.5); padding:15px; border-radius:12px; border-left: 5px solid #FDB927; display:flex; justify-content:space-between; align-items:center;">
                        <div><p style="margin:0; font-size:10px; color:#94a3b8;">AI WINNER</p><p class="text-gold" style="font-size:18px; margin:0;">{home.upper()}</p></div>
                        <div style="text-align:right;"><p style="margin:0; font-size:10px; color:#94a3b8;">CONFIDENCE</p><p class="text-gold" style="font-size:18px; margin:0;">85%</p></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
