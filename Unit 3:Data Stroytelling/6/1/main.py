import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("data.csv")
pd.set_option("display.max_columns", None)
df.drop("quarter", inplace=True, axis=1)
#C plus plus dataset
cpp = df.loc[df.name == "C++", :]
cpp.drop_duplicates(subset=['year'], keep="last", inplace=True)
cpp.drop("name", inplace=True, axis=1)
plt.pie(x=cpp['count'], labels=cpp['year'], autopct="%2.f%%")
plt.show()
