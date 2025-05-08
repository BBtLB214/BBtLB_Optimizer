import numpy as np
from projection_engine import get_player_projections
import pandas as pd

SIMULATIONS = 10000

def simulate_player(player):
    try:
        median, floor, ceiling = map(float, player['Proj (Med/Floor/Ceil)'].split("/"))
    except:
        return np.zeros(SIMULATIONS)

    mean = median
    std = (ceiling - floor) / 2.326  # Approximate 90th-10th width
    return np.random.normal(loc=mean, scale=std, size=SIMULATIONS)

def simulate_all_players(players):
    simulation_matrix = {}

    for player in players:
        name = player['Player']
        if player['Knick Factor'] == "OUT":
            continue
        simulation_matrix[name] = simulate_player(player)

    return simulation_matrix

def summarize_simulations(sim_matrix):
    summary = []
    for player, sims in sim_matrix.items():
        summary.append({
            "Player": player,
            "Sim_Floor": round(np.percentile(sims, 20), 2),
            "Sim_Median": round(np.median(sims), 2),
            "Sim_Ceiling": round(np.percentile(sims, 90), 2),
            "Boom_Prob": round(np.mean(sims >= np.percentile(sims, 90)) * 100, 2),
            "Bust_Prob": round(np.mean(sims <= np.percentile(sims, 20)) * 100, 2),
            "Salary": 5000  # Default placeholder
        })
    return summary

def run_monte_carlo():
    base_proj = get_player_projections()
    sim_matrix = simulate_all_players(base_proj)
    sim_summary = summarize_simulations(sim_matrix)
    return pd.DataFrame(sim_summary)

if __name__ == "__main__":
    df = run_monte_carlo()
    print(df.head
