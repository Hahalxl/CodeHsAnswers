import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"ohio.csv")
df2 = pd.read_csv(r"new_york.csv")
df3 = pd.read_csv(r"georgia.csv")
pd.set_option("display.max_columns", None)

df.drop("STATION", axis=1, inplace=True)
df2.drop("STATION", axis=1, inplace=True)
df3.drop("STATION", axis=1, inplace=True)

x = df.DATE

y = df.MLY_PRCP_NORMAL
y2 = df2.MLY_PRCP_NORMAL
y3 = df3.MLY_PRCP_NORMAL

plt.plot(x, y, linewidth = 1.0,  linestyle = "dashed", color="#FF0000", marker="o")
plt.plot(x, y2, color="green", marker="o")
plt.plot(x, y3, color="#000000", marker="o")


plt.xlabel("Month")
plt.ylabel("Precipitation (in)")
plt.title("Precipitation over month")
# Add a legend
plt.legend(["Ohio", "New York", 'Georgia'], loc="upper left")

plt.show()
