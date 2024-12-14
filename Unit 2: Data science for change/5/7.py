# Click on the Assignment tab to see more info. -->
# <-- Click on the data.csv file to see the dataset.

import pandas as pd

# import the data from the data.csv file
# set max_columns to None
df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)
print(df.isnull().sum())


# Check the data types. Do they look okay?
print(df.dtypes)
print(df.drop(["row_number","animal","sound"], axis=1, inplace=True))

# Drop the column labeled row_number.
print(df.loc[:, "row_number"])
df = df.fillna(method='ffill', axis=1)
print(df.shape)

# Print the shape of the data and check for duplicate rows. 
# How many are there?
print(df.duplicated().sum())

# Drop duplicate rows. 
print(df.drop_duplicates(inplace=True))

# Determine the number of missing values.


# What would be the best decision for dealing with the missing values? Make the call and change the data.
