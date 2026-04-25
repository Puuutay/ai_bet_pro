import streamlit as st
import streamlit.components.v1 as components
import os
from datetime import datetime

# --- CONFIG ---
st.set_page_config(page_title="NBA Elite Hub", layout="wide")

# CSS para sa Metrics sa itaas
st.markdown("""
    <style>
    .main { background-color: #1a0b2e; }
    .stMetric { background-color: rgba(85, 37, 131, 0.2); border: 1px solid #FDB927; border-radius: 15px; padding: 15px; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #FDB927;'>NBA ELITE PREDICTION HUB</h1>", unsafe_allow_html=True)

# Metrics Row
m1, m2, m3, m4 = st.columns(4)
m1.metric("Accuracy", "92.4%", "Stable")
m2.metric("Games", "4", "Live")
m3.metric("Value Bets", "2", "Gold")
m4.metric("ROI", "+14.2%", "+1.1%")

st.divider()

# --- DATA ---
nba_games = [
    {"home": "Lakers", "away": "Rockets", "winner": "LAKERS", "conf": "88.5%", "sq": "61.2%", "id": "LAL-HOU", "note": "KD OUT: Rockets Defense -18%"},
    {"home": "Suns", "away": "Thunder", "winner": "OKC THUNDER", "conf": "65.2%", "sq": "54.1%", "id": "PHX-OKC", "note": "High Defensive Pressure"},
    {"home": "Hawks", "away": "Knicks", "winner": "NY KNICKS", "conf": "59.8%", "sq": "52.4%", "id": "ATL-NYK", "note": "Standard Matchup"},
    {"home": "Timberwolves", "away": "Nuggets", "winner": "T-WOLVES", "conf": "54.1%", "sq": "50.8%", "id": "MIN-DEN", "note": "Upset Alert: Gordon GTD"}
]

# --- RENDER CARDS ---
cols = st.columns(2)

for idx, game in enumerate(nba_games):
    with cols[idx % 2]:
        # Gagamit tayo ng components.html para siguradong gagana ang CSS at HTML
        card_code = f"""
        <div style="
            background: linear-gradient(135deg, #2d1b4e 0%, #1a0b2e 100%);
            border: 1px solid #FDB927;
            border-radius: 20px;
            padding: 20px;
            font-family: sans-serif;
            color: white;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            margin-bottom: 20px;
        ">
            <div style="display: flex; justify-content: space-between; font-size: 12px; color: #94a3b8; margin-bottom: 10px;">
                <span>NBA PLAYOFFS 2026</span>
                <span style="color: #FDB927; font-weight: bold;">ID: {game['id']}</span>
            </div>
            <h2 style="margin: 0; font-size: 24px; text-transform: uppercase;">{game['away']} <span style="color: #FDB927;">@</span> {game['home']}</h2>
            
            <div style="background: rgba(0,0,0,0.3); padding: 15px; border-radius: 12px; border-left: 5px solid #FDB927; margin: 15px 0;">
                <p style="color: #94a3b8; font-size: 10px; margin: 0 0 5px 0; text-transform: uppercase;">AI Predicted Winner</p>
                <p style="color: #FDB927; font-size: 22px; font-weight: 900; margin: 0;">{game['winner']}</p>
                <div style="display: flex; justify-content: space-between; margin-top: 10px; font-size: 14px;">
                    <span>Confidence: <b>{game['conf']}</b></span>
                    <span>Shot Quality: <b>{game['sq']}</b></span>
                </div>
            </div>
            <p style="color: #4ade80; font-size: 12px; margin: 0;"><b>INSIGHT:</b> {game['note']}</p>
        </div>
        """
        components.html(card_code, height=250)
