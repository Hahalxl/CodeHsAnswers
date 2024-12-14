import pandas as pd

n = pd.Series([72, 41, 62, 37, 47], index = ["Joey Chestnut", "Miki Sudo", "Matthew Stonie", "Sonya Thomas", "Matthew P"])

print(n.var())
print(n.std())
max1 = n.max()
min1 = n.min()
print(max1-min1)
print(n.quantile(0.25))
print(n.quantile(0.75))
print(n.quantile(0.50))
