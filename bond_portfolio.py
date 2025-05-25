import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load and Inspect Datas
df = pd.read_excel("synthetic_bond_data.xlsx")
print("\n First 10 Rows of DataFrame:")
print(df.head(10))
print("\n Type of columns:")
print(df.dtypes)

# Data Analysis
conditions = [
    (df["Maturity_Years"] >= 0) & (df["Maturity_Years"] < 5),
    (df["Maturity_Years"] >= 5) & (df["Maturity_Years"] < 10),
    (df["Maturity_Years"] >= 10) & (df["Maturity_Years"] < 15),
    (df["Maturity_Years"] >= 15) & (df["Maturity_Years"] <= 20)
]

labels = ["0-5 years", "5-10 years", "10-15 years", "15-20 years"]

df["Maturity_Group"] = np.select(conditions, labels, default=None)

average_parameters = df.groupby("Maturity_Group")[["Coupon_Rate", "Yield", "Maturity_Years"]].mean()
average_parameters = average_parameters.loc[["0-5 years", "5-10 years", "10-15 years", "15-20 years"]]
print("\n Average Coupon Rate, Yield, and Maturity per Maturity Group:")
print(average_parameters)

highest_yield_bond = df.loc[df["Yield"].idxmax()]
print("\n Highest Yield in portfolio:")
print(highest_yield_bond)

highest_yield_per_group = df.loc[df.groupby("Maturity_Group")["Yield"].idxmax()]
print("\n Highest Yield per Maturity Group:")
print(highest_yield_per_group)

bonds_above_4 = (df["Coupon_Rate"] > 0.04).sum()
print("\n Total number of bonds with a coupon rate above 4%:")
print(bonds_above_4)

sorted_by_yield = df.sort_values(by="Yield", ascending=False)
print("\n Bond ranking by Yield:")
print(sorted_by_yield[["Bond_ID", "Yield"]])

# Data Visualization
plt.hist(df["Coupon_Rate"], bins=10, edgecolor="black")
plt.xlabel("Coupon Rate")
plt.ylabel("Number of Bonds")
plt.title("Distribution")
plt.show()

plt.scatter(df["Maturity_Years"], df["Yield"], alpha=0.5)
plt.xlabel("Maturity")
plt.ylabel("Yield")
plt.title("Yield versus Maturity")
plt.show()

# Results
summary = pd.DataFrame({
    "Parameter": [
        "Average Coupon Rate",
        "Average Yield",
        "Average Maturity",
        "Highest Yield Bond",
        "Longest Maturity Bond",
        "Coupon Rate above 4%"
    ],
    "Output": [
        df["Coupon_Rate"].mean(),
        df["Yield"].mean(),
        df["Maturity_Years"].mean(),
        highest_yield_bond["Bond_ID"],
        df.loc[df["Maturity_Years"].idxmax()]["Bond_ID"],
        bonds_above_4
    ]
})

with pd.ExcelWriter("bond_portfolio_summary.xlsx") as writer:
    summary.to_excel(writer, index=False, sheet_name="Summary")
    sorted_by_yield.to_excel(writer, index=False, sheet_name="Summary", startrow=len(summary) +  5)