import pandas as pd

#a.csv is the same csv used in 1-7-5.py, 1-7-7.py, 1-7-8.py
data = pd.read_csv("a.csv", sep=" ")
e = pd.DataFrame(data)

print(e["Test-One"].mean())
print(e["Test-Two"].max())
print(e["Test-Three"].min())
