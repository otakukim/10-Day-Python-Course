# ==========================================
# SECTION 2: The 'math' Module - For Mathematical Functions
# ==========================================

print("SECTION 2: The 'math' Module")
print("-" * 28)

# The 'math' module provides access to more advanced math functions and constants.
import math

# Exercise 2.1: Finding the Square Root
# math.sqrt(x) returns the square root of x.
number = 81
square_root = math.sqrt(number)
print(f"The square root of {number} is {square_root}")

print("\n" + "="*50)

# Exercise 2.2: Using Mathematical Constants
# The math module also contains constants like Pi.
print(f"The value of Pi is approximately: {math.pi}")

# Let's calculate the circumference of a circle with a radius of 5
radius = 5
circumference = 2 * math.pi * radius
print(f"The circumference of a circle with radius {radius} is {circumference:.2f}") # .2f formats to 2 decimal places

print("\n" + "="*50)

# YOUR CODE HERE - Calculate the diagonal of a square.
# The formula is: diagonal = side * sqrt(2)
# 1. Create a variable `side_length` and set it to 10.
# 2. Use math.sqrt() to calculate the diagonal.
# 3. Print the result.
# YOUR CODE HERE:



print("\n" + "="*50)
