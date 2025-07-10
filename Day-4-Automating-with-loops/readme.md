# ➡️ Day 4: Automating with Loops

On Day 4, we learned how to make the computer do the repetitive work for us. Loops are the key to automation and are essential for working with the data collections we learned about on Day 3.

* **Cheat Sheet:** [`day_4_cheatsheet.md`](./day4_cheatsheet.md)

---

### ⭐ Key Concepts Covered:

* **`for` loops:** For iterating over a known sequence (e.g., every item in a list).
* **`while` loops:** For repeating as long as a condition is true.
* **`range()`:** For looping a specific number of times.
* **`break` & `continue`:** For controlling the flow of a loop.

---

### 💡 Highlight Snippet:

```python
# A common pattern: a 'while' loop for a menu and a 'for' loop to display data
shopping_list = ["apples", "bread", "milk"]

while True:
    print("\n1. View List | 2. Quit")
    choice = input("Enter choice: ")

    if choice == "1":
        print("\n--- Shopping List ---")
        for item in shopping_list:
            print(f"- {item}")
        print("---------------------")
    elif choice == "2":
        print("Goodbye!")
        break # Exit the infinite 'while' loop
