# BBtLB_Optimizer/ownership_leverage.py

import pandas as pd
from monte_carlo_sim import run_monte_carlo

# Threshold to identify good leverage opportunities
LEVERAGE_THRESHOLD = 1.5


def mock_ownership_projection(players):
    # Placeholder: Replace with real ownership projection logic
    # Assign mock ownership between 5-40%
    import numpy as np
    return {p['Player']: np.random.uniform(5, 40) for p in players}


def compute_leverage(sim_df: pd.DataFrame, ownership_map: dict):
    leverage_list = []
    for _, row in sim_df.iterrows():
        player = row['Player']
        median = row['Sim_Median']
        ownership = ownership_map.get(player, 10.0)

        leverage_score = round((median / row['Salary']) / (ownership / 100), 2)
        if leverage_score >= LEVERAGE_THRESHOLD:
            leverage_list.append({
                "Player": player,
                "Proj": median,
                "Ownership%": round(ownership, 2),
                "Leverage": leverage_score
            })

    return pd.DataFrame(leverage_list).sort_values(by="Leverage", ascending=False)


def run_leverage_analysis():
    sim_df = run_monte_carlo()
    sim_df['Salary'] = 5000  # Replace with actual salary feed if available
    ownership_map = mock_ownership_projection(sim_df.to_dict(orient='records'))
    leverage_df = compute_leverage(sim_df, ownership_map)
    return leverage_df


if __name__ == '__main__':
    df = run_leverage_analysis()
    print("Top Leverage Plays:")
    print(df.head(10))
