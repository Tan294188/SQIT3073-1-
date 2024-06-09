# Define a string variable
message = "Hello,World!!"

# Print the string
print(message)

# Get user input for the name
name = input("Enter your name: ")
#
first_character = name[0]
print("The first character of your name is:", first_character)
Lengthname= len(name)
contains_space=" "in name
if contains_space==1:
    Find= name.find(" ")
    Lname=""
    for i in range (0,Find):
        Lname=Lname+name[i]
    print("Your last name is",Lname)   

# Concatenate (combine) two strings
greeting = "Hello, " + name + "!"
print(greeting)

# Use string methods
uppercase_greeting = greeting.upper()
print("Uppercase greeting:", uppercase_greeting)

# Check if a substring is in the string
contains_Bye = "Bye" in greeting
print("Does the message contain 'Bye'? ", contains_Bye)

# Replace part of the string
new_message = greeting.replace("Hello", "Bye")
print("Updated message:", new_message)
