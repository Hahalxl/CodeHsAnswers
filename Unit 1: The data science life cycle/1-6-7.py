import pandas as pd
import matplotlib.pyplot as plt




n = pd.Series([72, 41, 62, 37, 47], index = ["Joey Chestnut", "Miki Sudo", "Matthew Stonie", "Sonya Thomas", "Matthew P"])

# Plot a box plot
plt.boxplot(n)
plt.show()
