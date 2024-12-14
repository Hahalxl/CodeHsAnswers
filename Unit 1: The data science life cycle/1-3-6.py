"""
Click on the Assignment tab to see the instructions. -->
<-- Click on the data.csv file to see the dataset.
"""


            

# Create a list for the columns of your dataset.

heights:int = [71, 69, 70, 71, 68, 70, 70]
name:str = ["Jin", "Suga", "J-Hope", "RM", "Jimin", "JungKook"]
weight:int = [136, 138, 132, 145, 143, 137, 145]
net_worth:int = [8, 8, 12, 12, 8, 8, 8, 8]


# Print the data types of the elements in the lists. 

print("Name is stored as " + str(type(name)))
print("weight is stored as " + str(type(weight)))
print("networth is stored as " + str(type(net_worth)))
print("Height elements are stored as " + str(type(heights[0])))





# Print the length, the max value, the min value and the 
# sum of the other lists. Note: The sum function will not 
# work on a string.
print()
print("The length of the heights list is " + str(len(heights)))
print("The minimum height is " + str(min(heights)))
print("The maximum height is " + str(max(heights)))
print("The sum of all heights is " + str(sum(heights)))
