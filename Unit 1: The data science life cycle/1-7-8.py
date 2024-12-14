import pandas as pd

#a.csv is the same one as used in 1-7-5.py and also 1-7-7.py
data = pd.read_csv("a.csv", sep=" ")
e = pd.DataFrame(data)

print(e.head(3))
print(e.tail(5))
print(e.iloc[1:8])
