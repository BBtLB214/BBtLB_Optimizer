import pandas as pd

def fetch_api_data():
    return pd.DataFrame([
        {"Player": "John Doe", "Salary": 8000, "Team": "AAA"},
        {"Player": "Jane Smith", "Salary": 7500, "Team": "BBB"}
    ])

def load_model_data():
    return {}

def get_opponent_stats():
    return pd.DataFrame([
        {"Team": "AAA", "Defense_Rank": 5},
        {"Team": "BBB", "Defense_Rank": 15}
    ])

def load_props_data():
    return pd.DataFrame([
        {"Player": "John Doe", "Stat": "Points", "Line": 22.5},
        {"Player": "Jane Smith", "Stat": "Rebounds", "Line": 8.0}
    ])
