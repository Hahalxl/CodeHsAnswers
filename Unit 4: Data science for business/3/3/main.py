import pandas as pd

df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)
df.drop_duplicates(inplace=True)

# Displays the count for the first 10 publishers
print("Count")
print("------------------------")
print(df.groupby("publisher").publisher.count().head(10))

# Displays the maximum price and rating for the first 10 publishers
print()
print()
print("Maximum")
print("------------------------")
print(df.groupby("publisher")[["price", "rating"]].max().head(10))

# Displays the min, max and sum of the values in the price column for the first 10 publishers
print()
print()
print("Aggregate (Min, Max, Sum)")
print("------------------------")
print(df.groupby("publisher").price.agg([min, max, sum]).head(10))

# Displays the sorted list of values in the price column for the last 3 publishers
print()
print()
print("Sorted List")
print("------------------------")
print(df.groupby("publisher").price.agg([sorted]).tail(4))
