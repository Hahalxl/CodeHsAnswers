import pandas as pd

df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)
df.drop_duplicates(inplace=True)

# Sorts page_count values (increasing)
print("Page Counts (Ascending)")
print("------------------------")
print(df[["title", "page_count"]].sort_values(by="page_count").head())

# Sorts page_count values (decreasing)
print()
print()
print("Page Counts (Ascending = False)")
print("------------------------")
print(df[["title", "page_count"]].sort_values(by="page_count", ascending=False).head())

# Sorts by the rating (decreasing) and then by the author (alphabetically)
print()
print()
print("Highest Rated Authors (Alphabeticaly)")
print("------------------------")
print()
print(df[["author", "rating"]].sort_values(by=["rating", "author"], ascending=[False, True]).head())

