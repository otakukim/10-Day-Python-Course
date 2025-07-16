# 🐍 Python Day 7 Cheat Sheet
## Reading From and Writing to Files

---

## 📝 Table of Contents
1. [Core Definitions](#-core-definitions)
2. [The `with open()` Statement](#-the-with-open-statement)
3. [Reading from Files](#-reading-from-files)
4. [Writing to Files](#-writing-to-files)
5. [The `os` Module for Files](#-the-os-module-for-files)
6. [Quick Reference: File Modes](#-quick-reference-file-modes)
7. [Common Mistakes to Avoid](#-common-mistakes-to-avoid)

---

## 🧠 Core Definitions

* **File Path:** A string that specifies the location of a file (e.g., `'data/my_file.txt'` or just `'my_file.txt'` if it's in the same directory).
* **File Object:** The object that Python creates when you `open()` a file. You use this object's methods (like `.read()` or `.write()`) to interact with the file.
* **File Mode:** A character that tells Python how you want to open the file (`'r'` for read, `'w'` for write, `'a'` for append).

---

## ✅ The `with open()` Statement

This is the **recommended** way to work with files. It automatically handles closing the file, even if errors occur.

### Syntax
```python
with open('my_file.txt', 'r') as file_object:
    # Indented code that works with the file_object goes here.
    contents = file_object.read()

# The file is automatically closed when the 'with' block is exited.
print(contents)
```

---

## 📖 Reading from Files

### Reading an Entire File (`.read()`)
Reads the entire content of the file into a single string. Best for small files.
```python
with open('poem.txt', 'r') as file:
    all_contents = file.read()
```

### Reading Line by Line (Looping)
This is the most common and memory-efficient way to read a file.
```python
with open('data.txt', 'r') as file:
    for line in file:
        # .strip() removes leading/trailing whitespace, including the newline character
        print(line.strip())
```

### Reading into a List of Lines (`.readlines()`)
Reads the entire file into a list of strings, where each string is a line.
```python
with open('data.txt', 'r') as file:
    lines_list = file.readlines()

# lines_list is now ['First line\n', 'Second line\n', ...]
```

---

## ✍️ Writing to Files

### Writing to a File (`'w'` mode)
Opens a file for writing. **Creates the file if it doesn't exist. If it does exist, it ERASES all existing content.**
```python
# This will overwrite 'greetings.txt' or create it.
with open('greetings.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")
```

### Appending to a File (`'a'` mode)
Opens a file for appending. **Creates the file if it doesn't exist. If it exists, it adds new content to the END of the file.**
```python
# This will add text to the end of 'greetings.txt' without erasing it.
with open('greetings.txt', 'a') as file:
    file.write("Adding one more line.\n")
```

---

## ⚙️ The `os` Module for Files

You must `import os` before using these functions.

### `os.path.exists(filepath)`
Checks if a file or directory exists at the given path. Returns `True` or `False`.
```python
import os

if os.path.exists('my_data.txt'):
    print("File found!")
else:
    print("File not found.")
```

### `os.remove(filepath)`
Deletes a file. This will cause an error if the file doesn't exist.
```python
import os

if os.path.exists('file_to_delete.txt'):
    os.remove('file_to_delete.txt')
    print("File deleted.")
```

---

## ⚡ Quick Reference: File Modes

| Mode | Character | Description |
| :--: | :--- | :--- |
| **Read** | `'r'` | Opens a file for reading. **Error** if the file does not exist. (Default mode) |
| **Write** | `'w'` | Opens a file for writing. **Creates** a new file or **erases** an existing file. |
| **Append**| `'a'` | Opens a file for appending. **Creates** a new file or adds to the end of an existing file. |
| **Read/Write**| `'+'` | Can be added to other modes (e.g., `'r+'`) to allow both reading and writing. |

---

## 🎯 Common Mistakes to Avoid

❌ **Forgetting the Newline Character (`\n`)**
```python
# Wrong: This will write "HelloWorld" on one line.
with open('test.txt', 'w') as f:
    f.write("Hello")
    f.write("World")
```
✅ **Add `\n` When You Want a New Line**
```python
# Correct
with open('test.txt', 'w') as f:
    f.write("Hello\n")
    f.write("World\n")
```

❌ **Assuming a File Exists**
```python
# Wrong: This will crash with a FileNotFoundError if 'scores.txt' doesn't exist.
with open('scores.txt', 'r') as f:
    print(f.read())
```
✅ **Handle Potential Errors with `try...except` or `os.path.exists()`**
```python
# Correct (Option 1: try...except)
try:
    with open('scores.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("The scores file could not be found.")

# Correct (Option 2: os.path.exists)
import os
if os.path.exists('scores.txt'):
    with open('scores.txt', 'r') as f:
        print(f.read())
else:
    print("The scores file could not be found.")
```

---

*Happy coding! 🐍✨*
