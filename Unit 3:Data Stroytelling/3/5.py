import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)

# Set the index to the name of the state
# This will make filtering by state easier
df.set_index("state", inplace=True)

# Create a new filtered table
filtered_table = df.loc[["Colorado", "Illinois", "New York", "California","Delaware" ]]
#
# Plot the pie chart using the filtered table, and organizing it by the total population
filtered_table.plot.pie(y="Total_Pop", autopct="%.2f%%")

# Move the legend to the best location
plt.legend(loc="upper left")

plt.show()
