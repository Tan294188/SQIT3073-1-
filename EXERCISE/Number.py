# Get user input for integer and floating-point numbers
x = float(input("Enter a number (x): "))
y = float(input("Enter another number (y): "))

# Perform arithmetic operations
sum_xy = x + y
difference_xy = x-y
product_xy = x * y
quotient_xy = x / y
modulus_xy = x % y
exponentiation_xy = x ** y

# Print the results
print("x+y=", sum_xy)
print("x-y=", difference_xy)
print("x*y=", product_xy)
print("x/y=", quotient_xy)
print("x%y=", modulus_xy)
print("x^y=", exponentiation_xy)

# Use built-in functions for numerical operations
absolute_x = abs(x)
rounded_y = round(y)
max_value = max(x,y)
min_value = min(x,y)

print("Absolute value of x:", absolute_x)
print("Rounded value of y:", rounded_y)
print("Max value:", max_value)
print("Min value:", min_value)

# Import the math module for more advanced math operations
import math

square_root_x = math.sqrt(x)
logarithm_base_10_x = math.log10(x)
factorial_y = math.factorial(rounded_y)

print("Square root of a:", square_root_x)
print("Logarithm base 10 of a:", logarithm_base_10_x)
print(f"Factorial of |rounded_y|:", factorial_y)
