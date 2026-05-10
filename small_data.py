import pandas as pd

# original csv load
df = pd.read_csv("india_housing_prices.csv")

# first 5000 rows
small_df = df.head(5000)

# save new small csv
small_df.to_csv("small_housing.csv", index=False)

print("Small CSV Created Successfully")