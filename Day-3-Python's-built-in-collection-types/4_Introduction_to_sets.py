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

# YOUR CODE HERE - Manage tags for a blog post:
# 1. Create a list of tags with some duplicates, e.g., ["python", "code", "fun", "python", "guide"].
# 2. Create a set from this list to get the unique tags.
# 3. Print the set of unique tags.
# YOUR CODE HERE:



print("\n" + "="*50)

