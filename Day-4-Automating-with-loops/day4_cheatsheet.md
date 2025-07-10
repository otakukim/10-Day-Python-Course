# 🐍 Python Day 4 Cheat Sheet
## Automating with Loops

---

## 📝 Table of Contents
1. [Core Definitions](#-core-definitions)
2. [Key Differences: `for` vs `while`](#-key-differences-for-vs-while)
3. [The `for` Loop](#-the-for-loop)
4. [The `while` Loop](#-the-while-loop)
5. [Loop Control Statements](#-loop-control-statements)
6. [Quick Reference](#-quick-reference)
7. [Pro Tips](#-pro-tips)
8. [Common Mistakes to Avoid](#-common-mistakes-to-avoid)

---

## 🧠 Core Definitions

* **Iteration:** The process of repeating a set of instructions. Each time the instructions are executed is called one "iteration".
* **`for` Loop:** A loop that iterates over a **sequence** (like a list, dictionary, tuple, or string) or other iterable objects. It runs once for each item in the sequence.
* **`while` Loop:** A loop that continues to execute as long as a certain **condition** remains `True`.
* **`break`:** A keyword that immediately **terminates** the current loop, and the program continues at the next statement after the loop.
* **`continue`:** A keyword that **skips** the rest of the code inside the current iteration of the loop and proceeds to the next iteration.

---

## 📊 Key Differences: `for` vs `while`

| Feature | `for` Loop | `while` Loop |
| :--- | :--- | :--- |
| **Best For** | Iterating over a known sequence | Looping as long as a condition is true |
| **Typical Use** | "For each item in this list..." | "Keep doing this until..." |
| **Structure** | `for item in sequence:` | `while condition:` |
| **Infinite Loop Risk** | Low (stops when sequence ends) | **High** (if condition never becomes false) |

---

## 🗂️ The `for` Loop

### Looping Over a List
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like to eat {fruit}s.")
```

### Looping with `range()`
```python
# Loop 5 times (0 to 4)
for i in range(5):
    print(f"Loop number {i}")

# Loop from 2 up to (but not including) 6
for i in range(2, 6):
    print(f"Number: {i}")
```

### Drawing with Text
```python
# Drawing a 5x5 square
size = 5
for i in range(size):
    # For the first or last row, print a full line
    if i == 0 or i == size - 1:
        print("*" * size)
    # For middle rows, print a star, spaces, and a star
    else:
        print("*" + " " * (size - 2) + "*")
```

### Looping Over a Dictionary
```python
player_stats = {"name": "Alex", "level": 5}

# Using .items() to get key and value directly
for key, value in player_stats.items():
    print(f"{key}: {value}")
```

---

## 🔄 The `while` Loop

### Basic Counter Loop
```python
# Prints numbers 1 through 5
count = 1
while count <= 5:
    print(count)
    count = count + 1 # Crucial! This prevents an infinite loop.
```

### Creative Patterns
```python
# Drawing a growing triangle
lines = 1
while lines <= 7:
    print("*" * lines)
    lines += 1 # Shortcut for lines = lines + 1
```

### Interactive Loop (e.g., a Menu)
```python
command = ""
while command.lower() != "exit":
    command = input("Enter command (or 'exit'): ")
    print(f"Executing: {command}")
```

---

## 🛑 Loop Control Statements

### `break` (Exit the Loop)
Use `break` to exit a loop immediately, regardless of the loop's condition.
```python
# Find the first person named "Bob" and then stop.
names = ["Alice", "Charlie", "Bob", "David"]
for name in names:
    print(f"Checking {name}...")
    if name == "Bob":
        print("Found Bob!")
        break # Exit the loop now
```

### `continue` (Skip to Next Iteration)
Use `continue` to skip the current iteration and move to the next one.
```python
# Print all numbers from 0 to 9, but skip 5.
for i in range(10):
    if i == 5:
        continue # Skip the rest of this iteration
    print(i)
```

---

## ⚡ Quick Reference

### `for` Loop Patterns
```python
# Over a list
for item in my_list:
    # do something with item

# For a specific number of times
for i in range(10):
    # do something 10 times

# With index and item
for index, item in enumerate(my_list):
    print(f"Index {index}: {item}")
```

### `while` Loop Patterns
```python
# Counter-based
i = 0
while i < 10:
    # do something
    i += 1 # Shortcut for i = i + 1

# User-input based (infinite loop with a break condition)
while True:
    response = input("Continue? (y/n): ")
    if response.lower() == 'n':
        break # Exit condition
```

---

## 💡 Pro Tips

1.  **`for` loops are for `for each`:** If you can phrase your problem as "for each item in my collection...", a `for` loop is almost always the right choice. It's safer and often more readable.

2.  **`while` loops are for `until`:** If you can phrase your problem as "keep doing this until some condition changes...", a `while` loop is what you need. Perfect for games, menus, and waiting for events.

3.  **Combine Loops and `if`:** The real power comes when you put `if` statements inside your loops to make decisions on each iteration.

4.  **Use `enumerate()` for Indexes:** When you need both the index and the item from a list, `enumerate()` is cleaner than managing your own counter.

---

## 🎯 Common Mistakes to Avoid

❌ **Creating an Infinite `while` Loop**
```python
# Wrong: The condition `i < 5` never becomes false!
i = 0
while i < 5:
    print("This will never stop!")
# You forgot to increment i!
```
✅ **Always Update the Condition Variable**
```python
# Correct
i = 0
while i < 5:
    print(i)
    i += 1 # The variable is updated, so the loop will end.
```

❌ **Forgetting to Convert `input()` to a Number**
```python
# Wrong: 'guess' will be a string, so guess != 7 will always be true!
secret_number = 7
guess = ""
while guess != secret_number:
    guess = input("Guess the number: ") # guess is "7", not 7
```
✅ **Convert Input for Comparison**
```python
# Correct
secret_number = 7
guess = 0
while guess != secret_number:
    guess = int(input("Guess the number: ")) # Converts to integer
```

❌ **Modifying a List While Looping Over It**
```python
# This can cause unexpected behavior and skipped items.
numbers = [1, 2, 3, 4]
for number in numbers:
    if number % 2 == 0:
        numbers.remove(number) # DANGEROUS!
```
✅ **Loop Over a Copy**
```python
# Correct: Loop over a copy to safely modify the original
for number in numbers[:]: # The [:] creates a copy
    if number % 2 == 0:
        numbers.remove(number)
```

---

*Happy coding! 🐍✨*
