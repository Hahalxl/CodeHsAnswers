import pandas as pd
import matplotlib.pyplot as plt

student_pets = pd.Series(["Dog", "Cat", "Dog", "Cat", "Fish", "Fish", "Ferret", "Hamster", "Dog", "Cat", "Fish", "Hamster", "Dog", "Dog", "Dog"])

plt.title("Student Pets", fontsize=22)
plt.xlabel("Type of Pet")
plt.ylabel("Number of Pets")
plt.ylim([0, 7])

plt.hist(student_pets, edgecolor="black", bins=[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5])
plt.show()
