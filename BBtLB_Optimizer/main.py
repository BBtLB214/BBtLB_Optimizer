from BBtLB_Optimizer.fetchers import fetch_api_data, load_model_data, get_opponent_stats, load_props_data
from BBtLB_Optimizer.projections import get_player_projections
from BBtLB_Optimizer.lineup_generator import generate_lineup
from BBtLB_Optimizer.props_selector import generate_prop_combos
from BBtLB_Optimizer.output import output_lineups

dk_position_constraints = {}
fd_position_constraints = {}

def run_optimizer():
    api_data = fetch_api_data()
    model_data = load_model_data()
    opponent_stats = get_opponent_stats()
    props_data = load_props_data()

    projections = get_player_projections(api_data, model_data, opponent_stats)

    dk_lineups = generate_lineup(projections, salary_cap=50000, position_constraints=dk_position_constraints, is_gpp=True)
    fd_lineups = generate_lineup(projections, salary_cap=60000, position_constraints=fd_position_constraints, is_gpp=True)

    prop_combos = generate_prop_combos(projections.keys(), props_data)

    output_lineups(dk_lineups, 'draftkings_lineups.csv')
    output_lineups(fd_lineups, 'fanduel_lineups.csv')
    output_lineups(prop_combos, 'props_combos.csv')

if __name__ == "__main__":
    run_optimizer()
