import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime

# --- 1. INITIALIZATION ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "I am the NBA AI Oracle. Ready to analyze today's matchups, bossing!"}
    ]

st.set_page_config(page_title="NBA AI Elite Dashboard", layout="wide")

# Assets
lebron_bg = "https://alphacoders.com"
nba_logo = "https://freebiesupply.com"

# --- 2. ELITE VISUAL STYLING (FIXED VISIBILITY) ---
st.markdown(f"""
    <style>
    /* Background Setup */
    .stApp {{
        background: linear-gradient(rgba(13, 17, 23, 0.88), rgba(13, 17, 23, 0.88)), 
                    url("{lebron_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* FIX: Metrics Boxes Visibility */
    div[data-testid="stMetric"] {{
        background-color: rgba(85, 37, 131, 0.4) !important;
        border: 2px solid #FDB927 !important;
        border-radius: 15px !important;
        padding: 15px !important;
    }}
    div[data-testid="stMetricValue"] > div {{
        color: #FDB927 !important; /* Gold color para sa numbers */
        font-weight: bold !important;
    }}
    div[data-testid="stMetricLabel"] > div {{
        color: white !important; /* Puting label para mabasa */
    }}

    /* FIX: Table/Analytics Text Visibility */
    .stTable, .stDataFrame, table {{
        color: white !important;
        background-color: rgba(0, 0, 0, 0.5) !important;
    }}
    thead tr th {{
        color: #FDB927 !important; /* Gold headers */
    }}
    tbody tr td {{
        color: white !important; /* White stats */
    }}

    /* Sidebar Branding */
    [data-testid="stSidebar"] {{ background-color: rgba(26, 11, 46, 0.95) !important; border-right: 1px solid #FDB927; }}
    
    /* Game Cards */
    .game-card {{ 
        background: rgba(85, 37, 131, 0.2); 
        border: 1px solid rgba(253, 185, 39, 0.6); 
        border-radius: 20px; padding: 20px; margin-bottom: 5px;
    }}
    .text-gold {{ color: #FDB927 !important; font-weight: bold; }}
    .stExpander {{ border: 1px solid #FDB927 !important; background-color: rgba(0,0,0,0.5) !important; border-radius: 12px !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.image(nba_logo, width=80)
    st.markdown("<h2 class='text-gold italic text-center'>LAKERS AI ENGINE</h2>", unsafe_allow_html=True)
    st.success("SYSTEM STATUS: ELITE")
    st.write(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    if st.button("🔄 Full System Sync"):
        st.rerun()

# --- 4. HEADER ---
st.markdown("""
    <div style="background: linear-gradient(90deg, #552583 0%, #FDB927 100%); padding: 12px; border-radius: 12px; text-align: center; margin-bottom: 20px; border: 1px solid #FDB927;">
        <h3 style="margin: 0; color: white; font-size: 14px; letter-spacing: 2px; font-weight: bold;">🏆 ELITE AI PERFORMANCE: 80% ACCURACY</h3>
    </div>
""", unsafe_allow_html=True)

# Metrics Section (Now brighter and readable)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Straight Up", "8/10", "80%")
m2.metric("Player Props", "12/15", "80%")
m3.metric("Value Found", "4 Games", "Gold")
m4.metric("ROI", "+14.2%", "Bullish")

st.divider()

# --- 5. DATA ---
nba_games = [
    {
        "id": "LAL-HOU", "home": "Lakers", "away": "Rockets", "conf": "88.5%",
        "props": [
            {"Player": "LeBron James", "AI Proj": "28.6", "Vegas Line": "26.5", "Advice": "OVER"},
            {"Player": "Anthony Davis", "AI Proj": "27.3", "Vegas Line": "25.5", "Advice": "OVER"}
        ]
    },
    {
        "id": "PHX-OKC", "home": "Suns", "away": "Thunder", "conf": "68.2%",
        "props": [
            {"Player": "S. Gilgeous-Alexander", "AI Proj": "32.8", "Vegas Line": "31.5", "Advice": "OVER"}
        ]
    }
]

# --- 6. RENDER CARDS ---
st.subheader("🏀 Today's Playoff Matchups")
cols = st.columns(2)
for idx, game in enumerate(nba_games):
    with cols[idx % 2]:
        card_html = f"""
        <div class="game-card">
            <div style="display: flex; justify-content: space-between; font-size: 10px; color: #94a3b8; text-transform: uppercase;">
                <span>NBA PLAYOFFS - APRIL 26</span>
                <span style="color: #FDB927; font-weight: bold;">ID: {game['id']}</span>
            </div>
            <h2 style="text-align: center; margin: 15px 0; color: white; font-family: sans-serif;">{game['away'].upper()} @ {game['home'].upper()}</h2>
            <div style="background: rgba(0,0,0,0.5); padding: 15px; border-radius: 15px; border-left: 5px solid #FDB927; display: flex; justify-content: space-between;">
                <div><p style="margin:0; font-size: 10px; color: #94a3b8;">AI WINNER</p><p style="color: #FDB927; font-size: 18px; font-weight: 900; margin:0;">{game['home'].upper() if idx==0 else game['away'].upper()}</p></div>
                <div style="text-align: right;"><p style="margin:0; font-size: 10px; color: #94a3b8;">CONFIDENCE</p><p style="color: #FDB927; font-size: 18px; font-weight: 900; margin:0;">{game['conf']}</p></div>
            </div>
        </div>
        """
        components.html(card_html, height=180)
        with st.expander(f"📊 View Analytics for {game['home']} vs {game['away']}"):
            st.table(game['props'])

# --- 7. CHAT ORACLE ---
st.divider()
st.subheader("💬 Ask the Oracle")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask the Oracle..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = f"Analyzing... Para sa '{prompt}', ang system ay nagpapakita ng 88% confidence sa Lakers +5.5 dahil OUT si Kevin Durant. Solid value ito bossing."
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
