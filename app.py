import streamlit as st
from BBtLB_Optimizer import main as bbtlb_main
import pandas as pd

st.set_page_config(page_title="BBtLB Fantasy Lineup Generator", layout="wide")

st.title("🧠 Big Bank Take Little Bank (BBtLB)")
st.markdown("Generate fantasy lineups and props for DraftKings, FanDuel, PrizePicks, and Underdog.")

platform = st.selectbox("Choose Platform", ["DraftKings", "FanDuel", "PrizePicks", "Underdog"])
run_button = st.button("🚀 Run BBtLB Optimizer")

if run_button:
    st.info("Running projections and simulations...")
    try:
        output = bbtlb_main.run_full_pipeline(platform=platform)

        if platform in ["DraftKings", "FanDuel"]:
            for i, lineup in enumerate(output['lineups'], 1):
                st.subheader(f"{platform} Lineup #{i}")
                st.dataframe(pd.DataFrame(lineup))

        elif platform in ["PrizePicks", "Underdog"]:
            st.subheader(f"{platform} Top Props")
            st.dataframe(pd.DataFrame(output['props']))

    except Exception as e:
        st.error(f"Error running BBtLB optimizer: {e}")
