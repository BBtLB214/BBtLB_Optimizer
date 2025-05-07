import os
from BBtLB_Optimizer.fetchers import fetch_api_data, load_model_data, get_opponent_stats, load_props_data
from BBtLB_Optimizer.projections import get_player_projections
from BBtLB_Optimizer.lineup_generator import generate_lineup
from BBtLB_Optimizer.props_selector import generate_prop_combos
from BBtLB_Optimizer.output import output_lineups
from sheets_connector import write_to_sheet

# Environment configuration
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID", "14cQkxZSrMiTBlMMrFXg7V3M-sF1vMdErvHiX29yXFgU")
GOOGLE_CREDS_PATH = os.getenv("GOOGLE_SHEETS_CREDENTIALS", "credentials/psychic-raceway-459107-q0-4e66ae2a0716.json")

# Placeholder position constraints
dk_position_constraints = {}  # Example: {'QB': 1, 'RB': 2, 'WR': 3, ...}
fd_position_constraints = {}

def run_optimizer():
    # Fetch and prepare data
    api_data = fetch_api_data()
    model_data = load_model_data()
    opponent_stats = get_opponent_stats()
    props_data = load_props_data()

    projections = get_player_projections(api_data, model_data, opponent_stats)

    # Generate lineups
    dk_lineups = generate_lineup(projections, salary_cap=50000, position_constraints=dk_position_constraints, is_gpp=True)
    fd_lineups = generate_lineup(projections, salary_cap=60000, position_constraints=fd_position_constraints, is_gpp=True)

    # Generate prop combos
    prop_combos = generate_prop_combos(projections.keys(), props_data)

    # Output to local files
    output_lineups(dk_lineups, 'draftkings_lineups.csv')
    output_lineups(fd_lineups, 'fanduel_lineups.csv')
    output_lineups(prop_combos, 'props_combos.csv')

    # Write to Google Sheets
    sheet_output = [["Player", "Stat", "Line"]] + [[combo[0], combo[1], combo[2]] for combo in prop_combos]
    updated_cells = write_to_sheet(GOOGLE_SHEET_ID, 'Sheet1!G1', sheet_output, GOOGLE_CREDS_PATH)
    print(f"{updated_cells} cells updated in Google Sheet.")

if __name__ == "__main__":
    run_optimizer()
