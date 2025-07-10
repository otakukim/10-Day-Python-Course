# ==========================================
# SECTION 4: Day 4 Project - The Interactive Menu
# ==========================================

print("SECTION 4: Day 4 Project - The Interactive Menu")
print("-" * 50)

# This project combines while loops, for loops, lists, and if/elif/else.

shopping_list = []

while True: # This creates an infinite loop that we must 'break' out of.
    print("\n--- Shopping List Menu ---")
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item_to_add = input("What item do you want to add? ")
        shopping_list.append(item_to_add)
        print(f"'{item_to_add}' has been added!")

    elif choice == "2":
        print("\n--- Your Shopping List ---")
        if not shopping_list: # A quick way to check if a list is empty
            print("Your list is empty.")
        else:
            # Here we use a 'for' loop inside our 'while' loop!
            for item in shopping_list:
                print(f"- {item}")
        print("--------------------------")

    elif choice == "3":
        item_to_remove = input("What item would you like to remove? ")
        if item_to_remove in shopping_list:
            shopping_list.remove(item_to_remove)
            print(f"Successfully removed '{item_to_remove}'.")
        else:
            print(f"Sorry, '{item_to_remove}' is not in your list.")

    elif choice == "4":
        print("Goodbye!")
        break # This keyword immediately exits the current loop.

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

print("\n" + "="*50)
# print("Congratulations on completing Day 4! You can now automate tasks and build interactive programs with loops.")
