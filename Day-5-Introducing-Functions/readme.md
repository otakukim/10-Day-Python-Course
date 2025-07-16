# ➡️ Day 5: Introducing Functions

Day 5 was a huge step forward! We learned how to package our code into reusable blocks called **functions**. This is the most important organizational tool in programming and helps us write cleaner, more efficient code by following the "Don't Repeat Yourself" (DRY) principle.

* **Full Script:** [`day_5_script.py`](./day_5_script.py)
* **Cheat Sheet:** [`day_5_cheatsheet.md`](./day_5_cheatsheet.md)

---

### ⭐ Key Concepts Covered:

* **Defining and Calling:** Using the `def` keyword to create a function and calling it by its name to execute the code.
* **Parameters and Arguments:** Passing information *into* a function to make it more flexible.
* **`return` Values:** Getting a result *back from* a function so the rest of our program can use it.
* **Local Scope:** Understanding that variables created inside a function only exist within that function.
* **Advanced Concepts:** Using helper functions to break down problems and a brief introduction to recursion (a function calling itself).

---

### 💡 Highlight Snippet:

```python
# A function that takes two numbers and returns their sum
def add(a, b):
    return a + b

# The main part of the program calls the function and uses its return value
num1 = 10
num2 = 5
sum_result = add(num1, num2) # The returned value (15) is stored here

print(f"The sum is: {sum_result}")
