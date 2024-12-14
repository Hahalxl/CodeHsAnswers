# Click on the Assignment tab to see the instructions. -->
# <-- Click on the data.csv file to see the dataset.

import pandas as pd

# import the data from the data.csv file
df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)

# Using loc - Print the title and page count columns 
# for rows 3 to 6
print(df.loc[2:5, ["title", "page_count"]])

# Using iloc - Print the title and page count columns 
# for rows 3 to 6
print(df.iloc[2:6, [0, 6]])

# Using loc - Print the title of the book at index 400
print(df.loc[400, "title"])


# Using iloc - Print the title of the book at index 400
print(df.iloc[400, 0])

# Using loc - Print rows at index 10-15 and columns at index 3-5
print(df.loc[10:15, "voters":"publisher"])


# Using iloc - Print rows at index 10-15 and columns at index 3-5
print("\n\n\n\n\n\n\n\n")
print(df.iloc[10:16, 3:6])
