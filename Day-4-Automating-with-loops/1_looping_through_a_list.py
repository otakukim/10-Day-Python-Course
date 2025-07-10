# ==========================================
# DAY 4: Automating with Loops
# ==========================================

# print("Welcome to Day 4! Today, we'll learn how to make Python repeat tasks using loops.")
# print("This is how we automate the boring stuff and work with our data collections efficiently!")
# print("\n" + "="*50)

# ==========================================
# SECTION 1: The 'for' Loop - Doing Something for Each Item
# ==========================================

print("SECTION 1: The 'for' Loop")
print("-" * 25)

# Exercise 1.1: Looping Through a List
# A 'for' loop iterates over a sequence (like a list) and performs an action for each item.
print("📋 Looping through a list of tasks:")

tasks = ["clean room", "do homework", "walk the dog", "read a book"]

# The variable 'task' will hold one item from the 'tasks' list in each iteration.
for task in tasks:
    print(f"To do: {task}")

print("All tasks have been listed!")
print("\n" + "="*50)
