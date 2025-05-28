import pandas as pd

def test_generated_bond_data():
    df = pd.read_excel("synthetic_bond_data.xlsx")
    
    # Check number of bonds
    assert len(df) == 500, "Number of rows should be 500"

    # Check columns exist
    expected_cols = {"Bond_ID", "Coupon_Rate", "Maturity_Years", "Yield"}
    assert expected_cols.issubset(df.columns), "Missing expected columns"

    # Check ranges
    assert df["Coupon_Rate"].between(0.02, 0.05).all(), "Coupon_Rate out of range"
    assert df["Maturity_Years"].between(1, 20).all(), "Maturity_Years out of range"
    assert df["Yield"].between(0.01, 0.06).all(), "Yield out of range"
