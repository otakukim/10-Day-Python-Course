# 🐍 Python Day 3 Cheat Sheet
## Storing Collections of Data

---

## 📝 Table of Contents
1. [Core Definitions](#-core-definitions)
2. [Key Differences at a Glance](#-key-differences-at-a-glance)
3. [Lists](#️-lists)
4. [Dictionaries](#-dictionaries)
5. [Tuples](#-tuples)
6. [Sets](#-sets)
7. [Quick Reference](#-quick-reference)
8. [Pro Tips](#-pro-tips)
9. [Common Mistakes](#-common-mistakes)

---

## 🧠 Core Definitions

- **List**: An ordered and changeable collection that allows duplicate members.
- **Dictionary**: A collection of key-value pairs. It's changeable and does not allow duplicate keys.
- **Tuple**: An ordered and unchangeable collection that allows duplicate members.
- **Set**: An unordered and unindexed collection that does not allow duplicate members.

---

## 📊 Key Differences at a Glance

| Feature       | List        | Dictionary         | Tuple        | Set              |
|---------------|-------------|--------------------|--------------|------------------|
| **Syntax**    | `[ ]`       | `{key: value}`     | `( )`        | `{item1, item2}` |
| **Ordered**   | Yes         | Yes (Py 3.7+)      | Yes          | No               |
| **Changeable**| Yes         | Yes                | No           | Yes              |
| **Duplicates**| Yes         | No (keys)          | Yes          | No               |
| **Access**    | Index       | Key                | Index        | N/A              |

> *Dictionaries are ordered in Python 3.7+, but access them by key, not position.*

---

## 🗂️ Lists

### Creating & Accessing
```python
inventory = ["sword", "shield", "potion"]
first_item = inventory[0]
last_item = inventory[-1]
```

### Slicing
```python
first_two = inventory[0:2]
all_but_first = inventory[1:]
```

### Adding Items
```python
inventory.append("gold coin")
inventory.insert(1, "armor")
```

### Removing Items
```python
del inventory[2]
inventory.remove("potion")
removed_item = inventory.pop()
```

> ✅ Lists are ordered, changeable, and great for sequences.

---

## 📖 Dictionaries

### Creating & Accessing
```python
player_stats = {
    "name": "Alex",
    "level": 5,
    "health": 100
}
player_name = player_stats["name"]
player_health = player_stats["health"]
```

### Adding & Modifying
```python
player_stats["mana"] = 50
player_stats["level"] = 6
```

### Removing Items
```python
del player_stats["health"]
```

> ✅ Dictionaries are ideal for storing connected data via key-value pairs.

---

## 📦 Tuples

### Creating & Accessing
```python
coordinates = (100, 250)
rgb_color = (255, 0, 0)
x_coord = coordinates[0]
```

### What You CAN'T Do
```python
coordinates[0] = 150      # ❌ Error
coordinates.append(50)    # ❌ Error
del coordinates[0]        # ❌ Error
```

> ✅ Use tuples when data should never change.

---

## ✨ Sets

### Creating & Using
```python
tags = ["python", "code", "fun", "python", "guide"]
unique_tags = set(tags)
```

### Membership Check
```python
"python" in unique_tags  # True
"java" in unique_tags    # False
```

> ✅ Sets are best for unique values and fast membership checks.

---

## ⚡ Quick Reference

### List Methods
```python
my_list.append(item)
my_list.insert(i, item)
my_list.remove(item)
my_list.pop(i)
len(my_list)
```

### Dictionary Methods
```python
my_dict[key] = value
del my_dict[key]
key in my_dict
len(my_dict)
```

### General Functions
```python
len(collection)
list(my_tuple)
set(my_list)
```

---

## 💡 Pro Tips

- Use a **List** for ordered, changeable data.
- Use a **Dictionary** for key-value mappings.
- Use a **Tuple** when values should remain fixed.
- Use a **Set** to store unique, unordered items.

### Nesting Structures
```python
players = [
    {"name": "Alice", "level": 10},
    {"name": "Bob", "level": 8}
]
print(players[0]["name"])  # "Alice"
```

### Safe Dictionary Access
```python
if "mana" in player_stats:
    print(player_stats["mana"])
else:
    print("This player has no mana.")
```

---

## 🎯 Common Mistakes

### ❌ Accessing dict by index
```python
player_stats[0]  # ❌ KeyError!
```

✅ Access by key:
```python
player_stats["name"]
```

---

### ❌ Missing quotes in string keys
```python
stats = {name: "Alex"}  # ❌ NameError!
```

✅ Use quotes:
```python
stats = {"name": "Alex"}
```

---

### ❌ Modifying a tuple
```python
my_tuple = (1, 2, 3)
my_tuple[0] = 99  # ❌ TypeError!
```

✅ Convert to list first:
```python
my_list = list(my_tuple)
my_list[0] = 99
my_tuple = tuple(my_list)
```

---

*Happy coding! 🐍✨*
