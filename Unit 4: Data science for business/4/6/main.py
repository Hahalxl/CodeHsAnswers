import pandas as pd

df1 = pd.read_csv(r"customers1.csv")
df2 = pd.read_csv(r"customers2.csv")
pd.set_option("display.max_columns", None)

# Print both datasets for comparison
# Are there names that appear in both sets?
print("DF1")
print("----------")
print(df1)
print()
print()
print("DF2")
print("----------")
print(df2)

# Inner Join using the last_name as a primary key
# What was kept?
# Do you notice any duplicate columns? Why do think this happened?
print()
print()
print("Inner Join")
print("----------")
print(pd.merge(df1, df2, on="last_name", how="inner"))

# Outer Join using the first_name AND last_name as primary keys
# What was kept?
# What do the NaN values represent?
print()
print()
print("Outer Join")
print("----------")
print(pd.merge(df1, df2, on=["first_name","last_name"], how="outer"))

# Left Join using the first_name AND last_name as primary keys
# What was kept?
# What do the NaN values represent?
print()
print()
print("Left Join")
print("----------")
print(pd.merge(df1, df2, on=["first_name","last_name"], how="left"))

# Right Join using the first_name AND last_name as primary keys
# What was kept?
# What do the NaN values represent?
print()
print()
print("Right Join")
print("----------")
print(pd.merge(df1, df2, on=["first_name","last_name"], how="right"))

# Which join might make the most sense to use and why?
