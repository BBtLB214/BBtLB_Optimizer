# main.py

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from projection_engine import get_player_projections
from dk_fd_builder import run_optimizer as run_lineup_optimizer
from prop_picker import run_prop_picker
from sheets_connector import write_to_sheet

GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID", "14cQkxZSrMiTBlMMrFXg7V3M-sF1vMdErvHiX29yXFgU")
GOOGLE_CREDS_PATH = os.getenv("GOOGLE_SHEETS_CREDENTIALS", "credentials/psychic-raceway-459107-q0-4e66ae2a0716.json")


def run_optimizer():
    # Get player projections (BBtLB model)
    projections = get_player_projections()

    # Run DFS lineup optimizer
    lineups = run_lineup_optimizer()

    # Run correlated prop picks
    props = run_prop_picker()

    # Output prop picks to Google Sheets
    sheet_output = [["Player", "Prop", "Line", "Proj", "Edge", "Reason", "Risk"]]
    sheet_output += [[p['Player'], p['Prop'], p['Line'], p['Proj'], p['Edge'], p['Reason'], p['Risk']] for p in props]

    updated_cells = write_to_sheet(GOOGLE_SHEET_ID, 'Sheet1!G1', sheet_output, GOOGLE_CREDS_PATH)
    print(f"{updated_cells} cells updated in Google Sheet.")

    # Local print
    print("\nTop DraftKings Lineup:")
    for p in lineups['DraftKings'][0]:
        print(p)

    print("\nTop FanDuel Lineup:")
    for p in lineups['FanDuel'][0]:
        print(p)

    print("\nTop Props:")
    for p in props:
        print(p)


if __name__ == "__main__":
    run_optimizer()
