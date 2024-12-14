import pandas as pd
import numpy as np
import os

df = pd.read_csv (r"issues.csv")
pd.set_option("display.max_columns", None)
print(df.dtypes)

print(df.drop_duplicates(inplace=True))
df.drop(["quarter"], axis=1, inplace=True)
print(df.loc[df.year == 2011, :])
input("Type anything to continue")
os.system("clear")
print(df.loc[df.name == "Python", :])
