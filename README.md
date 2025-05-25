# Bond Portfolio Analysis

This project involves generating synthetic bond data and performing portfolio analysis using Python.

## Overview

- Synthetic bond data is generated in `bond_generator.py`, including:
  - Bond ID
  - Coupon Rate
  - Maturity in years
  - Yield (as a decimal)

- Portfolio analysis is performed in `bond_portfolio.py`, including:
  - Grouping bonds by maturity range
  - Calculating average coupon, yield, and maturity per group
  - Identifying bonds with the highest yield (overall and per group)
  - Counting bonds with coupon rate above 4%
  - Ranking bonds by yield
  - Creating relevant plots

- Results are saved to Excel for further review.

## Files

- `bond_generator.py` – generates the synthetic dataset
- `synthetic_bond_data.xlsx` – generated bond data
- `bond_portfolio.py` – performs analysis and visualization
- `bond_portfolio_summary.xlsx` – summary of results

