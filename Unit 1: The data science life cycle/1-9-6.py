import pandas as pd


# test data
data = {"student": ["Anayo", "Brandon", "Claudia", "Dave", "Evelyn","Finn", "Gloria", "Hank", "Isla", "Julia" ],
        "test_one": [84, 90, 50, 29, 49, 44, 30, 98, 31, 66],
        "test_two": [68, 78, 28, 80, 45, 56, 53, 93, 31, 66],
        "test_three": [42, 35, 30, 40, 28, 85, 80, 99, 38, 48]
    }

# format data into a DataFrame
test_data = pd.DataFrame(data)

# create a function that finds the maximum value between 
# two columns for a single row
def max_two(c):
    print(c)
    a = test_data["test_one"].max()
    b = test_data["test_two"].max()
    return a if a > b else b
    
# use the function to create a new column that lists the max
# value between test one and test two

test_data["combine"] = test_data.apply(max_two, axis=1)
test_data["combine2"] = test_data.apply(max_two, axis=1)


# use the function to create a new column that lists the max
# value between all three tests
def max_three(row):
    a = []
    a.append(test_data["test_one"].max())
    a.append(test_data["test_two"].max())
    a.append(test_data["test_three"].max())
    return max(a)


print(test_data)
# Decide which calculations, along with these two new columns, 
# can help you answer the original statistical question.



# Conclusion: What do your calculations tell you? Can you answer
# the original question? Print a conclusion statement here.
