import pandas as pd

male = pd.read_csv (r"male_cats.csv")
female = pd.read_csv (r"female_cats.csv")
pd.set_option("display.max_columns", None)


# Compare columns from both datasets
print("Male Cats")
print(male.info())
print("-------------------")


print()
print()
print("Female Cats")
print(female.info())
print("-------------------")



# Rename columns to match across both datasets
male.rename(columns={"name":"Name", 'fur_color':"Furcolor"}, inplace=True)


# Again - compare columns from both datasets

print("Male Cats")
print(male.info())
print("-------------------")


print()
print()
print("Female Cats")
print(female.info())
print("-------------------")



# Concatenate the two datasets (add on as new rows)
print()
print()
print("All Cats")
print(pd.concat([male, female]))
print("-------------------")


# Check the information from the new concatenated dataset.
print()
print()
print("All Cats")
print(pd.concat([male, female]).info())
print("-------------------")

