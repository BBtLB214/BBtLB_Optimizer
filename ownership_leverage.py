# ownership_leverage.py

import os
import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve API key from environment variables
SPORTSDATAIO_API_KEY = os.getenv("SPORTSDATAIO_API_KEY")

# Base URL for SportsDataIO's DFS Ownership Projections API
BASE_URL = "https://api.sportsdata.io/v4/nfl/dfs/ownership"

def fetch_ownership_projections():
    headers = {
        "Ocp-Apim-Subscription-Key": SPORTSDATAIO_API_KEY
    }
    try:
        response = requests.get(BASE_URL, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching ownership projections: {e}")
        return None

def display_ownership_projections(data):
    if not data:
        print("No data to display.")
        return

    print("Player Ownership Projections:")
    print(f"{'Player':<25} {'Team':<10} {'Position':<10} {'DK Ownership':<15} {'FD Ownership':<15}")
    print("-" * 75)
    for player in data:
        name = player.get("Name", "N/A")
        team = player.get("Team", "N/A")
        position = player.get("Position", "N/A")
        dk_ownership = player.get("DraftKingsOwnershipPercentage", "N/A")
        fd_ownership = player.get("FanDuelOwnershipPercentage", "N/A")
        print(f"{name:<25} {team:<10} {position:<10} {dk_ownership:<15} {fd_ownership:<15}")

def main():
    data = fetch_ownership_projections()
    display_ownership_projections(data)

if __name__ == "__main__":
    main()
