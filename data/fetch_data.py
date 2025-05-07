import os
import requests
from dotenv import load_dotenv
from espn_api.basketball import League

load_dotenv()

def fetch_sportsradar_data():
    api_key = os.getenv("SPORTS_RADAR_API_KEY")
    url = f"https://api.sportradar.com/nba/trial/v7/en/players/statistics.json?api_key={api_key}"
    response = requests.get(url)
    return response.json()

def fetch_odds_data():
    api_key = os.getenv("ODDS_API_KEY")
    url = f"https://api.the-odds-api.com/v4/sports/basketball_nba/odds/?apiKey={api_key}&regions=us&markets=h2h,spreads,totals"
    response = requests.get(url)
    return response.json()

def fetch_espn_fantasy_data():
    league_id = os.getenv("ESPN_LEAGUE_ID")
    season = os.getenv("ESPN_SEASON")
    swid = os.getenv("ESPN_SWID")
    espn_s2 = os.getenv("ESPN_S2")

    league = League(league_id=league_id, year=int(season), espn_s2=espn_s2, swid=swid)
    teams = league.teams
    players = league.free_agents(size=50)

    return {
        "teams": [team.team_name for team in teams],
        "players": [{
            "name": p.name,
            "position": p.position,
            "points": p.total_points,
            "injury_status": p.injuryStatus
        } for p in players]
    }

def fetch_all_data():
    return {
        "sportsradar": fetch_sportsradar_data(),
        "odds": fetch_odds_data(),
        "espn_fantasy": fetch_espn_fantasy_data()
    }
