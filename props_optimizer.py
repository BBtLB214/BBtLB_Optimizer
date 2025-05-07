def optimize_props(props_df, projections_df, platform):
    merged = props_df.merge(projections_df, on="Player", how="left")
    merged["Edge"] = merged["Proj_Med"] - merged["Line"]
    top_props = merged.sort_values("Edge", ascending=False).head(5)

    result = []
    for _, row in top_props.iterrows():
        result.append({
            "Player": row["Player"],
            "Stat": row["Stat"],
            "Line": row["Line"],
            "BBtLB Proj": round(row["Proj_Med"], 1),
            "Edge %": f"{round(row['Edge'] / row['Line'] * 100, 1)}%",
            "Justification": "Projection > Line by model edge"
        })
    return result
