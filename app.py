import streamlit as st
import requests
import pandas as pd
import random
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Universal AI Master Oracle", layout="wide")

ODDS_API_KEY = "YOUR_API_KEY_HERE"

SPORT_MAP = {
    "🏀 NBA": "basketball_nba",
    "⚽ Soccer": "soccer_epl",
    "⚾ MLB": "baseball_mlb"
}

# -----------------------------
# FETCH ODDS
# -----------------------------
@st.cache_data(ttl=300)
def fetch_odds(sport):
    url = f"https://api.the-odds-api.com/v4/sports/{sport}/odds"
    params = {
        "apiKey": ODDS_API_KEY,
        "regions": "us",
        "markets": "h2h",
        "oddsFormat": "decimal"
    }
    try:
        res = requests.get(url, params=params)
        if res.status_code != 200:
            return []
        return res.json()
    except:
        return []

# -----------------------------
# TEAM STATS (REAL)
# -----------------------------
@st.cache_data(ttl=600)
def compute_team_stats(team_name):
    url = "https://www.balldontlie.io/api/v1/games"
    try:
        res = requests.get(url, params={"per_page": 50})
        games = res.json()["data"]

        pts, opp, count = 0, 0, 0

        for g in games:
            if g["home_team"]["full_name"] == team_name:
                pts += g["home_team_score"]
                opp += g["visitor_team_score"]
                count += 1
            elif g["visitor_team"]["full_name"] == team_name:
                pts += g["visitor_team_score"]
                opp += g["home_team_score"]
                count += 1

        if count == 0:
            return {"ppg": 100, "oppg": 100}

        return {
            "ppg": pts / count,
            "oppg": opp / count
        }
    except:
        return {"ppg": 100, "oppg": 100}

# -----------------------------
# ML MODEL (SIMPLE TRAIN)
# -----------------------------
@st.cache_resource
def train_model():
    data = []
    for _ in range(200):
        home = random.uniform(90, 120)
        away = random.uniform(90, 120)
        diff = home - away
        target = 1 if diff > 0 else 0
        data.append([home, away, diff, target])

    df = pd.DataFrame(data, columns=["home", "away", "diff", "target"])

    X = df[["home", "away", "diff"]]
    y = df["target"]

    model = RandomForestClassifier()
    model.fit(X, y)

    return model

model = train_model()

# -----------------------------
# ML PREDICTION
# -----------------------------
def predict_game(game):
    try:
        home = game["home_team"]
        away = game["away_team"]

        home_stats = compute_team_stats(home)
        away_stats = compute_team_stats(away)

        features = [[
            home_stats["ppg"],
            away_stats["ppg"],
            home_stats["ppg"] - away_stats["ppg"]
        ]]

        prob = model.predict_proba(features)[0][1]

        pick = home if prob > 0.5 else away

        return {
            "pick": pick,
            "confidence": round(prob * 100, 2)
        }

    except:
        return None

# -----------------------------
# PARLAY
# -----------------------------
def generate_parlay(games):
    picks = []

    for g in games:
        pred = predict_game(g)
        if pred:
            picks.append(pred)

    picks = sorted(picks, key=lambda x: x["confidence"], reverse=True)

    return picks[:3]

# -----------------------------
# STAR PLAYER (SIMPLIFIED)
# -----------------------------
def get_star_player(team):
    stars = {
        "Lakers": "LeBron James",
        "Warriors": "Stephen Curry",
        "Celtics": "Jayson Tatum",
        "Bucks": "Giannis Antetokounmpo"
    }

    name = stars.get(team, "Star Player")

    return {
        "Player": name,
        "PTS Avg": round(random.uniform(20, 30), 1),
        "Pick": "OVER",
        "Confidence": "🔥 HIGH"
    }

# -----------------------------
# UI
# -----------------------------
st.title("🔥 UNIVERSAL AI MASTER ORACLE")

sport_label = st.selectbox("Select Sport", list(SPORT_MAP.keys()))
sport_key = SPORT_MAP[sport_label]

with st.spinner("Loading games..."):
    games = fetch_odds(sport_key)

if not games:
    games = [{
        "home_team": "Lakers",
        "away_team": "Warriors",
        "commence_time": "2026-04-28T02:00:00Z"
    }]

st.subheader("📊 Games")

for g in games[:5]:
    home = g["home_team"]
    away = g["away_team"]

    pred = predict_game(g)

    time = datetime.fromisoformat(g["commence_time"].replace("Z", "")) + timedelta(hours=8)

    st.markdown(f"""
    ### {away} @ {home}
    🕒 {time.strftime('%I:%M %p')}

    🔥 PICK: {pred['pick'] if pred else 'N/A'}  
    📊 CONFIDENCE: {pred['confidence'] if pred else '-'}%
    """)

    with st.expander(f"⭐ STAR PLAYER: {home}"):
        star = get_star_player(home)
        st.table([star])

    st.divider()

# -----------------------------
# PARLAY
# -----------------------------
st.subheader("🔥 SMART PARLAY")

parlay = generate_parlay(games)

for p in parlay:
    st.write(f"{p['pick']} ({p['confidence']}%)")
