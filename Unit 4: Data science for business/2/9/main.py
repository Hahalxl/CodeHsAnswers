import pandas as pd
from fuzzywuzzy import process, fuzz

df = pd.read_csv (r"data.csv")

# Create a Series of unique title names
titles = df["title"].unique()

# Extract values that are close to matching 
matches = process.extract("batman", titles)

# Print out each matching item
print()
for item in matches:
    print(item)
