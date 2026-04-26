import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime

# --- 1. INITIALIZATION ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "I am the NBA AI Oracle. Ready for the Playoff slate, bossing?"}]

st.set_page_config(page_title="NBA AI Elite Dashboard v13.5", layout="wide")

# Branding Assets
lebron_bg = "https://alphacoders.com"
nba_logo = "https://freebiesupply.com"

# --- 2. MASTER CSS (Lighting, Background, Table Fix) ---
st.markdown(f"""
    <style>
    /* Cinematic Background */
    .stApp {{
        background: linear-gradient(rgba(13, 17, 23, 0.9), rgba(13, 17, 23, 0.9)), 
                    url("{lebron_bg}");
        background-size: cover; background-position: center; background-attachment: fixed;
    }}
    
    /* Force Sidebar Visibility */
    [data-testid="stSidebar"] {{
        background-color: rgba(26, 11, 46, 1) !important;
        border-right: 2px solid #FDB927;
    }}
    [data-testid="stSidebar"] * {{ color: white !important; font-weight: bold; }}
    
    /* Metrics Boxes */
    div[data-testid="stMetric"] {{
        background-color: rgba(85, 37, 131, 0.5) !important;
        border: 2px solid #FDB927 !important;
        border-radius: 15px !important;
    }}
    div[data-testid="stMetricValue"] > div {{ color: #FDB927 !important; font-weight: 900 !important; }}
    div[data-testid="stMetricLabel"] > div {{ color: white !important; font-weight: bold !important; }}

    /* Tables Lighting */
    .stTable, table, td, th {{ color: white !important; font-size: 13px !important; }}
    thead tr th {{ color: #FDB927 !important; background-color: rgba(0,0,0,0.6) !important; }}

    /* Chat Oracle Visibility */
    .stChatMessage {{ background-color: rgba(85, 37, 131, 0.4) !important; border: 1px solid #FDB927 !important; }}
    .stChatMessage [data-testid="stMarkdownContainer"] p {{ color: white !important; }}

    /* Tabs Styling */
    .stTabs [data-baseweb="tab"] {{ color: white !important; font-weight: bold !important; }}
    .stTabs [aria-selected="true"] {{ color: #FDB927 !important; border-bottom-color: #FDB927 !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (Live Input) ---
with st.sidebar:
    st.image(nba_logo, width=80)
    st.markdown("<h2 style='color: #FDB927 !important; font-style: italic;'>LAKERS AI ENGINE</h2>", unsafe_allow_html=True)
    st.write(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    st.divider()
    bankroll = st.number_input("Your Bankroll (₱)", value=10000, step=500)
    st.info("System Mode: High-Confidence Analytics")

# --- 4. TOP PERFORMANCE HEADER ---
st.markdown("""<div style="background: linear-gradient(90deg, #552583 0%, #FDB927 100%); padding: 12px; border-radius: 12px; text-align: center; margin-bottom: 20px; border: 1px solid #FDB927;">
    <h3 style="margin: 0; color: white !important; font-size: 14px; font-weight: bold;">🏆 ELITE PERFORMANCE: 80% ACCURACY</h3></div>""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Straight Up", "8/10", "80%")
m2.metric("Player Props", "12/15", "80%")
m3.metric("Value Picks", "4 Today", "Gold")
m4.metric("ROI", "+14.2%", "Bullish")

st.divider()

# --- 5. TABS ---
tab1, tab2 = st.tabs(["🏀 NBA MATCHUPS", "🎲 PARLAY GENERATOR"])

with tab1:
    # DATA ENGINE
    nba_games = [
        {
            "id": "LAL-HOU", "home": "Lakers", "away": "Rockets", "conf": "88.5%", "winner": "LAKERS", 
            "stake": round(bankroll * 0.12, 2), "odds": "DK: -115 | FD: -110",
            "props": [{"Player": "LeBron James", "AI": "28.6", "Vegas": "26.5", "Tip": "OVER"}, {"Player": "Anthony Davis", "AI": "27.3", "Vegas": "25.5", "Tip": "OVER"}]
        },
        {
            "id": "PHX-OKC", "home": "Suns", "away": "Thunder", "conf": "68.2%", "winner": "THUNDER", 
            "stake": round(bankroll * 0.05, 2), "odds": "DK: +105 | FD: +108",
            "props": [{"Player": "S.G. Alexander", "AI": "32.8", "Vegas": "31.5", "Tip": "OVER"}]
        }
    ]
    
    cols = st.columns(2)
    for idx, game in enumerate(nba_games):
        with cols[idx % 2]:
            card_html = f"""<div style="background: rgba(85, 37, 131, 0.2); border: 1px solid #FDB927; border-radius: 20px; padding: 20px; color: white; font-family: sans-serif;">
                <div style="display: flex; justify-content: space-between; font-size: 10px; color: #94a3b8; text-transform: uppercase;">
                    <span>NBA Playoff Analytics</span>
                    <span style="color: #FDB927;">ID: {game['id']}</span>
                </div>
                <h2 style="text-align: center; margin: 15px 0; color: white;">{game['away'].upper()} @ {game['home'].upper()}</h2>
                <div style="background: rgba(0,0,0,0.5); padding: 15px; border-radius: 15px; border-left: 5px solid #FDB927; margin-top: 10px; display: flex; justify-content: space-between; align-items: center;">
                    <div><p style="margin:0; font-size: 10px; color: #94a3b8;">AI WINNER</p><p style="color: #FDB927 !important; font-size: 18px; font-weight: 900; margin:0;">{game['winner']}</p></div>
                    <div style="text-align: right;"><p style="margin:0; font-size: 10px; color: #94a3b8;">CONFIDENCE</p><p style="color: #FDB927 !important; font-size: 18px; font-weight: 900; margin:0;">{game['conf']}</p></div>
                </div>
                <div style="margin-top: 12px; display: flex; justify-content: space-between; font-size: 12px;">
                    <span style="color: #4ade80;"><b>Stake: ₱{game['stake']}</b></span>
                    <span style="color: #94a3b8; font-size: 11px;">{game['odds']}</span>
                </div>
            </div>"""
            components.html(card_html, height=210)
            with st.expander(f"📊 Deep Analytics: {game['home']} vs {game['away']}"):
                st.table(game['props'])

with tab2:
    st.subheader("🎲 AI Parlay Generator")
    if st.button("🔥 Generate 3-Leg Parlay"):
        st.markdown("""<div style="background: rgba(253, 185, 39, 0.1); border: 2px dashed #FDB927; padding: 20px; border-radius: 15px;">
            <p style="color: #FDB927; font-weight: bold; font-size: 18px;">🔥 3-LEG ELITE PARLAY (+595 Odds)</p>
            <p style="color: white; margin: 5px 0;">✅ <b>Lakers +5.5</b> (vs Rockets)</p>
            <p style="color: white; margin: 5px 0;">✅ <b>Celtics -7.5</b> (@ 76ers)</p>
            <p style="color: white; margin: 5px 0;">✅ <b>LeBron James OVER 26.5 PTS</b></p>
            <p style="color: #4ade80; font-size: 12px; margin-top: 10px;"><i>*AI Reasoning: KD is OUT, BOS leads momentum, LAL dominance in paint.</i></p></div>""", unsafe_allow_html=True)

# --- 6. CHAT ORACLE ---
st.divider()
st.subheader("💬 Ask the Multi-Sport Oracle")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]): st.markdown(msg["content"])

if prompt := st.chat_input("Ask about today's value bets..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    with st.chat_message("assistant"):
        response = f"Analyzing... Bossing, based on April 26 data, Lakers +5.5 is the top value play because KD is OUT. My confidence is 88%."
        st.markdown(response); st.session_state.messages.append({"role": "assistant", "content": response})
