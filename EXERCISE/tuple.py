# Create a tuple
a=str(input("Pls insert a name of furit:"))
b=str(input("Pls insert a name of furit:"))
c=str(input("Pls insert a name of furit:"))
d=str(input("Pls insert a name of furit:"))
fruits = (a,b,c,d)

# Access elements by index
first_fruit = fruits[0]
second_fruit = fruits[1]

# Iterate through the tuple
print("Fruits:")
for fruit in fruits:
    print(fruit)

# Check if an element is in the tuple
contains_cherry = "cherry" in fruits

# Find the length of the tuple
num_fruits = len(fruits)

# Concatenate two tuples
e=str(input("Pls insert a new furit:"))
f=str(input("Pls insert a new furit:"))
more_fruits = (e,f)
all_fruits = fruits + more_fruits

# Nested tuple
g= str(input("Pls insert name of colour:"))
h= str(input("Pls insert name of colour:"))
i= str(input("Pls insert name of colour:"))
nested_tuple = (g, (h,i))

# Print the results
print("First fruit:", first_fruit)
print("Second fruit:", second_fruit)
print("Does it contain 'cherry'? ", contains_cherry)
print("Number of fruits:", num_fruits)
print("All fruits:", all_fruits)
print("Nested tuple:", nested_tuple)
