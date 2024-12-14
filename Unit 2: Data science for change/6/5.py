import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)
df.drop(["rating", "voters"], axis=1, inplace=True)
df.dropna(axis=1)
print(df.dtypes)

print(df.loc[:, ["title", "price", "author"]])
print("The average price of a book: ")
print(round(df.price.sum()/ len(df.price), 2))



plt.show()
