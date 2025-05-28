import unittest
import pandas as pd
import numpy as np

# Load the Excel file
df = pd.read_excel("synthetic_bond_data.xlsx")

class TestBondPortfolio(unittest.TestCase):

    def test_dataframe_not_empty(self):
        # Check if the DataFrame is not empty
        self.assertFalse(df.empty, "The DataFrame is empty.")

    def test_columns_exist(self):
        # Verify that all required columns are present
        required_columns = {"Bond_ID", "Coupon_Rate", "Maturity_Years", "Yield"}
        self.assertTrue(required_columns.issubset(df.columns), "Some required columns are missing.")

    def test_coupon_rate_range(self):
        # Check if all coupon rates are within the expected range
        self.assertTrue(((df["Coupon_Rate"] >= 0.02) & (df["Coupon_Rate"] <= 0.05)).all(), "Coupon Rate out of range.")

    def test_yield_range(self):
        # Check if all yields are within the expected range
        self.assertTrue(((df["Yield"] >= 0.01) & (df["Yield"] <= 0.06)).all(), "Yield out of range.")

    def test_maturity_range(self):
        # Check if all maturity values are between 1 and 20
        self.assertTrue(((df["Maturity_Years"] >= 1) & (df["Maturity_Years"] <= 20)).all(), "Maturity out of range.")

if __name__ == '__main__':
    unittest.main()