# ==========================================
# SECTION 2: Introduction to Dictionaries
# ==========================================

print("SECTION 2: Introduction to Dictionaries")
print("-" * 40)

# Exercise 2.1: Creating and Accessing Dictionaries
# Dictionaries store data in key-value pairs, like a real-world dictionary.
# You use a unique key (a string) to look up its value.
print("📖 Creating and Accessing a Dictionary")

student = {
    "name": "Alex",
    "age": 17,
    "grade": 11,
}
print("Student data:", student)

# Access values by their key inside square brackets.
student_name = student["name"]
print(f"The student's name is {student_name}.")

print("\n" + "="*50)

# YOUR CODE HERE - Create a "car" dictionary:
# 1. Create a dictionary for a car with keys "make", "model", and "year".
# 2. Give them appropriate values (e.g., "Ford", "Mustang", 1969).
# 3. Print a sentence like "I have a 1969 Ford Mustang." using the dictionary values.
# YOUR CODE HERE:



print("\n" + "="*50)

# Exercise 2.2: Adding and Modifying Dictionary Entries
# You can easily add new key-value pairs or change existing ones.
print("\n✏️ Adding to and Modifying a Dictionary")

user_profile = {"username": "coder_01"}
print("Original profile:", user_profile)

# To ADD a new entry, just assign a value to a new key.
user_profile["level"] = 1
print("Added level:", user_profile)

# To CHANGE an existing entry, just assign a new value to that key.
user_profile["level"] = 2
print("Changed level:", user_profile)

print("\n" + "="*50)

# YOUR CODE HERE - Manage character stats:
# 1. Create a dictionary for a character with one key: "health", set to 100.
# 2. The character finds armor! Add a new key "armor" and set it to 50.
# 3. The character gets hit! Change their "health" to 80.
# 4. Print the final stats.
# YOUR CODE HERE:



print("\n" + "="*50)

# Exercise 2.3: Removing from Dictionaries
# The `del` keyword is the primary way to remove a key-value pair.
print("\n🗑️ Removing from a Dictionary")

contact = {
    "name": "John Doe",
    "email": "john.doe@email.com",
    "phone": "555-1234"
}
print("Full contact info:", contact)

# Use del to remove a key and its associated value.
del contact["phone"]
print("Contact info without phone:", contact)

print("\n" + "="*50)
