import pandas as pd



data = {"student": ["Anayo", "Brandon", "Claudia", "Dave", "Evelyn","Finn", "Gloria", "Hank", "Isla", "Julia" ],
        "test_one": [84, 90, 50, 29, 49, 44, 30, 98, 31, 66],
        "test_two": [68, 78, 28, 80, 45, 56, 53, 93, 31, 66],
        "test_three": [42, 35, 30, 40, 28, 85, 80, 99, 38, 48]
    }

# format data into a DataFrame
e = pd.DataFrame(data)

print(e.head(3))
print(e.tail(5))
print(e.iloc[1:8])
