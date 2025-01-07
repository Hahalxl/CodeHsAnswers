# Click on the Example tab to see more info. -->
# <-- Click on the data.csv file to see the dataset.

import pandas as pd

google_books_df = pd.read_csv (r"google_books.csv")
pd.set_option("display.max_columns", None)

print("Number of null values for each column:")
print("----------------------------------------")
print(google_books_df.isnull().sum())

print()
print("Mean (Average) of null values in each column:")
print("----------------------------------------")
print(google_books_df.isnull().mean())

print()
print("Percentage of null values in each column:")
print("----------------------------------------")
print(google_books_df.isnull().mean().round(4) * 100)

print()
print("Mean (Average) of null values in the WHOLE dataset:")
print("----------------------------------------")
print(google_books_df.isnull().mean().mean())

print()
print("Percentage of null values in the WHOLE dataset:")
print("----------------------------------------")
print(google_books_df.isnull().mean().mean().round(4) * 100)

print()
print("Number of duplicated rows in the datset:")
print("----------------------------------------")
print(google_books_df.duplicated().sum())

# Drops the duplicated rows
google_books_df.drop_duplicates(inplace=True)

print()
print("Number of duplicated rows after dropping:")
print("----------------------------------------")
print(google_books_df.duplicated().sum())
