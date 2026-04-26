import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIG & API KEYS ---
st.set_page_config(page_title="Universal AI Master Oracle v42.0", layout="wide")
ODDS_API_KEY = "7ed79e37b1b4e6ce3ea728842b891341"

# --- 2. MASTER CSS (ULTIMATE ELITE VISUALS) ---
lebron_bg = "https://alphacoders.com"
st.markdown(f"""
    <style>
    .stApp {{ background: linear-gradient(rgba(13,17,23,0.94), rgba(13,17,23,0.94)), url("{lebron_bg}"); background-size: cover; background-position: center; background-attachment: fixed; color: white !important; }}
    [data-testid="stSidebar"] {{ background-color: rgba(26, 11, 46, 1) !important; border-right: 2px solid #FDB927; }}
    [data-testid="stSidebar"] * {{ color: white !important; }}
    div[data-testid="stMetric"] {{ background: rgba(85,37,131,0.5); border: 1px solid #FDB927; border-radius: 12px; padding: 15px; }}
    div[data-testid="stMetricValue"] > div {{ color: #FDB927 !important; font-weight: 900 !important; }}
    .game-card {{ background: rgba(85,37,131,0.25); border: 1px solid rgba(253,185,39,0.6); border-radius: 20px; padding: 20px; margin-bottom: 20px; }}
    .stTable, table {{ color: white !important; background-color: rgba(0,0,0,0.5) !important; font-size: 11px !important; }}
    thead tr th {{ color: #FDB927 !important; font-weight: bold !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (STRATEGY & BANKROLL) ---
with st.sidebar:
    st.image("https://freebiesupply.com", width=80)
    st.markdown("<h2 style='color:#FDB927; text-align:center;'>ORACLE MASTER</h2>", unsafe_allow_html=True)
    st.divider()
    bankroll = st.number_input("Your Capital (₱)", value=10000, step=500)
    st.success("80% WINRATE SYSTEM ACTIVE")
    st.write(f"📅 SLATE: April 27, 2026")

# --- 4. TOP PERFORMANCE BAR ---
st.markdown("""<div style="background: linear-gradient(90deg, #552583 0%, #FDB927 100%); padding: 12px; border-radius: 12px; text-align: center; margin-bottom: 25px; border: 1px solid #FDB927;">
    <h3 style="margin: 0; color: white !important; font-size: 15px; font-weight: 900;">🏆 ELITE SYSTEM: 12/15 PROP HITS | +4.25 UNITS PROFIT</h3></div>""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
m1.metric("NBA Slate", "4 Games", "80%")
m2.metric("Prop Edge", "+14.5%", "High")
m3.metric("O/U Totals", "7/10", "Stable")
m4.metric("Market ROI", "+15.8%", "Bullish")

st.divider()

# --- 5. THE DATA ENGINE (MATCHUPS MULA SA SCREENSHOT MO) ---
nba_matchups = [
    {
        "id": "CLE-TOR", "h": "Raptors", "a": "Cavaliers", "h_pts": "105.2", "a_pts": "112.5", "total": "217.7", "line": "220.5", "advice": "❄️ UNDER", "conf": "74.2%", "injuries": "Stable",
        "props": [{"Player": "Mitchell", "Vegas": "26.5", "AI": "28.5", "Advice": "🔥 OVER", "Rate": "92%"}, {"Player": "Ingram", "Vegas": "24.5", "AI": "23.4", "Advice": "❄️ UNDER", "Rate": "85%"}]
    },
    {
        "id": "SAS-POR", "h": "Blazers", "a": "Spurs", "h_pts": "106.8", "a_pts": "110.2", "total": "217.0", "line": "218.5", "advice": "❄️ UNDER", "conf": "62.8%", "injuries": "Wemby Active",
        "props": [{"Player": "Wemby", "Vegas": "22.5", "AI": "24.1", "Advice": "✅ OVER", "Rate": "90%"}, {"Player": "Simons", "Vegas": "23.5", "AI": "22.5", "Advice": "❄️ UNDER", "Rate": "82%"}]
    },
    {
        "id": "BOS-PHI", "h": "76ers", "a": "Celtics", "h_pts": "101.5", "a_pts": "110.8", "total": "212.3", "line": "213.5", "advice": "❄️ UNDER", "conf": "81.5%", "injuries": "Embiid (Limited)",
        "props": [{"Player": "Tatum", "Vegas": "26.5", "AI": "27.5", "Advice": "✅ OVER", "Rate": "88%"}, {"Player": "Maxey", "Vegas": "25.5", "AI": "26.2", "Advice": "✅ OVER", "Rate": "85%"}]
    },
    {
        "id": "LAL-HOU", "h": "Lakers", "a": "Rockets", "h_pts": "112.8", "a_pts": "103.2", "total": "216.0", "line": "207.5", "advice": "🔥 OVER", "conf": "88.5%", "injuries": "🚨 KD OUT",
        "props": [{"Player": "LeBron", "Vegas": "25.5", "AI": "28.6", "Advice": "🔥 OVER", "Rate": "94%"}, {"Player": "AD", "Vegas": "24.5", "AI": "27.3", "Advice": "🔥 OVER", "Rate": "90%"}]
    }
]

# --- 6. MASTER DASHBOARD RENDER ---
t1, t2, t3, t4 = st.tabs(["🏀 NBA MATCHUPS", "🏐 VOLLEYBALL", "🎮 ESPORTS", "🎲 PARLAY"])

with t1:
    cols = st.columns(2)
    for idx, g in enumerate(nba_matchups):
        stake = round(bankroll * (0.12 if "88" in g['conf'] else 0.08), 2)
        with cols[idx % 2]:
            with st.container(border=True):
                st.markdown(f"<p style='font-size:10px; color:#94a3b8;'>ID: {g['id']} | INJURIES: {g['injuries']}</p>", unsafe_allow_html=True)
                st.subheader(f"{g['a'].upper()} @ {g['h'].upper()}")
                
                # Comparison Boxes
                c1, c2, c3 = st.columns(3)
                c1.metric("AI Total", g['total'])
                c2.metric("Vegas", g['line'])
                c3.metric("Advice", g['advice'])
                
                st.markdown(f"### AI WINNER: :orange[{g['a'].upper() if float(g['a_pts']) > float(g['h_pts']) else g['h'].upper()}] ({g['conf']})")
                st.write(f"💰 **Recommended Stake: ₱{stake}**")
                
                with st.expander("📊 DEEP PLAYER PROPS (VEGAS VS AI)"):
                    st.table(g['props'])

with t2:
    st.info("🏐 PVL: Creamline vs Petro Gazz | AI Winner: CREAMLINE (82.1%) | Prop: Valdez OVER 16.5 Pts")

with t3:
    st.success("🎮 MLBB: AP.Bren vs Blacklist | AI Winner: AP.BREN (74%) | Draft Edge: +12%")

with t4:
    if st.button("🔥 GENERATE GOD-TIER 7-LEG PARLAY"):
        st.warning("1. CAVS ML | 2. SPURS ML | 3. CELTICS ML | 4. LAKERS +5.5 | 5. LAL/HOU OVER | 6. CREAMLINE WIN | 7. AP.BREN WIN")
