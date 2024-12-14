import pandas as pd

df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)

print(df.loc[df.publisher == "Sigma"])
print(df.loc[df.price > 100])
print(df.iloc[0:100, 0])
print(df.iloc[100:200, 1])
