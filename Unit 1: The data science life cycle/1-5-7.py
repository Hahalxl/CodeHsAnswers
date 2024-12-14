import pandas as pd

# Create and print the series
people_named_anna = pd.Series([7288, 7118, 6846, 6808, 7523, 8564,
    8565, 8337, 8378, 9098, 10588, 10588,
    10385, 9443, 9514, 9101, 8601, 7888,
    7265, 6800, 6326, 5658, 5615, 5378,
    5679, 5125, 4775, 4520], index=["1990", "1991", "1992", "1993", "1994", "1995",
    "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005",
    "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015",
    "2016", "2017"])

print("People Named Anna")
print("--------------------")
print(people_named_anna)

# Search for an item in the series
print()
print('Is "2002" in the people_named_anna series?') 
print("2002" in people_named_anna)
print()
print("Is 2002 in the people_named_anna series?") 
print(2002 in people_named_anna) 
print()
print('Is "1983" in the people_named_anna series?') 
print("1983" in people_named_anna) 

# Print summary statistics

print()
print("Mean:") 
print(people_named_anna.mean())
print()
print("Median:")
print(people_named_anna.median())
print()
print("Mode:")
print(people_named_anna.mode())
print()
print("Summary Statistics:")
print(str(people_named_anna.describe()))
