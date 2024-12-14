import wikipedia 

t = wikipedia.summary("turtles",sentences=2)
s = wikipedia.search("tesla", 2)

print(t)
print(s)
