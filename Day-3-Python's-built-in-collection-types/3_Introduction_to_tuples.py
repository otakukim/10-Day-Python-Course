# ==========================================
# SECTION 3: An Introduction to Tuples (Immutable Lists)
# ==========================================

print("SECTION 3: An Introduction to Tuples")
print("-" * 35)

# A tuple is like a list, but it CANNOT be changed after it's created. It's "immutable".
# You create them with parentheses ().
# Use them for data that should not change, like coordinates or fixed settings.
print("📦 Creating and Accessing a Tuple")

# A tuple of RGB color values for "red"
red_color = (255, 0, 0)
print("The RGB tuple for red is:", red_color)

# You can access items just like a list
red_value = red_color[0]
print(f"The 'red' value is {red_value}")

# The following lines would cause an error because you cannot change a tuple:
# red_color[0] = 200  # This is not allowed!
# red_color.append(50) # This is not allowed!

print("\n" + "="*50)

# YOUR CODE HERE - Work with a coordinate point:
# 1. Create a tuple named `point` to represent an (x, y) coordinate, e.g., (150, 250).
# 2. Print the entire tuple.
# 3. Print a sentence: "The x-coordinate is [your x value] and the y-coordinate is [your y value]."
# YOUR CODE HERE:



print("\n" + "="*50)
