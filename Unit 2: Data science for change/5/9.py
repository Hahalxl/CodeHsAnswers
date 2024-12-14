import pandas as pd

df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)

print(df.dtypes)
df.drop(["price", "published_date"], axis=1, inplace=True)
df.drop_duplicates(inplace=True)
print(df.isnull().sum())
df.fillna(method="bfill")
