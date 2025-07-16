# 🐍 Python Day 6 Cheat Sheet
## Using Modules

---

## 📝 Table of Contents
1. [Core Definitions](#-core-definitions)
2. [The `random` Module](#-the-random-module)
3. [The `math` Module](#-the-math-module)
4. [The `datetime` and `time` Modules](#-the-datetime-and-time-modules)
5. [Ways to Import](#-ways-to-import)
6. [Quick Reference](#-quick-reference)
7. [Common Mistakes to Avoid](#-common-mistakes-to-avoid)

---

## 🧠 Core Definitions

* **Module:** A file containing Python code (functions, variables, classes) that can be imported and used in other Python files. It's like a toolbox for a specific job.
* **`import`:** The keyword used to bring a module's code into your current program so you can use it.
* **Library:** A collection of related modules. The "Python Standard Library" is the collection of modules that comes included with Python.

---

## 🎲 The `random` Module

You must `import random` before using these functions.

### `random.randint(a, b)`
Returns a random integer `N` such that `a <= N <= b`.
```python
import random
roll = random.randint(1, 6)
```

### `random.choice(sequence)`
Returns a single, random element from a sequence (like a list or tuple).
```python
import random
players = ["Alice", "Bob", "Charlie"]
winner = random.choice(players)
```

---

## 🧮 The `math` Module

You must `import math` before using these.

### `math.sqrt(x)`
Returns the square root of a number.
```python
import math
side_length = math.sqrt(144) # 12.0
```

### `math.pi`
A constant that holds the value of Pi (approx. 3.14159...).
```python
import math
circumference = 2 * math.pi * 5
```

---

## 🕒 The `datetime` and `time` Modules

### `datetime.datetime.now()`
Gets the current local date and time.
```python
import datetime
now = datetime.datetime.now()
print(now)
```

### `strftime()` (String Format Time)
Formats a datetime object into a readable string.
```python
# (continuing from above)
# %Y=Year, %m=month, %d=day, %H=Hour, %M=Minute, %S=Second
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)
```

### `time.sleep(seconds)`
Pauses the execution of your program for a given number of seconds.
```python
import time
print("Waiting...")
time.sleep(3) # Pauses for 3 seconds
print("Done waiting!")
```

---

## 📥 Ways to Import

### Method 1: `import module_name` (Most Common)
Imports the entire module. You must use the module name as a prefix.
```python
import random
roll = random.randint(1, 6)
```

### Method 2: `from module_name import function_name`
Imports a specific function directly. No prefix is needed.
```python
from random import choice
winner = choice(["Alice", "Bob"])
```

### Method 3: `import module_name as alias`
Imports a module and gives it a shorter nickname (alias).
```python
import math as m
circumference = 2 * m.pi * 5
```

---

## ⚡ Quick Reference

| Function/Constant | Module | Description |
| :--- | :--- | :--- |
| `randint(a, b)` | `random` | Random integer between `a` and `b`. |
| `choice(seq)` | `random` | Random item from a sequence. |
| `sqrt(x)` | `math` | Square root of `x`. |
| `pi` | `math` | The constant Pi. |
| `datetime.now()` | `datetime` | The current date and time. |
| `sleep(sec)` | `time` | Pause the program for `sec` seconds. |

---

## 🎯 Common Mistakes to Avoid

❌ **Forgetting to `import` the module.**
```python
# Wrong: This will cause a NameError because Python doesn't know 'random'.
roll = random.randint(1, 6)
```
✅ **Always `import` first.**
```python
# Correct
import random
roll = random.randint(1, 6)
```

❌ **Using the wrong prefix after `from...import`.**
```python
# Wrong: 'choice' was imported directly, so it has no prefix.
from random import choice
winner = random.choice(["Alice", "Bob"]) # NameError: name 'random' is not defined
```
✅ **Call the function directly.**
```python
# Correct
from random import choice
winner = choice(["Alice", "Bob"])
```

---

*Happy coding! 🐍✨*
