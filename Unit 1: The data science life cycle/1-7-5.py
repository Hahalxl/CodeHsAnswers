import pandas as pd

data = pd.read_csv("b.csv", sep=" ")
e = pd.DataFrame(data)
print(e)
