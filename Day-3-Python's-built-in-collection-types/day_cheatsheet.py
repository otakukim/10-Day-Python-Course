# 🐍 Python Day 3 Cheat Sheet: Storing Collections of Data

## 📝 Table of Contents
- [Core Definitions](#-core-definitions)
- [Key Differences at a Glance](#-key-differences-at-a-glance)
- [Lists](#️-lists)
- [Dictionaries](#-dictionaries)
- [Tuples](#-tuples)
- [Sets](#-sets)
- [Quick Reference](#-quick-reference)
- [Pro Tips](#-pro-tips)
- [Common Mistakes](#-common-mistakes)

---

## 🧠 Core Definitions

- **List**: An ordered and changeable collection that allows duplicate members.  
- **Dictionary**: A collection of key-value pairs. Changeable and does not allow duplicate keys.  
- **Tuple**: An ordered and unchangeable collection that allows duplicate members.  
- **Set**: An unordered, unindexed collection with unique elements.

---

## 📊 Key Differences at a Glance

| Feature       | List           | Dictionary         | Tuple           | Set              |
|---------------|----------------|--------------------|------------------|------------------|
| **Syntax**    | `[ ]`          | `{key: value}`     | `( )`            | `{item1, item2}` |
| **Ordered**   | Yes            | Yes (Python 3.7+)  | Yes              | No               |
| **Changeable**| Yes            | Yes                | No               | Yes              |
| **Duplicates**| Yes            | No (keys only)     | Yes              | No               |
| **Access**    | Index          | Key                | Index            | N/A              |

> *Dictionaries are ordered as of Python 3.7, but access by key — not by position.*

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

> ✅ **Key Point**: Lists are ordered, changeable, and best for sequences.

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

> ✅ **Key Point**: Use dictionaries to link keys to values.

---

## 📦 Tuples

### Creating & Accessing
```python
coordinates = (100, 250)
rgb_color = (255, 0, 0)
x = coordinates[0]
```

### What You CAN'T Do
```python
coordinates[0] = 150      # ❌ TypeError
coordinates.append(50)    # ❌ AttributeError
del coordinates[0]        # ❌ TypeError
```

> ✅ **Key Point**: Tuples are immutable — ideal for fixed data.

---

## ✨ Sets

### Creating & Using
```python
tags = ["python", "code", "fun", "python", "guide"]
unique_tags = set(tags)
```

### Membership Test
```python
"python" in unique_tags  # True
"java" in unique_tags    # False
```

> ✅ **Key Point**: Sets store unique items and are great for membership checks.

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

**Choose the Right Tool:**
- ✅ **List**: Ordered and editable
- ✅ **Dictionary**: Key-value mapping
- ✅ **Tuple**: Ordered and fixed
- ✅ **Set**: Unique, unordered

**Nested Structures**
```python
players = [
    {"name": "Alice", "level": 10},
    {"name": "Bob", "level": 8}
]
print(players[0]["name"])  # "Alice"
```

**Safe Key Access**
```python
if "mana" in player_stats:
    print(player_stats["mana"])
else:
    print("This player has no mana.")
```

---

## 🎯 Common Mistakes to Avoid

### ❌ Accessing Dictionary by Index
```python
# Wrong
player_stats[0]  # KeyError

# Correct
player_stats["name"]
```

### ❌ Missing Quotes in Keys
```python
# Wrong
stats = {name: "Alex"}  # NameError

# Correct
stats = {"name": "Alex"}
```

### ❌ Trying to Modify a Tuple
```python
# Wrong
my_tuple = (1, 2, 3)
my_tuple[0] = 99  # TypeError

# Correct
my_list = list(my_tuple)
my_list[0] = 99
my_tuple = tuple(my_list)
```

---

**Happy coding!** 🐍✨
