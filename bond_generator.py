import pandas as pd
import numpy as np

# Generate Data
np.random.seed(10)
num_bonds = 500 

bond_data = {
    "Bond_ID": [f"Bond_{i+1}" for i in range(num_bonds)],
    "Coupon_Rate": np.random.uniform(0.02, 0.05, num_bonds),
    "Maturity_Years": np.random.randint(1, 21, num_bonds),
    "Yield": np.random.uniform(0.01, 0.06, num_bonds)
}
# Create and Save DataFrame
df = pd.DataFrame(bond_data)
df.to_excel("synthetic_bond_data.xlsx", index=False)
print(df)