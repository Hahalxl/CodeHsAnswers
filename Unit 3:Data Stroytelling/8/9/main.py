import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import the data
df = pd.read_csv (r"swim_times.csv")

#X and Y
x = df.year
y = df.seconds

corr = y.corr(x)
print("Correlation:", corr)

plt.title("Year and the swim time (s)")
plt.xlabel("Years")
plt.ylabel("Time (seconds)")

plt.scatter(x, y)
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

x_lin_reg = range(df.year.min(), df.year.max()) # range is based on the min and max values
y_lin_reg = predict(x_lin_reg)
plt.plot(x_lin_reg, y_lin_reg, color = "red")
  

plt.show()
