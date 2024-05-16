# Create a list of numbers
a=int(input("Enter a number(a):"))
b=int(input("Enter a number(b):"))
c=int(input("Enter a number(c):"))
d=int(input("Enter a number(d):"))
e=int(input("Enter a number(e):"))
numbers = [a,b,c,d,e]

# Print the list
print("Original list:", numbers)

numbers.sort()
print("Sorted list:", numbers)

# Access elements by index
third_element = numbers[2]
print("The third element by sorted is:", third_element)

# Slice the list to get a subset
subset = numbers[2:4]
print("Subset of the list:", subset)

# Append an element to the end of the list
numbers.append(int(input("pls add a new number in the list")))
print("List after appending :", numbers)

# Remove an element by value
numbers.remove(int(input("pls insert the number you want to remove :")))
print("List after removing :", numbers)

# Reverse the list
numbers.reverse()
print("Reversed list:", numbers)

# Modify an element in the list
numbers[4] = int(input("Pls replace the smallest number with other number:"))
print("Modified list:", numbers)

# Find the index of an element
index_of_y = numbers.index(int(input("Pls input the number in the list to find the index(y) :")))
print("Index of y:", index_of_y)

# Check if an element is in the list
contains_z = int(input("Pls insert a number to check rather the number in the list:")) in numbers
print("Does the list contain ?", contains_z)

