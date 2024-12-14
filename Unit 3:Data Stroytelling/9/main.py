import pandas as pd 
import matplotlib.pyplot as mp
import numpy as np

#Dataset
df = pd.read_csv("data.csv")
pd.set_option("display.max_columns", None)
df.drop("quarter", inplace=True, axis=1)

#C plus plus dataset
cpp = df.loc[df["name"] == "C++", :]
cpp.drop_duplicates(subset=['year'], keep="last", inplace=True)
#X
x = cpp.year
#Y
y = cpp['count']
corr = y.corr(x)
print("Correlation:", corr)

mp.title("C++ repos count on Github over the years")
mp.xlabel("Years")
mp.ylabel("Repos")
mp.scatter(x, y)

model = np.polyfit(x, y, 1)
m = str(round(model[0], 2))
b = str(round(model[1], 2))

print("Model: y = " + m +"x + " + b)

predict = np.poly1d(model)

try:
    pre = int(input("You: "))
except ValueError:
    pre = 0

predicted = round(predict(pre), 2)

print(predicted)
mp.show()
