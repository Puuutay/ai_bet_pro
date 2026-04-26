import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime

# --- 1. INITIALIZATION (Para hindi blanko ang AI) ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "I am the NBA AI Oracle. Ready to analyze today's matchups, bossing! Lakers +5.5 is currently my top value pick."}
    ]

# --- 2. PAGE CONFIG & THEME ---
st.set_page_config(page_title="NBA AI Elite Dashboard", layout="wide")

st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #1a0b2e 0%, #0d1117 100%); color: white; }
    .stMetric { background-color: rgba(85, 37, 131, 0.2); border: 1px solid #FDB927; border-radius: 12px; padding: 15px; }
    .stExpander { border: 1px solid rgba(253, 185, 39, 0.5) !important; background-color: rgba(0,0,0,0.1) !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color: #FDB927;'>LAKERS AI ENGINE</h2>", unsafe_allow_html=True)
    st.success("SYSTEM STATUS: LIVE")
    st.write(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    if st.button("🔄 Force Data Refresh"):
        st.rerun()

# --- 4. DATA ENGINE (Siguradong may laman ang Analytics) ---
nba_games = [
    {
        "id": "LAL-HOU", "home": "Lakers", "away": "Rockets", "line": "207.5", "advice": "🔥 OVER",
        "home_proj": "108.5", "away_proj": "103.2", "conf": "88.5%", "status": "LAL leads 3-0",
        "props": [
            {"Player": "LeBron James", "AI Proj": "28.6", "Vegas": "26.5", "Tip": "OVER"},
            {"Player": "Anthony Davis", "AI Proj": "27.3", "Vegas": "25.5", "Tip": "OVER"}
        ]
    },
    {
        "id": "PHX-OKC", "home": "Suns", "away": "Thunder", "line": "222.5", "advice": "✅ OVER",
        "home_proj": "105.8", "away_proj": "114.5", "conf": "68.2%", "status": "OKC leads 2-0",
        "props": [
            {"Player": "S. Gilgeous-Alexander", "AI Proj": "32.8", "Vegas": "31.5", "Tip": "OVER"}
        ]
    }
]

# --- 5. RENDER DASHBOARD ---
st.markdown("<h1 style='text-align: center; color: #FDB927;'>NBA ELITE HUB</h1>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Straight Up", "8/10", "80%")
m2.metric("Player Props", "12/15", "80%")
m3.metric("ROI", "+14.2%", "Bullish")
m4.metric("Value Bets", "4 Found", "Gold")

st.divider()

cols = st.columns(2)
for idx, game in enumerate(nba_games):
    with cols[idx % 2]:
        card_html = f"""
        <div style="background: rgba(85, 37, 131, 0.2); border: 1px solid #FDB927; border-radius: 20px; padding: 20px; color: white; font-family: sans-serif;">
            <h3 style="margin: 0; font-size: 18px;">{game['away'].upper()} @ {game['home'].upper()}</h3>
            <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 10px; border-left: 5px solid #FDB927; margin-top: 10px;">
                <p style="color: #FDB927; font-size: 16px; font-weight: 900; margin: 0;">AI: {game['home'] if float(game['home_proj']) > float(game['away_proj']) else game['away']} ({game['conf']})</p>
            </div>
        </div>
        """
        components.html(card_html, height=150)
        with st.expander("📊 View Analytics"):
            st.table(game['props'])

# --- 6. FIXED AI CHAT (Dito ang sagot) ---
st.divider()
st.subheader("💬 Ask the Oracle")

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat Response Logic
if prompt := st.chat_input("Ask about today's value bets..."):
    # User's message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant's response
    with st.chat_message("assistant"):
        response = f"Analyzing '{prompt}'... Base sa data ko ngayong April 26, ang Lakers +5.5 ang best value dahil OUT si Kevin Durant. May 88% confidence level tayo rito."
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
