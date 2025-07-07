# ==========================================
# SECTION 2: Understanding Data Types
# ==========================================

print("SECTION 2: Data Types in Python")
print("-" * 30)

# Exercise 2.1: Discovering Data Types
# Learn that input() always gives strings and explore other types
user_input = input("Enter any number: ")
print("You entered:", user_input)
print("Type of your input:", type(user_input))

# Compare with actual data types
text_number = "25"
real_number = 25
boolean_value = True
decimal_number = 25.5

print("Text '25':", text_number, "- Type:", type(text_number))
print("Number 25:", real_number, "- Type:", type(real_number))
print("Boolean True:", boolean_value, "- Type:", type(boolean_value))
print("Decimal 25.5:", decimal_number, "- Type:", type(decimal_number))

print("\n" + "="*50)

# YOUR CODE HERE - Create your own data type examples:
# Make variables of each type and print them with their types
# YOUR CODE HERE:


print("\n" + "="*50)

# Exercise 2.2: Data Type Behaviors
# Learn how different types behave differently
print("\n🔍 How Data Types Behave:")

# Strings can be combined
greeting = "Hello" + " " + "World"
print("String combination:", greeting)

# Numbers can be calculated
number_math = 10 + 15
print("Number calculation:", number_math)

# Interesting behaviors
print("String + String:", "5" + "3")  # This gives "53"
print("Number + Number:", 5 + 3)      # This gives 8
print("String × Number:", "Hi! " * 3)  # This repeats the string

print("\n" + "="*50)

# YOUR CODE HERE - Experiment with data type behaviors:
# Try multiplying strings by numbers, comparing different types
# YOUR CODE HERE:




print("\n" + "="*50)
