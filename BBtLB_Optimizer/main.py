#!/usr/bin/env python3

# Direct import assuming PYTHONPATH is set to the parent of BBtLB_Optimizer
from BBtLB_Optimizer import prop_picker, ownership_leverage, dk_fd_builder

def main():
    print("🚀 Starting BBtLB Optimizer...\n")

    # Run prop picking logic
    print("🔍 Running prop picker...")
    prop_picker.run()

    # Run ownership leverage logic
    print("📊 Calculating ownership leverage...")
    ownership_leverage.calculate()

    # Build the DraftKings FD data
    print("🏗️ Building DK/FD lineups...")
    dk_fd_builder.build()

    print("\n✅ Optimization pipeline completed.")

if __name__ == "__main__":
    main()
