import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

"""Plot the data"""

# Import the data
df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)

# Set data to be the values in the verbal_scores column
data = df.verbal_scores

# Add labels to the graph
plt.title("Verbal score")
plt.xlabel("Student")
plt.ylabel("Score")

# Plot the histogram (w/density)
plt.hist(data, bins=10, density=True)

"""Plot the Normal Distribution Curve"""

# Determine the mean, median and std
mean = data.mean()
median = data.median()
std = data.std()

# Set up min and max of the x-axis using the mean and standard deviation
xmin = mean - 3 * std
xmax = mean + 3 * std

# Define the x-axis values
x = np.linspace(xmin, xmax) 

# "Norm" the y-axis values based on the x-axis values, the mean and the std
y = norm.pdf(x, mean, std)

# Plot the graph using the x and the y values
plt.plot(x, y, color="orange", linewidth=2) 

plt.show()
