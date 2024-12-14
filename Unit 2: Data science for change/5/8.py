# Click on the Assignment tab to see the instructions. -->
# <-- Click on the data.csv file to see the dataset.

import pandas as pd

# import the data from the data.csv file
# set max_columns to None
df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)


# Check the data types. Do they look okay?
print(df.dtypes)


# Drop the publisher and published_date columns.
df = df.drop(["publisher","published_date"], axis=1)
print(df)

# Print the shape of the data and check for duplicate rows. 
print(df.shape)
# How many are there?
print(df.duplicated().sum())


# Drop duplicate rows. 
print(df.drop_duplicates(inplace=True))

# Determine the number of missing values.
print(df.isnull().sum())


# What would be the best decision for dealing with
# the missing values? Make the call and change
