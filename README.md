# Bond Portfolio Analysis

![Tests](https://github.com/mglancu/bond_portfolio_analysis/actions/workflows/python-app.yml/badge.svg)

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

- Basic testing is implemented in `bond_generator_test.py` to verify dataset generation,  
  and in `bond_portfolio_test.py` to validate portfolio analysis logic.

- Continuous Integration is enabled via **GitHub Actions** to automatically run tests on each push or pull request.

## Files

- `bond_generator.py` – generates the synthetic dataset
- `bond_generator_test.py` – basic tests for dataset generation
- `synthetic_bond_data.xlsx` – generated bond data
- `bond_portfolio.py` – performs analysis and visualization
- `bond_portfolio_test.py` – basic tests for portfolio analysis
- `bond_portfolio_summary.xlsx` – summary of results

## How to Run Tests

```bash
pytest bond_generator_test.py
pytest bond_portfolio_test.py
