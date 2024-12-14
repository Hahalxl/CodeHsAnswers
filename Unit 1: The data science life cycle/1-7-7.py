import pandas as pd

#a.csv is the same csv file as the one used in 1-7-5.py
data = pd.read_csv("a.csv", sep=" ")
e = pd.DataFrame(data)
print(e.shape)
print(e.dtypes)
print(e.describe())
