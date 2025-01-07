# Click on the Assignment tab to see more info. -->
# <-- Click on the files to see the different datasets.
import pandas as pd

#First dataset
df = pd.read_csv("internet_users.csv")
print(df.isnull().mean().round(4) * 100)

#Second dataset
df = pd.read_csv("cereal.csv")
print("\n\n\n")
print(df.isnull().mean().round(4) * 100)
