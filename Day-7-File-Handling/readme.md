# ➡️ Day 7: Reading From and Writing to Files

Day 7 gave our programs a memory! We learned about **File I/O (Input/Output)**, which allows our programs to save data to files and read it back later. This is how applications remember information even after they are closed.

* **Full Script:** [`day_7_script.py`](./day_7_script.py)
* **Cheat Sheet:** [`day_7_cheatsheet.md`](./day_7_cheatsheet.md)

---

### ⭐ Key Concepts Covered:

* **The `with open()` Statement:** The standard, safe way to open and automatically close files.
* **File Modes:** Understanding the difference between `'r'` (read), `'w'` (write, which erases), and `'a'` (append).
* **Reading Files:** Using `.read()`, `.readlines()`, and looping line-by-line.
* **Writing Files:** Using `.write()` to save strings to a file.
* **The `os` Module:** Using `os.path.exists()` to safely check if a file exists before trying to open it.

---

### 💡 Highlight Snippet:

```python
# A safe way to append a new high score to a file
new_score = "Player 1: 500\n"

# 'a' mode creates the file if it doesn't exist, or adds to the end if it does.
with open('scores.txt', 'a') as file:
    file.write(new_score)

print("Score saved successfully!")
