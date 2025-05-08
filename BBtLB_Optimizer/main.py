# BBtLB_Optimizer/main.py

import argparse
from BBtLB_Optimizer import (
    prop_picker,
    ownership_leverage,
    dk_fd_builder,
    projection_engine
)
import pandas as pd


def run_prop_picker():
    print("[INFO] Running Prop Picker...")
    sim_df = prop_picker.run_monte_carlo()
    picks = prop_picker.pick_props(sim_df)
    for p in picks:
        print(p)


def run_ownership_leverage():
    print("[INFO] Running Ownership Leverage...")
    ownership_leverage.main()


def run_lineup_builder():
    print("[INFO] Running DK/FD Lineup Builder...")
    # Add CLI-level stub if dk_fd_builder exposes main() or similar
    # Example placeholder
    print("[WARN] Lineup builder not fully integrated.")


def run_projection_engine():
    print("[INFO] Running Projection Engine...")
    projections = projection_engine.generate_projections()
    print(pd.DataFrame(projections).head())


def main():
    parser = argparse.ArgumentParser(description="Run BBtLB Optimizer modules")
    parser.add_argument("--module", choices=["prop", "ownership", "lineup", "projection"],
                        required=True, help="Module to run")
    args = parser.parse_args()

    if args.module == "prop":
        run_prop_picker()
    elif args.module == "ownership":
        run_ownership_leverage()
    elif args.module == "lineup":
        run_lineup_builder()
    elif args.module == "projection":
        run_projection_engine()


if __name__ == "__main__":
    main()
