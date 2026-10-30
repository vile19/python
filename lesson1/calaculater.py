# This is a simple calculator program that takes two number inputs from the user and prints their sum.

# Take two numbers inputs from the user
x = float(input("x="))
y = float(input("y="))

# Calculate the sum of the two numbers and round it to the nearest integer
z = round(x + y)

# Print the sum of the two numbers
print(f"{z:,}")