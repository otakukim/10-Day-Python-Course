# ============================================================
# SECTION 5: Day 3 Project - The Ultimate Game Character Creator
# ============================================================

print("SECTION 5: Day 3 Project - The Ultimate Game Character Creator")
print("-" * 60)

# This project uses all four data structures we learned today.

print("⚔️ Welcome to the Ultimate Game Character Creator! ⚔️")

# 1. DICTIONARY: The main container for our character
character = {
    "name": input("What is your character's name? "),
    "level": 1,
    "hp": 100
}

# 2. TUPLE: For data that won't change, like class and alignment.
# We create the tuple directly and add it to our dictionary.
character_class = ("Warrior", "Lawful Good")
character["class_info"] = character_class

# 3. LIST: For a changeable, ordered inventory.
# We start with a basic list and add it to our dictionary.
inventory = ["rusty sword", "cloth armor"]
character["inventory"] = inventory

# --- Perform a list operation ---
print("\nYou find a health potion!")
character["inventory"].append("health potion") # Add an item to the list

# 4. SET: For unique skills. A character can't learn the same skill twice.
# We start with an empty set and add it to our dictionary.
skills = set()
character["skills"] = skills

# --- Perform a set operation ---
print("You learn a new skill: Power Attack!")
character["skills"].add("Power Attack")
character["skills"].add("Power Attack") # Adding it again does nothing!

# 5. Print the final, formatted character sheet
print("\n--- Your Generated Character Sheet ---")
print(f"👤 Name: {character['name']}")
print(f"❤️ HP: {character['hp']} | 🎖️ Level: {character['level']}")

# Accessing data from the TUPLE
print(f"⚔️ Class: {character['class_info'][0]} ({character['class_info'][1]})")

# Accessing data from the LIST
print(f"🎒 Inventory: {character['inventory']}")

# Accessing data from the SET
print(f"✨ Skills: {character['skills']}")
print("------------------------------------")


print("\n" + "="*50)
# print("Congratulations on completing Day 3! You now have a solid understanding of how to organize data using lists, dictionaries, tuples, and sets.")
# print("Tomorrow, we will learn how to use loops to work with these structures!")
