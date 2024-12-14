import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#I couldn't find a dataset in the Spurious Correlations. So, I went on the internet and found this data.
#I will turn this data in something LIKE the 2 csv files
df = pd.read_csv("data.csv")

#x
person = df.Name.head(10)
#y1
wealth = df["Net Worth"].head(10).str.replace("B", "", regex=False).str.replace("$", "", regex=False)
wealth = wealth.str.replace(",", "", regex=False).astype(float) 
#y2
age = pd.to_numeric(df["Age"].head(10), errors="coerce")

correlation = wealth.corr(age)
print(correlation) 

plt.title("Billionaries: wealth vs age")
plt.xlabel("Billionarie")
plt.ylabel("Wealth/Age")

plt.scatter(person, wealth)
plt.scatter(person, age)
plt.show()
