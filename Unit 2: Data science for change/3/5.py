# Click on the Assignment tab to see the instructions. -->
# <-- Click on the data.csv file to see the dataset.

import pandas as pd

# import the data from the data.csv file
df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)


# Using loc - Print the row and animal columns for rows 3 to 6
print(df.loc[2:5, ["row", "animal"]])


# Using iloc - Print the row and animal columns for rows 3 to 6
print(df.iloc[2:6, [0, 1]])



# Using loc - Print the sound of the animal at index 7
print(df.loc[7, "sound"])



# Using iloc - Print the sound of the animal at index 7
print(df.iloc[7, 2])

# Using loc - Print rows at index 8-10 
print(df.loc[8:10])

print("What the sigma\n\n\n\n\n")
# Using iloc - Print rows at index 8-10
print(df.iloc[8:11])
