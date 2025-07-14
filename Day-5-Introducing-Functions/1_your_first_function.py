# ==========================================
# DAY 5: Introducing Functions
# ==========================================

# print("Welcome to Day 5! Today, we'll learn how to package our code into reusable blocks called functions.")
# print("This is the key to writing clean, organized, and powerful programs!")
# print("\n" + "="*50)

# ==========================================
# SECTION 1: Your First Function - Defining and Calling
# ==========================================

print("SECTION 1: Your First Function")
print("-" * 30)

# A function is a named block of code that performs a specific task.
# You create it using the 'def' keyword.
# This function is DEFINED here, but it won't run yet.
def show_greeting():
    print("Hello, World!")
    print("Welcome to the world of functions.")

# To run the code inside the function, you must CALL it by its name.
print("Calling the function now:")
show_greeting()

print("\nCalling it again:")
show_greeting() # The beauty is you can reuse it as many times as you want!

print("\n" + "="*50)
