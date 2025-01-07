import pandas as pd
from fuzzywuzzy import process, fuzz

df = pd.read_csv (r"data.csv")

# Create a Series of unique title names
df.title.replace(to_replace =["Batman and Robin Vol. 1: Batman Reborn"], value = "Batman and Robin Vol. One: Batman Reborn", inplace=True)
titles = df["title"].unique()
# Extract values that are close to matching 
matches = process.extract("batman", titles)

# Print out each matching item
print("Titles : \n\n\n"  )
for item in matches:
    print(item)
    
