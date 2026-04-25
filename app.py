import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="NBA AI Elite Hub", layout="wide")

st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #1a0b2e 0%, #0d1117 100%); }
    .stMetric { background-color: rgba(85, 37, 131, 0.2); border: 1px solid #FDB927; border-radius: 15px; padding: 15px; color: white; }
    .stExpander { border: 1px solid rgba(253, 185, 39, 0.5) !important; background-color: rgba(0,0,0,0.2) !important; border-radius: 12px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color: #FDB927; font-style: italic;'>LAKERS AI ENGINE</h2>", unsafe_allow_html=True)
    st.success("SYSTEM STATUS: LIVE")
    st.info("Mode: Full Prop Analytics")
    if st.button("🔄 Sync Live Market Data"):
        st.rerun()

# --- 3. HEADER ---
st.markdown("<h1 style='text-align: center; color: #FDB927;'>NBA ELITE PREDICTION HUB</h1>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Predictive Accuracy", "92.4%", "Stable")
m2.metric("Active Series", "8", "First Round")
m3.metric("Value Props Found", "12", "Gold Alert")
m4.metric("Market ROI", "+14.2%", "Bullish")

st.divider()

# --- 4. DATA ENGINE (Fixed Structure) ---
nba_games = [
    {
        "home": "Lakers", "away": "Rockets", "winner": "LAKERS", "conf": "88.5%", "sq": "61.2%", "id": "LAL-HOU",
        "note": "KD OUT: Rockets Defense -18.5%", "status": "9:30 PM ET",
        "props": [
            {"Name": "LeBron James", "AI Proj": "28.6", "Vegas Line": "26.5", "Advice": "🔥 OVER"},
            {"Name": "Anthony Davis", "AI Proj": "27.3", "Vegas Line": "25.5", "Advice": "✅ OVER"},
            {"Name": "Alperen Sengun", "AI Proj": "24.5", "Vegas Line": "23.5", "Advice": "✅ OVER"}
        ]
    },
    {
        "home": "Suns", "away": "Thunder", "winner": "OKC THUNDER", "conf": "68.2%", "sq": "54.1%", "id": "PHX-OKC",
        "note": "OKC Leads 2-0; High Def Pressure", "status": "3:30 PM ET",
        "props": [
            {"Name": "S. Gilgeous-Alexander", "AI Proj": "32.8", "Vegas Line": "31.5", "Advice": "🔥 OVER"},
            {"Name": "Devin Booker", "AI Proj": "26.4", "Vegas Line": "27.5", "Advice": "❄️ UNDER"}
        ]
    },
    {
        "home": "Hawks", "away": "Knicks", "winner": "NY KNICKS", "conf": "59.8%", "sq": "52.4%", "id": "ATL-NYK",
        "note": "Series Tied 1-1", "status": "6:00 PM ET",
        "props": [
            {"Name": "Jalen Brunson", "AI Proj": "30.2", "Vegas Line": "28.5", "Advice": "🔥 OVER"},
            {"Name": "Trae Young", "AI Proj": "24.8", "Vegas Line": "26.5", "Advice": "❄️ UNDER"}
        ]
    },
    {
        "home": "Timberwolves", "away": "Nuggets", "winner": "T-WOLVES", "conf": "54.1%", "sq": "50.8%", "id": "MIN-DEN",
        "note": "UPSET ALERT: Gordon GTD", "status": "8:30 PM ET",
        "props": [
            {"Name": "Anthony Edwards", "AI Proj": "31.5", "Vegas Line": "29.5", "Advice": "🔥 OVER"},
            {"Name": "Nikola Jokic", "AI Proj": "27.8", "Vegas Line": "28.5", "Advice": "❄️ UNDER"}
        ]
    }
]

# --- 5. RENDER GRID ---
st.subheader("🔥 Today's Predictions & Player Props")
cols = st.columns(2)

for idx, game in enumerate(nba_games):
    with cols[idx % 2]:
        card_html = f"""
        <div style="background: linear-gradient(135deg, #2d1b4e 0%, #0d1117 100%); border: 1px solid #FDB927; border-radius: 20px; padding: 20px; font-family: sans-serif; color: white; margin-bottom: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            <div style="display: flex; justify-content: space-between; font-size: 11px; color: #94a3b8; text-transform: uppercase;">
                <span>{game['status']}</span>
                <span style="color: #FDB927;">ID: {game['id']}</span>
            </div>
            <h2 style="margin: 10px 0; font-size: 22px;">{game['away'].upper()} <span style="color: #FDB927;">@</span> {game['home'].upper()}</h2>
            <div style="background: rgba(0,0,0,0.4); padding: 15px; border-radius: 12px; border-left: 5px solid #FDB927; margin: 15px 0;">
                <p style="color: #94a3b8; font-size: 9px; margin: 0; text-transform: uppercase;">AI Winner</p>
                <p style="color: #FDB927; font-size: 24px; font-weight: 900; margin: 0;">{game['winner']}</p>
                <div style="display: flex; justify-content: space-between; margin-top: 10px; font-size: 13px;">
                    <span>Conf: <b>{game['conf']}</b></span>
                    <span>SQ: <b>{game['sq']}</b></span>
                </div>
            </div>
            <p style="color: #4ade80; font-size: 11px; margin: 0;"><b>ELITE INSIGHT:</b> {game['note']}</p>
        </div>
        """
        components.html(card_html, height=270)
        
        with st.expander(f"📊 Player Props: {game['away']} vs {game['home']}"):
            # Dito inayos ang error: Diretsong list of dicts na ang ipinasa
            st.table(game['props'])
