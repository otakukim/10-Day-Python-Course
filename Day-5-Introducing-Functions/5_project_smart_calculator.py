# ==========================================
# SECTION 5: Day 5 Project - The Smart Calculator
# ==========================================

print("SECTION 5: Day 5 Project - The Smart Calculator")
print("-" * 50)

# This project uses functions to create a clean and organized calculator.

# --- Function Definitions ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    else:
        return a / b

# --- Main Program Loop ---
while True:
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == "1":
            print(f"Result: {add(num1, num2)}")
        elif choice == "2":
            print(f"Result: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {multiply(num1, num2)}")
        elif choice == "4":
            print(f"Result: {divide(num1, num2)}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

print("\n" + "="*50)
# print("Congratulations on completing Day 5! You can now write clean, reusable code with functions.")
