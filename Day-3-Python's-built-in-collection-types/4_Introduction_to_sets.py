# ==========================================
# SECTION 4: An Introduction to Sets (Unique Items)
# ==========================================

print("SECTION 4: An Introduction to Sets")
print("-" * 34)

# A set is a collection that is UNORDERED and contains NO DUPLICATE items.
# They are great for removing duplicates from a list or checking if an item exists in a collection.
print("✨ Creating a Set to Find Unique Items")

numbers_with_duplicates = [10, 20, 30, 20, 40, 10, 50]
print("Original list with duplicates:", numbers_with_duplicates)

# Convert the list to a set to automatically remove duplicates
unique_numbers = set(numbers_with_duplicates)
print("The set of unique numbers:", unique_numbers)

# You cannot access items by index (e.g., unique_numbers[0]) because sets are unordered.
# But you can check for membership very quickly.
print("Is 20 in our set?", 20 in unique_numbers)
print("Is 99 in our set?", 99 in unique_numbers)

print("\n" + "="*50)

# Exercise 4.2: Adding and Removing Items from a Set
print("\n🔄 Adding and Removing from a Set")

# Let's start with a set of approved users
approved_users = {"Alice", "Bob", "Charlie"}
print("Original users:", approved_users)

# Use .add() to add a new user. If the user already exists, nothing happens.
approved_users.add("David")
approved_users.add("Alice") # This does nothing, as "Alice" is already in the set
print("After adding users:", approved_users)

# Use .remove() to delete an item. This will cause an ERROR if the item doesn't exist.
approved_users.remove("Bob")
print("After removing 'Bob':", approved_users)
# The following line would cause an error:
# approved_users.remove("Eve") # Raises a KeyError because "Eve" is not in the set

# Use .discard() for safe removal. It does nothing if the item isn't there.
approved_users.discard("Charlie") # Removes "Charlie"
approved_users.discard("Eve")     # Does nothing, no error
print("After discarding users:", approved_users)


print("\n" + "="*50)

# YOUR CODE HERE - Manage tags for a blog post:
# 1. Create a list of tags with some duplicates, e.g., ["python", "code", "fun", "python", "guide"].
# 2. Create a set from this list to get the unique tags.
# 3. A new tag "beginner" needs to be added. Use .add().
# 4. The "fun" tag is no longer relevant. Remove it.
# 5. Print the final set of tags.
# YOUR CODE HERE:
