# Click on the Assignment tab to see the instructions. -->
# <-- Click on the data.csv file to see the dataset.

import pandas as pd

# import the data from the data.csv file
# set max_columns to None
df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)

# print title and page count for books that have less 
# than 100 pages
print(df.loc[df.page_count < 100, ["title", "page_count"]])


# print only the rows that have the publisher "IDW Publishing"
print(df.loc[df.publisher == "IDW Publishing"])

# print the title, rating and voters columns for books 
# that have a rating of 4.0 or higher and over 9000 voters
print(df.loc[(df.rating >= 4.0) & (df.voters > 9000), ["title", "rating", "voters"]])

# print only the row(s) with the max price
print(df.price.max)
