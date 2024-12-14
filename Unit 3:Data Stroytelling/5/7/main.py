import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

"""Plot the Histogram"""

# Import dataset for the histogram
df = pd.read_csv (r"data.csv")
pd.set_option("display.max_columns", None)

# Filtered Tables
female = df.loc[(df['rank'] == "Prof") & (df['sex'] == "Female"), :]
years = df.loc[(df['rank'] == "Prof") & (df['years_of_service'] > 10)]




# Set data equal to one column of a dataset
data = df.salary

# Add labels and a title
plt.grid(True)
plt.xlabel("Yearly Salary")
plt.ylabel("Distribution")
plt.title("Professor Salaries", fontsize=22)

# Plot histogram using the data, 15 bins and show the density
plt.hist(data, bins=15, density=True)

"""Plot the Normal Distribution Curve"""

# Determine the mean, median and std
mean = data.mean()
median = data.median()
std = data.std()

# Print the mean, median and standard deviation of the data
print(mean)
print(median)
print(std)


# Set up min and max of the x-axis using the mean and standard deviation
xmin = mean - 3 * std
xmax = mean + 3 * std

# Define the x-axis values
x = np.linspace(xmin, xmax)

# "Norm" the y-axis values based on the x values
y = norm.pdf(x, mean, std)

# Plot the graph using the x and the y values
plt.plot(x, y, linewidth=2)

"""Determine Likelihoods"""

x_value = 100000

# Calculate the likelihood according to the normal distribution

pdf = norm.pdf(x_value, mean, std) 
print()
print("The likelihood of earning a salary of " + str(x_value) + " is " + str(pdf * 100))

cdf = norm.cdf(x_value, mean, std) 
print()
print("The likelihood of earning a salary less than " + str(x_value) + " is " + str(cdf * 100))

more_than_cdf = 1 - norm.cdf(x_value, mean, std) 
print()
print("The likelihood of earning a salary more than " + str(x_value) + " is " + str(more_than_cdf * 100))
print((more_than_cdf + cdf))
plt.show()
