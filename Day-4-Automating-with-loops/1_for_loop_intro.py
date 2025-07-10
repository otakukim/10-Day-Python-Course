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

# Exercise 1.2: Looping Through a Dictionary
# When you loop through a dictionary, you get its keys by default.
print("\n📖 Looping through a dictionary:")

player_stats = {
    "name": "Alex",
    "level": 5,
    "health": 100
}

print("Player Stat Keys:")
for stat_key in player_stats:
    # You can use the key to access the value inside the loop
    stat_value = player_stats[stat_key]
    print(f"-> Key: '{stat_key}', Value: {stat_value}")

print("\n" + "="*50)

# Exercise 1.3: Drawing a Shape with a Loop
# Since turtle graphics don't work in all online IDEs, let's draw with text!
# We can use a loop to print a square made of asterisks.
print("\n🎨 Drawing a square with a for loop:")

size = 5
# The top border
print("*" * size)

# The middle part: loop `size - 2` times for the inner rows
for _ in range(size - 2):
    # Print a star, then spaces, then a star
    print("*" + " " * (size - 2) + "*")

# The bottom border (only if size > 1)
if size > 1:
    print("*" * size)

print("Square drawing complete!")


print("\n" + "="*50)

