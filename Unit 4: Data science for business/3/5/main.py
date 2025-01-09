import pandas as pd

df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)

# Group results by gender 
# What insights does this grouping give you?
print("Grouped by Gender")
print(df.groupby("gender")["gender"].count())
print("------------------------")


# Group results by industry 
# What insights does this grouping give you?
print()
print()
print("Grouped by Industry")
print(df.groupby("industry")['industry'].count())
print("------------------------")


# Sort by age (increasing)
print()
print()
print("Age (Ascending)")
print(df.groupby("age")["age"].agg([sorted]))
print("------------------------")


# Sort by net_worth (decreasing)
print()
print()
print("Net Worth (Ascending = False)")
print(df.groupby("net_worth")["net_worth"].agg([sorted]).tail())
print("------------------------")


# Sort by age (descreasing) and then net_worth (decreasing)
print()
print()
print("Age and Net Worth (Ascending = False)")
print(df.groupby("age")["net_worth"].sort_values(by="net_worth", ascending=False))
print("------------------------")
