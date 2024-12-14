import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"plastics.csv")

x = df.Year
y = df["Global plastics production (million tonnes)"]

plt.xlabel("Year")
plt.ylabel("Plastic production (million ton)")
plt.title("Plastic production over years")

plt.bar(x, y, color="#000000")
plt.show()
