def optimize_lineups(df, platform):
    df = df.sort_values("Proj_Med", ascending=False)
    lineups = []
    for i in range(3):
        lineups.append([{
            "Player": df.iloc[i]["Player"],
            "Salary": df.iloc[i]["Salary"],
            "Team": df.iloc[i]["Team"],
            "Proj": f"{df.iloc[i]['Proj_Med']:.1f}/{df.iloc[i]['Proj_Floor']:.1f}/{df.iloc[i]['Proj_Ceil']:.1f}",
            "Value": round(df.iloc[i]["Value"], 3)
        }])
    return lineups
