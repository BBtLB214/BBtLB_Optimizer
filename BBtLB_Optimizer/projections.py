import pandas as pd

def generate_projections(players_df, model_data, opponent_stats):
    df = pd.merge(players_df, opponent_stats, on="Team", how="left")
    df["Proj_Med"] = df["Salary"] / 1000 * 2.5
    df["Proj_Floor"] = df["Proj_Med"] * 0.8
    df["Proj_Ceil"] = df["Proj_Med"] * 1.2
    df["Value"] = df["Proj_Med"] / df["Salary"]
    return df
