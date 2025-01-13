import pandas as pd


first = pd.read_csv("first.csv")
second = pd.read_csv("second.csv")
combine = pd.merge(first, second, on="name", how="outer")

print(combine.info())
print(combine)
#1. Names
#2. The height and weight
