import pandas as pd
from fuzzywuzzy import process, fuzz

df = pd.read_csv (r"data.csv")

# Uncomment the following command to fix the fuzzy matches
"""
df.author.replace(to_replace =["agatha Christie", "AgathaChristie", "Agath Christie", "Agathachristie", "Christie Agatha"], value = "Agatha Christie", inplace=True)
"""

# Create a Series of unique author names
new_table = df["author"].unique()

# Extract values that are close to matching 
matches = process.extract("Agatha Christie", new_table, limit=6)

# Print out each matching item
print()
for item in matches:
    print(item)
    
