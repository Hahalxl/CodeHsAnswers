"""
Click on the Assignment tab to see the instructions. -->
<-- Click on the data.csv file to see the dataset.

Create a list for the height_in_inches column that consists of all 
of the values in that column.
"""

heights:int = [71, 69, 70, 71, 68, 70, 70]
name:str = ["Jin", "Suga", "J-Hope", "RM", "Jimin", "JungKook"]
weight:int = [136, 138, 132, 145, 143, 137, 145]
net_worth:int = [8, 8, 12, 12, 8, 8, 8, 8]

# Your Turn: Create a list for the name, weight, and 
# net_worth columns.





"""
Print the data type of the elements in the height list. 
What data type is it?
"""

print("Name is stored as " + str(type(name))
print("weight is stored as " + str(type(weight))
print("networth is stored as " + str(type(net_worth))
print("Height elements are stored as " + str(type(heights[0])))

# Your Turn: Print the data types of the elements in the other lists. 




# Your Turn: Print the data type of one of the lists. 
# What data type is it?




"""
Print the length of the heights list, the max value, the min value 
and the sum of the heights list.
"""

print()
print("The length of the heights list is " + str(len(heights)))
print("The minimum height is " + str(min(heights)))
print("The maximum height is " + str(max(heights)))
print("The sum of all heights is " + str(sum(heights)))

# Your Turn: Print the length, the max value, the min value and the 
# sum of the other lists. Note: The sum function will not work on a string.
# How do you suppose the min and max work with strings based on what
# is printed?
