# ==========================================
# SECTION 2: Functions with Parameters - Giving Input to Your Functions
# ==========================================

print("SECTION 2: Functions with Parameters")
print("-" * 35)

# A parameter is a variable listed inside the parentheses in the function definition.
# It's a placeholder for the data you will give the function.
def greet_user(name): # 'name' is the parameter
    print(f"Hello, {name}!")
    print("How are you today?")

# When you call the function, you pass an ARGUMENT to it.
# The argument is the actual value that the parameter will hold.
print("Greeting Alice:")
greet_user("Alice") # "Alice" is the argument

print("\nGreeting Bob:")
greet_user("Bob") # "Bob" is the argument

# A function can have multiple parameters.
def add_numbers(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")

add_numbers(5, 3)
add_numbers(100, 50)

print("\n" + "="*50)

# YOUR CODE HERE - Create a function that describes a pet.
# 1. Define a function called `describe_pet`.
# 2. It should take two parameters: `animal_type` and `pet_name`.
# 3. Inside the function, print a sentence like "I have a [animal_type] named [pet_name]."
# 4. Call your function for a dog named "Willie" and a cat named "Whiskers".
# YOUR CODE HERE:



print("\n" + "="*50)
