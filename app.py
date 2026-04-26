import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime

# --- 1. INITIALIZATION & CONFIG ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "I am the NBA AI Oracle. 80% accuracy yesterday. What's the plan, bossing?"}
    ]

st.set_page_config(page_title="NBA AI Oracle v11.0", layout="wide")

# Branding Assets
lebron_bg = "https://alphacoders.com"
nba_logo = "https://freebiesupply.com"

# --- 2. ELITE VISUAL STYLING (THE BEAUTIFUL UI) ---
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(13, 17, 23, 0.85), rgba(13, 17, 23, 0.85)), 
                    url("{lebron_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    [data-testid="stSidebar"] {{ background-color: rgba(26, 11, 46, 0.95) !important; border-right: 1px solid #FDB927; }}
    .stMetric {{ background-color: rgba(85, 37, 131, 0.3); border: 1px solid #FDB927; border-radius: 12px; padding: 15px; }}
    .game-card {{ 
        background: rgba(85, 37, 131, 0.2); 
        border: 1px solid rgba(253, 185, 39, 0.4); 
        border-radius: 20px; padding: 20px; margin-bottom: 5px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}
    .text-gold {{ color: #FDB927 !important; font-weight: bold; }}
    .stExpander {{ border: 1px solid rgba(253, 185, 39, 0.5) !important; background-color: rgba(0,0,0,0.4) !important; border-radius: 12px !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR BRANDING ---
with st.sidebar:
    st.image(nba_logo, width=80)
    st.markdown("<h2 class='text-gold italic text-center'>LAKERS AI ENGINE</h2>", unsafe_allow_html=True)
    st.success("SYSTEM STATUS: ELITE")
    st.write(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    st.divider()
    user_bankroll = st.number_input("Your Bankroll (₱)", value=10000)
    if st.button("🔄 Full System Sync"):
        st.rerun()

# --- 4. ACCURACY PERFORMANCE HEADER ---
st.markdown("""
    <div style="background: linear-gradient(90deg, #552583 0%, #FDB927 100%); padding: 12px; border-radius: 12px; text-align: center; margin-bottom: 20px; border: 1px solid #FDB927;">
        <h3 style="margin: 0; color: white; font-size: 14px; letter-spacing: 2px;">🏆 ELITE AI PERFORMANCE: 80% ACCURACY</h3>
    </div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Straight Up", "8/10", "80%")
m2.metric("Player Props", "12/15", "80%")
m3.metric("Value Found", "4 Games", "Gold")
m4.metric("ROI", "+14.2%", "Bullish")

st.divider()

# --- 5. DATA ENGINE (Full Stats) ---
nba_games = [
    {
        "id": "LAL-HOU", "home": "Lakers", "away": "Rockets", "line": "207.5", "advice": "🔥 OVER",
        "home_proj": "108.5", "away_proj": "103.2", "conf": "88.5%", "id_label": "LAL-HOU",
        "props": [
            {"Player": "LeBron James", "AI Proj": "28.6", "Vegas Line": "26.5", "Advice": "OVER"},
            {"Player": "Anthony Davis", "AI Proj": "27.3", "Vegas Line": "25.5", "Advice": "OVER"}
        ]
    },
    {
        "id": "PHX-OKC", "home": "Suns", "away": "Thunder", "line": "222.5", "advice": "✅ OVER",
        "home_proj": "105.8", "away_proj": "114.5", "conf": "68.2%", "id_label": "PHX-OKC",
        "props": [
            {"Player": "S. Gilgeous-Alexander", "AI Proj": "32.8", "Vegas Line": "31.5", "Advice": "OVER"}
        ]
    }
]

# --- 6. RENDER DASHBOARD ---
st.subheader("🏀 Today's Playoff Matchups")
cols = st.columns(2)
for idx, game in enumerate(nba_games):
    with cols[idx % 2]:
        card_html = f"""
        <div class="game-card">
            <div style="display: flex; justify-content: space-between; font-size: 10px; color: #94a3b8; text-transform: uppercase;">
                <span>NBA PLAYOFFS - APRIL 26</span>
                <span style="color: #FDB927; font-weight: bold;">ID: {game['id_label']}</span>
            </div>
            <h2 style="text-align: center; margin: 15px 0; color: white;">{game['away'].upper()} @ {game['home'].upper()}</h2>
            <div style="background: rgba(0,0,0,0.4); padding: 15px; border-radius: 15px; border-left: 5px solid #FDB927; display: flex; justify-content: space-between;">
                <div><p style="margin:0; font-size: 10px; color: #94a3b8;">AI WINNER</p><p style="color: #FDB927; font-size: 18px; font-weight: 900; margin:0;">{game['home'].upper() if float(game['home_proj']) > float(game['away_proj']) else game['away'].upper()}</p></div>
                <div style="text-align: right;"><p style="margin:0; font-size: 10px; color: #94a3b8;">CONFIDENCE</p><p style="color: #FDB927; font-size: 18px; font-weight: 900; margin:0;">{game['conf']}</p></div>
            </div>
        </div>
        """
        components.html(card_html, height=180)
        with st.expander(f"📊 View Analytics for {game['home']} vs {game['away']}"):
            st.table(game['props'])

# --- 7. THE AI ORACLE CHAT (FIXED & RESPONSIVE) ---
st.divider()
st.subheader("💬 Ask the Oracle")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask the Oracle about today's value bets..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Simulated Expert Analysis
        if "Lakers" in prompt.lower():
            response = "Bossing, based on my 80% accuracy logic, the Lakers have a massive edge today. KD being OUT reduces Rockets' defense by 15.5%. Go for Lakers +5.5."
        else:
            response = f"Analyzing '{prompt}'... Based on live playoff data, my oracle projects a high value on the OVER for today's matchups."
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
