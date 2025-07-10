# ==========================================
# SECTION 3: The 'while' Loop - Repeating as Long as a Condition is True
# ==========================================

print("SECTION 3: The 'while' Loop")
print("-" * 27)

# Exercise 3.1: The Infinite Loop (and How to Fix It)
# A 'while' loop continues as long as its condition is True.
# If the condition NEVER becomes false, you get an infinite loop!
print("☠️ Demonstrating an infinite loop (don't run this version!):")
print("""
# DANGEROUS CODE:
# count = 1
# while count <= 5:
#     print("This will run forever!")
# The variable 'count' never changes, so the condition is always true.
""")

print("\n✅ The FIX: Always change the condition variable inside the loop.")
# It's common to use a counter variable.
count = 1
while count <= 5:
    print(f"This is loop iteration number {count}")
    count = count + 1 # IMPORTANT: This line makes the loop eventually stop!

print("The while loop has ended correctly.")
print("\n" + "="*50)


# Exercise 3.2: Creating a Design with a While Loop
print("\n🎨 Drawing a triangle with a while loop:")
lines = 1
while lines <= 7:
    print("*" * lines)
    lines = lines + 1

print("\n" + "="*50)


# Exercise 3.3: An Interactive While Loop
# This is great for making menus or games that run until the user wants to quit.
print("\n🗣️ A Program That Runs Until You Say 'quit'")

command = ""
while command.lower() != "quit":
    command = input("Enter a command (or type 'quit' to exit): ")
    print(f"Executing command: '{command}'")

print("Goodbye! Thanks for using the program.")
print("\n" + "="*50)

# YOUR CODE HERE - Simple guessing game:
# 1. Create a variable `secret_number = 7`.
# 2. Create a variable `guess = 0`.
# 3. Use a `while` loop that continues as long as `guess` is NOT equal to `secret_number`.
# 4. Inside the loop, ask the user to guess the number and store it in the `guess` variable.
#    (Remember to convert the input to an integer!)
# 5. After the loop ends (meaning they guessed correctly), print "You got it!".
# YOUR CODE HERE:



print("\n" + "="*50)
