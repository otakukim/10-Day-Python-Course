# ==========================================
# SECTION 3: Functions that Return Values
# ==========================================

print("SECTION 3: Functions that Return Values")
print("-" * 39)

# So far, our functions have only performed actions (printing).
# But what if we want a function to give us a result back? We use the 'return' keyword.

def square(number):
    return number * number # This function sends a value back

# When you call a function with a return statement, you can store the result in a variable.
result = square(5)
print(f"The square of 5 is {result}")

# You can also use the returned value directly.
print(f"The square of 10 is {square(10)}")

# Contrast this with the 'add_numbers' function from before.
# It only printed the result, it didn't give it back for us to use later.

print("\n" + "="*50)

# YOUR CODE HERE - Create a function that calculates the area of a rectangle.
# 1. Define a function called `calculate_area`.
# 2. It should take two parameters: `width` and `height`.
# 3. Inside the function, it should `return` the area (width * height).
# 4. Call the function with a width of 10 and a height of 5, and store the result in a variable.
# 5. Print the result in a sentence like "The area is 50."
# YOUR CODE HERE:



print("\n" + "="*50)
