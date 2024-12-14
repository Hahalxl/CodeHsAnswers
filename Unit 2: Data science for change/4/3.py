# Click on the Assignment tab to see the instructions. -->
# <-- Click on the data.csv file to see the dataset.

import pandas as pd

# import the data from the data.csv file
df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)


# print the rows where followers are greater than 230 (million)
print(df.loc[df.followers > 230])

# print only the account columns of those from the United States
print(df.loc[(df.country == "United States"), ["account"]])


# print the account and followers columns of the row with the maximum number of followers
print(df.loc[df.followers.max()])
