# BBtLB Fantasy Optimizer

This project implements the "Big Bank Take Little Bank" (BBtLB) methodology to optimize fantasy sports lineups and props for DraftKings, FanDuel, Underdog, and PrizePicks.

## Features

- Real-time data ingestion
- Blended player projection engine
- Monte Carlo simulations
- Injury-aware adjustments ("Knick Factor")
- Correlation and stacking logic
- Ownership leverage analysis

## Supported Platforms

- DraftKings (GPP + Cash)
- FanDuel (GPP + Cash)
- Underdog Fantasy (Pick'em)
- PrizePicks (Over/Under props)

## Usage

To run the optimizer for a given date:
```bash
python main.py --date YYYY-MM-DD
```
