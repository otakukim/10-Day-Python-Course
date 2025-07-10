# ➡️ Day 2: Interactive Python & Data Types

On Day 2, we moved from simple `print` statements to creating programs that can have a conversation with the user. We learned how Python handles different kinds of data and how to make programs that can make decisions.

* **Full Script:** [`day_2_script.py`](./day_2_script.py)
* **Cheat Sheet:** [`day_2_cheatsheet.md`](./day_2_cheatsheet.md)

---

### ⭐ Key Concepts Covered:

* **Getting user input with `input()`:** How to pause the program and wait for the user to type something.
* **Understanding data types:** Learning the difference between `string`, `int`, `float`, and `bool`.
* **Making decisions with `if`, `elif`, and `else`:** Giving our programs the ability to choose what to do next.
* **Converting between data types with `int()` and `float()`:** Turning user input (text) into numbers for calculations.

---

### 💡 Highlight Snippet:

```python
# A simple grade calculator combining input, type conversion, and if/elif/else
grade = int(input("Enter your percentage grade: "))

if grade >= 90:
    print("Excellent! You got an A!")
elif grade >= 80:
    print("Great job! You got a B!")
else:
    print("Keep practicing!")
