import streamlit as st
import pandas as pd
import requests
from datetime import datetime
from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import leaguegamefinder, playercareerstats, playergamelog

# --- CONFIG (Palitan mo ng API Key mo o gamitin ang st.secrets) ---
ODDS_API_KEY = '7ed79e37b1b4e6ce3ea728842b891341'

st.set_page_config(page_title="NBA AI Analytics", layout="wide")
st.title("🏀 NBA Pro-Analytics & 1xBet Predictor")

tab1, tab2, tab3 = st.tabs(["Win/Loss & Fatigue", "Prop Predictor", "Player Stats"])

# --- FUNCTION PARA SA PAGOD (TRAVEL DISTANCE/B2B) ---
def get_fatigue_penalty(team_id):
    try:
        finder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
        games = finder.get_data_frames()
        last_game_date = pd.to_datetime(games.iloc[0]['GAME_DATE'])
        days_rest = (datetime.now() - last_game_date).days
        penalty = 0
        if days_rest <= 1: penalty -= 0.08  # Back-to-Back Penalty
        if "@" in games.iloc[0]['MATCHUP']: penalty -= 0.04 # Away/Travel Penalty
        return penalty
    except: return 0

# --- TAB 1: WIN/LOSS ANALYTICS ---
with tab1:
    col1, col2 = st.columns(2)
    all_teams = [t['full_name'] for t in teams.get_teams()]
    with col1: home_team = st.selectbox("Home Team", all_teams)
    with col2: away_team = st.selectbox("Away Team", all_teams)

    if st.button("Run AI Prediction"):
        h_id = [t['id'] for t in teams.get_teams() if t['full_name'] == home_team][0]
        a_id = [t['id'] for t in teams.get_teams() if t['full_name'] == away_team][0]
        h_penalty = get_fatigue_penalty(h_id)
        a_penalty = get_fatigue_penalty(a_id)
        
        final_prob = ( (0.55 + h_penalty) / ((0.55 + h_penalty) + (0.45 + a_penalty)) ) * 100
        st.metric(label=f"Win Chance: {home_team}", value=f"{final_prob:.1f}%")
        
        # CHART: Win Probability
        chart_data = pd.DataFrame({'Team': [home_team, away_team], 'Prob': [final_prob, 100-final_prob]})
        st.bar_chart(chart_data.set_index('Team'))

# --- TAB 2: PROP PREDICTOR ---
with tab2:
    p_name = st.text_input("Player Name", "Stephen Curry")
    p_line = st.number_input("1xBet Line", value=25.5)
    if st.button("Analyze Prop"):
        p_info = players.find_players_by_full_name(p_name)[0]
        log = playergamelog.PlayerGameLog(player_id=p_info['id']).get_data_frames()[0]
        last_10 = log.head(10)
        hit_rate = (last_10['PTS'] > p_line).mean() * 100
        
        st.write(f"### Hit Rate: {hit_rate:.1f}%")
        st.line_chart(last_10[['GAME_DATE', 'PTS']].set_index('GAME_DATE').sort_index())

# --- TAB 3: PLAYER STATS ---
with tab3:
    search_p = st.text_input("Search Player", "LeBron James")
    if st.button("Fetch Stats"):
        p_info = players.find_players_by_full_name(search_p)[0]
        stats = playercareerstats.PlayerCareerStats(player_id=p_info['id']).get_data_frames()[0]
        latest = stats.iloc[-1]
        st.write(f"**Season PPG:** {latest['PTS']/latest['GP']:.1f}")
        # CHART: Stat Breakdown
        st.bar_chart(pd.DataFrame({'Stat': ['PTS', 'REB', 'AST'], 'Value': [latest['PTS']/latest['GP'], latest['REB']/latest['GP'], latest['AST']/latest['GP']]}).set_index('Stat'))
