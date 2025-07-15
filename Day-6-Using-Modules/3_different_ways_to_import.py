# ==========================================
# SECTION 3: Different Ways to Import
# ==========================================

print("SECTION 3: Different Ways to Import")
print("-" * 35)

# So far, we've used 'import module_name'. Here are other ways.

# Method 2: Importing a specific function
# This brings only the 'choice' function into our program. We don't need to type 'random.' anymore.
from random import choice
print("Using 'from random import choice':")
players = ["Alice", "Bob", "Charlie", "David"]
captain = choice(players) # No 'random.' prefix needed
print(f"The captain is {captain}")

# Method 3: Using an alias
# If a module has a long name, you can give it a shorter nickname (alias) using 'as'.
import math as m
print("\nUsing 'import math as m':")
print(f"The value of Pi is {m.pi}") # Use the alias 'm' instead of 'math'

print("\n" + "="*50)
