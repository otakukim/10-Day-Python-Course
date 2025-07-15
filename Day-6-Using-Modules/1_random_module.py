# ==========================================
# DAY 6: Using Modules - Python's Superpowers
# ==========================================

# print("Welcome to Day 6! Today, we'll learn how to import and use modules.")
# print("Modules are like toolboxes full of pre-written code that give our programs new powers!")
# print("\n" + "="*50)

# ==========================================
# SECTION 1: The 'random' Module - For All Things Random
# ==========================================

print("SECTION 1: The 'random' Module")
print("-" * 30)

# To use a module, you must first import it.
import random

# Exercise 1.1: Generating Random Integers
# random.randint(a, b) returns a random integer between a and b (inclusive).
print("Rolling a 6-sided die...")
roll = random.randint(1, 6)
print(f"You rolled a {roll}!")

print("\n" + "="*50)

# Exercise 1.2: Making a Random Choice
# random.choice(sequence) returns a random element from a list or tuple.
print("Choosing a team captain...")
players = ["Alice", "Bob", "Charlie", "David"]
captain = random.choice(players)
print(f"The new captain is: {captain}!")

print("\n" + "="*50)
