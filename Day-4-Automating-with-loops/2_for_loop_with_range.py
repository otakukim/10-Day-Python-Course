# ==========================================
# SECTION 2: The 'for' Loop with range() - Repeating a Set Number of Times
# ==========================================

print("SECTION 2: The 'for' Loop with range()")
print("-" * 37)

# Exercise 2.1: Simple Counting
# The range() function generates a sequence of numbers, which is perfect for loops.
# range(5) generates numbers from 0 up to (but not including) 5.
print("🚀 Countdown from 0 to 4:")
for number in range(5):
    print(f"Current number: {number}")

print("\n" + "="*50)

# Exercise 2.2: Counting with a Start and Stop
# You can also set a start and stop value: range(start, stop)
print("\n🔔 Counting from 1 to 5:")
for number in range(1, 6): # It stops right before 6
    print(f"Bell rings {number} time(s)!")

print("\n" + "="*50)

# YOUR CODE HERE - Print the 3 times table:
# 1. Use a for loop and range() to loop from 1 to 10.
# 2. Inside the loop, multiply the current number by 3 and print the result.
#    (e.g., "3 x 1 = 3", "3 x 2 = 6", etc.)
# YOUR CODE HERE:



print("\n" + "="*50)
