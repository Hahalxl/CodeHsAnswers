import pandas as pd

#Dataset is provided
coasters = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)

# create a function that uses the ranking algorithm
def ranks(row):
    return (4 * row["Speed"]) + (3 * row["Length"]) + (5 * row["Drop"]) + (4 * row["Duration"])

# use the function to create a new column with the calculations      
coasters['Score'] = coasters.apply(ranks, axis=1)


# filter the table to display the name of the roller coaster and the 
# ranking   


# find the max value of the ranking column
print(coasters['Score'].max())

# filter for the row that corresponds with the max value


# print the answer!
