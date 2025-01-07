import pandas as pd
from fuzzywuzzy import process, fuzz

df = pd.read_csv (r"data.csv")

# Create a Series of unique author names
new_table = df["author"].unique()

# Extract values that are close to matching 
matches = process.extract("Agatha Christie", new_table, limit=6)

# Print out each matching item
print()
for item in matches:
    print(item)
