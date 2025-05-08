# ownership_leverage.py

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SPORTSDATAIO_API_KEY = os.getenv("SPORTSDATAIO_API_KEY")

def fetch_ownership_projections(sport: str, platform: str):
    """
    Fetch ownership projections from SportsDataIO.
    """
    url = f"https://api.sportsdata.io/v3/{sport}/dfs/projections"
    headers = {
        "Ocp-Apim-Subscription-Key": SPORTSDATAIO_API_KEY
    }
    params = {
        "platform": platform
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")

def calculate_leverage(projections):
    """
    Calculate leverage scores for each player.
    """
    total_ownership = sum(player['ProjectedOwnership'] for player in projections)
    average_ownership = total_ownership / len(projections)
    for player in projections:
        player['LeverageScore'] = player['ProjectedOwnership'] / average_ownership
    return projections

def main():
    sport = "nfl"  # or "nba", "mlb", etc.
    platform = "DraftKings"  # or "FanDuel"
    try:
        projections = fetch_ownership_projections(sport, platform)
        projections_with_leverage = calculate_leverage(projections)
        for player in projections_with_leverage:
            print(f"{player['Name']}: Leverage Score = {player['LeverageScore']:.2f}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
