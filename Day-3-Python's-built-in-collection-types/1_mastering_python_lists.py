# ==========================================
# DAY 3: Storing Collections of Data
# ==========================================

# print("Welcome to Day 3! Today, we'll focus on how Python stores collections of data.")
# print("We will master lists and get our first look at another powerful tool: dictionaries.")
# print("\n" + "="*50)

# ==========================================
# SECTION 1: Mastering Python Lists
# ==========================================

print("SECTION 1: Mastering Python Lists")
print("-" * 32)

# Exercise 1.1: Creating and Accessing a SINGLE Item
# A list is a container for an ordered sequence of items.
# We access items using an index, which starts from 0.
print("📋 Accessing Single List Items")

inventory = ["sword", "shield", "potion", "gold coin", "map"]
print("Full inventory:", inventory)

# Accessing the VERY FIRST item (index 0)
first_item = inventory[0]
print("First item:", first_item)

# Accessing the VERY LAST item (negative index -1)
last_item = inventory[-1]
print("Last item:", last_item)

# Accessing the second item (index 1)
second_item = inventory[1]
print("Second item:", second_item)

print("\n" + "="*50)

# YOUR CODE HERE - Practice accessing single items:
# 1. Create a list of your three favorite foods.
# 2. Print the entire list.
# 3. Print the food that is your absolute favorite (the first one).
# 4. Print your least favorite of the three (the last one).
# YOUR CODE HERE:



print("\n" + "="*50)

# Exercise 1.2: Accessing MULTIPLE Items (Slicing)
# Slicing lets you grab a "slice" or a sub-section of your list.
print("\n🔪 Slicing a List to Get Multiple Items")

# The syntax is list[start:stop]
# It gets items from the 'start' index up to, but NOT including, the 'stop' index.
first_three_items = inventory[0:3]
print("First three items:", first_three_items)

# You can leave out the start or stop.
# Leaving out the start defaults to the beginning.
also_first_three = inventory[:3]
print("Also first three:", also_first_three)

# Leaving out the stop defaults to the end.
from_second_item_on = inventory[1:]
print("From the second item to the end:", from_second_item_on)

print("\n" + "="*50)

# YOUR CODE HERE - Practice slicing:
# 1. Create a list of the days of the week: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# 2. Create a slice containing just the weekdays.
# 3. Create a slice containing just the weekend.
# 4. Print both slices.
# YOUR CODE HERE:



print("\n" + "="*50)

# Exercise 1.3: ADDING Items to a List
# Lists are dynamic, meaning you can change their size.
print("\n➕ Adding Items to a List")

guests = ["Alice", "Bob"]
print("Original guests:", guests)

# .append() adds an item to the VERY END of the list.
guests.append("Charlie")
print("Appended 'Charlie':", guests)

# .insert() adds an item at a SPECIFIC INDEX.
guests.insert(0, "Zelda")
print("Inserted 'Zelda' at the start (index 0):", guests)

print("\n" + "="*50)

# YOUR CODE HERE - Build a grocery list:
# 1. Start with an empty list called `groceries`.
# 2. Append "milk" and "bread" to the list.
# 3. You forgot eggs! Insert "eggs" at the beginning of the list.
# 4. Print the final list.
# YOUR CODE HERE:



print("\n" + "="*50)

# Exercise 1.4: REMOVING Items from a List
# There are several ways to remove items from a list.
print("\n➖ Removing Items from a List")

playlist = ["Song A", "Song B", "Song C", "Song D"]
print("Original playlist:", playlist)

# del removes an item at a specific index.
del playlist[2] # This removes "Song C"
print("After deleting item at index 2:", playlist)

# .pop() removes the item at an index AND returns it, so you can save it.
# If you don't give it an index, it removes the LAST item.
removed_song = playlist.pop() # Removes "Song D"
print(f"Popped song was '{removed_song}'. List is now:", playlist)

# .remove() searches for the first matching VALUE and removes it.
playlist.remove("Song A")
print("After removing 'Song A' by value:", playlist)

print("\n" + "="*50)

# YOUR CODE HERE - Manage party RSVPs:
# 1. Create a list of guests: ["Eve", "Mallory", "Trent"]
# 2. Mallory can't make it. Remove "Mallory" by its value.
# 3. You need to un-invite the first person on the list. Use `del`.
# 4. Print the final guest list.
# YOUR CODE HERE:



print("\n" + "="*50)
