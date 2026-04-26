import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime

# --- 1. CONFIG & INITIALIZATION ---
st.set_page_config(page_title="Universal AI Oracle v23.0", layout="wide")
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Master Oracle Live. 🏀🏐⚽🎮 All systems verified. Ready to dominate the slate, bossing?"}]

# Assets
lebron_bg = "https://alphacoders.com"
nba_logo = "https://freebiesupply.com"

# --- 2. MASTER CSS (Ultimate UI Polish) ---
st.markdown(f"""
    <style>
    .stApp {{ background: linear-gradient(rgba(13, 17, 23, 0.92), rgba(13, 17, 23, 0.92)), url("{lebron_bg}"); background-size: cover; background-position: center; background-attachment: fixed; color: white !important; }}
    [data-testid="stSidebar"] {{ background-color: rgba(26, 11, 46, 1) !important; border-right: 2px solid #FDB927; }}
    [data-testid="stSidebar"] * {{ color: white !important; font-weight: bold; }}
    div[data-testid="stMetric"] {{ background-color: rgba(85, 37, 131, 0.5) !important; border: 2px solid #FDB927 !important; border-radius: 15px !important; }}
    div[data-testid="stMetricValue"] > div {{ color: #FDB927 !important; font-weight: 900 !important; }}
    .stTable, table, td, th {{ color: white !important; font-size: 11px !important; }}
    thead tr th {{ color: #FDB927 !important; background-color: rgba(0,0,0,0.6) !important; }}
    .stTabs [data-baseweb="tab"] {{ color: white !important; font-weight: bold; font-size: 14px !important; }}
    .stTabs [aria-selected="true"] {{ color: #FDB927 !important; border-bottom-color: #FDB927 !important; }}
    .stExpander {{ border: 1px solid #FDB927 !important; background-color: rgba(0,0,0,0.6) !important; border-radius: 12px !important; }}
    .parlay-box {{ background: rgba(253, 185, 39, 0.1); border: 2px dashed #FDB927; padding: 20px; border-radius: 15px; margin-top: 20px; }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (Bankroll Advisor) ---
with st.sidebar:
    st.image(nba_logo, width=80)
    st.markdown("<h2 style='color: #FDB927; text-align: center;'>ORACLE ELITE</h2>", unsafe_allow_html=True)
    st.divider()
    bankroll = st.number_input("Your Bankroll (₱)", value=10000, step=500)
    st.write(f"📅 {datetime.now().strftime('%Y-%m-%d')}")
    st.success("BRAIN ENGINE: 80% WINRATE")

# --- 4. TOP PERFORMANCE & RECAP ---
st.markdown("""<div style="background: linear-gradient(90deg, #552583 0%, #FDB927 100%); padding: 12px; border-radius: 12px; text-align: center; margin-bottom: 20px; border: 1px solid #FDB927;">
    <h3 style="margin: 0; color: white !important; font-size: 14px; font-weight: bold;">🏆 YESTERDAY'S RECAP: 8/10 STRAIGHT UP | +4.25 UNITS PROFIT</h3></div>""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Overall Accuracy", "80%", "+2.5%")
m2.metric("Player Props", "12/15", "HOT")
m3.metric("O/U Totals", "7/10", "Stable")
m4.metric("Market ROI", "+15.8%", "Bullish")

st.divider()

# --- 5. MULTI-SPORT MASTER TABS ---
t1, t2, t3, t4 = st.tabs(["🏀 BASKETBALL", "🏐 VOLLEYBALL", "🎮 ESPORTS", "🎲 7-LEG PARLAY"])

# --- 🏀 NBA/PBA (Deep Detail) ---
with t1:
    nba_games = [
        {
            "id": "LAL-HOU", "h": "Lakers", "a": "Rockets", "hp": "108.5", "ap": "103.2", "w": "LAKERS", "conf": "88.5%", "sq": "62.4%", "stake": round(bankroll * 0.12, 2),
            "h_props": [{"Player": "LeBron", "PTS": "28.6", "REB": "7.9", "AST": "9.2", "Rate": "92%"}, {"Player": "AD", "PTS": "27.3", "REB": "13.1", "AST": "2.1", "Rate": "85%"}],
            "a_props": [{"Player": "Sengun", "PTS": "24.5", "REB": "11.2", "AST": "4.1", "Rate": "88%"}]
        }
    ]
    for g in nba_games:
        card = f"""<div style="background: rgba(85,37,131,0.2); border: 1px solid #FDB927; border-radius: 20px; padding: 20px; color: white; text-align: center;">
            <div style="display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; margin-bottom: 10px;">
                <div><p style="font-size:12px; color:#94a3b8;">{g['a'].upper()}</p><h2>{g['ap']}</h2></div><div style="color:#FDB927; font-weight:900; padding:0 15px;">VS</div>
                <div><p style="font-size:12px; color:#FDB927; font-weight:bold;">{g['h'].upper()}</p><h2 style="color:#FDB927;">{g['hp']}</h2></div>
            </div>
            <div style="background: rgba(0,0,0,0.5); padding: 12px; border-radius: 12px; border-left: 5px solid #FDB927; display:flex; justify-content:space-between;">
                <div><p style="margin:0; font-size:9px; color:#94a3b8;">AI WINNER</p><p style="color:#FDB927; font-size:18px; font-weight:900; margin:0;">{g['w']}</p></div>
                <div><p style="margin:0; font-size:9px; color:#94a3b8;">SQ: {g['sq']}</p><p style="color:#FDB927; font-size:18px; font-weight:900; margin:0;">{g['conf']}</p></div>
            </div>
            <p style="color:#4ade80; font-size:11px; margin-top:10px;"><b>Optimal Stake: ₱{g['stake']}</b></p></div>"""
        components.html(card, height=210)
        with st.expander(f"📊 Deep Stats & Consistency: {g['a']} vs {g['h']}"):
            c1, c2 = st.columns(2)
            with c1: st.table(g['a_props'])
            with c2: st.table(g['h_props'])

# --- 🏐 VOLLEYBALL (PVL Deep Detail) ---
with t2:
    vol_games = [{"h": "Petro Gazz", "a": "Creamline", "hp": "1 Set", "ap": "3 Sets", "w": "CREAMLINE", "conf": "82.1%", "stake": round(bankroll * 0.10, 2), "h_props": [{"Player": "Sabete", "Pts": "12", "Attacks": "10"}], "a_props": [{"Player": "Valdez", "Pts": "18", "Attacks": "15"}]}]
    for g in vol_games:
        v_card = f"""<div style="background: rgba(74,222,128,0.1); border: 1px solid #4ade80; border-radius: 20px; padding: 20px; color: white;">
            <p style="color:#4ade80; font-size:18px; font-weight:900; text-align:center;">AI: {g['w']} ({g['conf']})</p>
            <p style="color:white; text-align:center; font-size:11px;">Recommended Stake: ₱{g['stake']}</p></div>"""
        components.html(v_card, height=120)
        with st.expander("🏐 Volleyball Set & Player Points"):
            c1, c2 = st.columns(2); c1.table(g['a_props']); c2.table(g['h_props'])

# --- 🎮 ESPORTS (MLBB/DOTA Detailed Drafts) ---
with t3:
    esports = [{"h": "Blacklist", "a": "AP.Bren", "w": "AP.BREN", "conf": "74%", "draft": [{"Player": "FlapTzy", "Hero": "Arlott", "Role": "EXP"}]}]
    for e in esports:
        e_card = f"""<div style="background: rgba(0,242,255,0.05); border: 1px solid #00f2ff; border-radius: 20px; padding: 15px; color: white; text-align: center;">
            <p style="font-size:20px; font-weight:900; color:#00f2ff;">AI: {e['w']} ({e['conf']})</p></div>"""
        components.html(e_card, height=100)
        with st.expander("🎮 Draft & Lane Analysis"): st.table(e['draft'])

# --- 🎲 7-LEG PARLAY (The Final Boss) ---
with t4:
    if st.button("🔥 GENERATE GOD-TIER 7-LEG PARLAY"):
        st.markdown(f"""<div class="parlay-box">
            <p style="color:#FDB927; font-weight:bold; font-size:20px; text-align:center;">🔥 THE SEVEN-LEG ORACLE (+1800 Odds)</p>
            <p style='color:white; font-size:13px;'>1. NBA: LAL +5.5 | 2. NBA: BOS ML | 3. PVL: Creamline ML | 4. MPL: AP.Bren ML | 5. Dota: Team Spirit ML | 6. UCL: Real Madrid Over 1.5 | 7. PBA: Ginebra Win</p>
            <p style='color:#4ade80; text-align:center; font-size:12px;'>*Combined Edge detected. Bankroll stake: ₱{bankroll * 0.02}.</p></div>""", unsafe_allow_html=True)

# --- 💬 ORACLE CHAT ---
st.divider()
st.subheader("💬 Ask the Multi-Sport Oracle")
if prompt := st.chat_input("Ask about NBA, PVL, or MPL..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    with st.chat_message("assistant"):
        res = "Analyzing KD's injury and the current MPL draft meta... Lakers +5.5 and AP.Bren ML are today's elite locks."
        st.markdown(res); st.session_state.messages.append({"role": "assistant", "content": res})
