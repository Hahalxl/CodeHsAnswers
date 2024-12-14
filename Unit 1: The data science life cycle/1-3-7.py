"""
Click on the Assignment tab to see the instructions. -->
"""

countries = ["Australia", "Egypt", "Greece", "India", "Jamaica", "Mexico",
"Spain", "United States"]
sugar_1980 = [152, 71.8, 73.5 ,52.2, 153, 124, 83.7, 158]
sugar_1990 = [137, 86.6, 87.3, 56, 142, 141, 76.1, 173]
sugar_2000 = [123, 82.1, 90.4, 63.7, 161, 132, 81, 189]
sugar_2010 = [126, 81.2, 77.3, 59.9, 137, 136, 83.2, 167]

"""
Add the sugar consumed in 1980 and 1990 lists. Print the result. 
What happens?
"""

print()
print(sugar_1980 + sugar_1990)

# Your Turn: Add the countries and the sugar_2010 list. Print the result.
# What happens here?

for i in range(len(countries)):
    print("\n" + countries[i] + ": " +str(sugar_2010[i]))



"""
Add an element from the sugar_1990 list to an element 
from the sugar_2000 list. 
Print the result.
"""

print()
print("First element in sugar_1990 + first element in sugar_2000 = " 
+ str(sugar_1990[0] + sugar_2000[0]))

# Your Turn: Add the first two elements of the countries list. 
# Print the result. What happens here?
print(countries[0] + countries[1])



"""
Decide whether the following expressions are true or false. 
Add the print function to the expressions to check your answers.
"""

print(True)
print(sugar_1990[0] > sugar_1980[1])  # prints True

# Take a guess and then add the print function to check
# Guess:
print(sugar_2010[0] == sugar_2000[1] )

# Take a guess and then add the print function to check
# Guess:
print(sugar_1980[3] < sugar_1990[5]  )

# Your Turn: Create and print another true expression and another false
# expression using the elements in the lists.

for i in range(len(sugar_2000) - 1):
    print(sugar_2000[i] > sugar_2000[i+1])

"""
Decide whether the following Boolean statements are true or false.
Add the print function to the statements to check your answers.
"""

print()

# Take a guess and then add the print function to check
# Guess:
print(sugar_1980[3] < sugar_1990[4] or sugar_1980[3] == sugar_2010[5])

# Take a guess and then add the print function to check
# Guess:
print(sugar_2000[2] < sugar_2010[5] and sugar_1990[0] < sugar_2010[1])

# Your Turn: Create and print a true Boolean statement that uses 'or' 
# and a false Boolean statement that uses 'and'
