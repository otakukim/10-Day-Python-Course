# 🐍 Python Day 3 Cheat Sheet
## Storing Collections of Data

---

## 📝 Table of Contents
1. [Core Definitions](#-core-definitions)
2. [Key Differences at a Glance](#-key-differences-at-a-glance)
3. [Lists](#-lists)
4. [Dictionaries](#-dictionaries)
5. [Tuples](#-tuples)
6. [Sets](#-sets)
7. [Quick Reference](#-quick-reference)
8. [Pro Tips](#-pro-tips)
9. [Common Mistakes](#-common-mistakes-to-avoid)

---

## 🧠 Core Definitions

* **List:** An **ordered** and **changeable** collection that allows duplicate members. It's your most common tool for storing a sequence of items.
* **Dictionary:** A collection of **key-value pairs**. It's changeable and does not allow duplicate keys. Used for connecting related pieces of information.
* **Tuple:** An **ordered** and **unchangeable** collection that allows duplicate members. Use it for data that you know should not change.
* **Set:** An **unordered** and unindexed collection that does **not** allow duplicate members. Use it to store unique items and perform mathematical set operations.

---

## 📊 Key Differences at a Glance

| Feature | List | Dictionary | Tuple | Set |
| :--- | :---: | :---: | :---: | :---: |
| **Syntax** | `[ ]` | `{key: value}` | `( )` | `{item1, item2}` |
| **Ordered** | **Yes** | Yes (in Python 3.7+)* | **Yes** | No |
| **Changeable** | **Yes** | **Yes** | No | **Yes** |
| **Duplicates** | **Yes** | No (Keys) | **Yes** | No |
| **Access** | Index | Key | Index | N/A |

*\*While dictionaries are ordered in modern Python, it's best practice to access items by key, not by their position.*

---

## 🗂️ Lists

### Creating & Accessing
```python
# Create a list with square brackets []
inventory = ["sword", "shield", "potion"]

# Access by index (starts at 0)
first_item = inventory[0]  # "sword"
last_item = inventory[-1] # "potion"
```

### Slicing (Getting Multiple Items)
```python
# Syntax: list[start:stop]
# Grabs items from start up to (but not including) stop
first_two = inventory[0:2] # ["sword", "shield"]
all_but_first = inventory[1:] # ["shield", "potion"]
```

### Adding Items
```python
# .append() adds to the end
inventory.append("gold coin")
# inventory is now ["sword", "shield", "potion", "gold coin"]

# .insert() adds at a specific index
inventory.insert(1, "armor")
# inventory is now ["sword", "armor", "shield", "potion", "gold coin"]
```

### Removing Items
```python
# del removes by index
del inventory[2] # Removes "shield"

# .remove() searches for and removes a value
inventory.remove("potion")

# .pop() removes the last item and returns it
removed_item = inventory.pop() # removed_item is "gold coin"
```

**Key Point:** Lists are ordered, changeable, and your go-to for storing a sequence of items.

---

## 📖 Dictionaries

### Creating & Accessing
```python
# Create a dictionary with curly braces {} and key:value pairs
player_stats = {
    "name": "Alex",
    "level": 5,
    "health": 100
}

# Access values by their key (not by index!)
player_name = player_stats["name"] # "Alex"
player_health = player_stats["health"] # 100
```

### Adding & Modifying
```python
# Add a new key-value pair
player_stats["mana"] = 50

# Modify an existing value
player_stats["level"] = 6
```

### Removing Items
```python
# del removes a key-value pair by its key
del player_stats["health"]
```

**Key Point:** Dictionaries are for storing connected data. The order is not guaranteed (in older Python versions), but the link between a key and its value is.

---

## 📦 Tuples

### Creating & Accessing
```python
# Create a tuple with parentheses ()
# Tuples are IMMUTABLE (cannot be changed)
coordinates = (100, 250)
rgb_color = (255, 0, 0)

# Access just like a list
x_coord = coordinates[0] # 100
```

### What You CAN'T Do
```python
# These lines will cause an ERROR
coordinates[0] = 150      # Cannot change a value
coordinates.append(50)    # Cannot add a value
del coordinates[0]        # Cannot remove a value
```

**Key Point:** Use tuples for data that should never change, like coordinates or fixed settings.

---

## ✨ Sets

### Creating & Using
```python
# Create a set from a list to get unique items
tags = ["python", "code", "fun", "python", "guide"]
unique_tags = set(tags)
# unique_tags is {"python", "code", "fun", "guide"}

# Sets are UNORDERED. You cannot access by index.
# The main use is checking for membership.
has_python = "python" in unique_tags # True
has_java = "java" in unique_tags   # False
```

**Key Point:** Use sets when you need to store unique items and quickly check if an item exists in the collection.

---

## ⚡ Quick Reference

### List Methods
```python
my_list.append(item)    # Add to end
my_list.insert(i, item) # Add at index i
my_list.remove(item)    # Remove first occurrence of item
my_list.pop(i)          # Remove and return item at index i (or last item if i is omitted)
len(my_list)            # Get number of items
```

### Dictionary Methods
```python
my_dict[key] = value    # Add or modify entry
del my_dict[key]        # Remove entry
key in my_dict          # Check if key exists
len(my_dict)            # Get number of key-value pairs
```

### General Functions
```python
# Works on lists, dictionaries, tuples, and sets
len(collection)

# Create from another collection
list(my_tuple)
set(my_list)
```

---

## 💡 Pro Tips

1.  **Choose the Right Tool:**
    * Need an ordered collection you can change? **Use a List.**
    * Need to link keys to values? **Use a Dictionary.**
    * Need an ordered collection that never changes? **Use a Tuple.**
    * Need to store unique items and check for membership? **Use a Set.**

2.  **Combine Data Structures:** You can nest collections inside each other for powerful data organization.
    ```python
    # A list of dictionaries
    players = [
        {"name": "Alice", "level": 10},
        {"name": "Bob", "level": 8}
    ]
    # Accessing nested data
    print(players[0]["name"]) # "Alice"
    ```

3.  **Check Before Accessing:** Use the `in` keyword to avoid errors when accessing dictionary keys.
    ```python
    if "mana" in player_stats:
        print(f"Mana: {player_stats['mana']}")
    else:
        print("This player has no mana.")
    ```

---

## 🎯 Common Mistakes to Avoid

❌ **Trying to access a dictionary by index.**
```python
# Wrong
first_stat = player_stats[0] # This will cause a KeyError!
```
✅ **Access dictionaries by key.**
```python
# Correct
first_stat = player_stats["name"]
```

❌ **Forgetting quotes around string keys in a dictionary.**
```python
# Wrong
stats = {name: "Alex"} # This will cause a NameError!
```
✅ **Always use quotes for string keys.**
```python
# Correct
stats = {"name": "Alex"}
```

❌ **Trying to change a tuple.**
```python
# Wrong
my_tuple = (1, 2, 3)
my_tuple[0] = 99 # This will cause a TypeError!
```
✅ **If you need to change it, make it a list first.**
```python
# Correct
my_list = list(my_tuple)
my_list[0] = 99
my_tuple = tuple(my_list) # Optional: convert back to tuple
```

---

*Happy coding! 🐍✨*
