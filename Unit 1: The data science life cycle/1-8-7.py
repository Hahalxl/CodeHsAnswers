import pandas as pd
#a.csv is the same csv used in 1-7-5.py, 1-7-7.py, 1-7-8.py
data = pd.read_csv("a.csv", sep=" ")
e = pd.DataFrame(data)
d = e[(e["Test-One"] < 50)]
print(d)
f = e[(e["Test-Two"] > 50)]
print(f)
h = e[(e["Test-Two"] > 50 & e["Test-Three"] < 50 & e["Test-Three"] < 50)]
print(h)

e.reset_index(inplace=True)

e.set_index("Student", inplace=True)
