# ==========================================
# SECTION 2: Day 9 Project - Running the Simulation
# ==========================================

print("SECTION 2: Running the Simulation")
print("-" * 35)

# Now we use our Pet class to create an interactive game loop.

# --- Create a Pet Object ---
pet_name = input("What will you name your pet? ")
pet_type = input(f"What kind of animal is {pet_name}? ")

my_pet = Pet(pet_name, pet_type)
print(f"\nWelcome, {my_pet.name} the {my_pet.animal_type}!")


# --- The Main Game Loop ---
while True:
    my_pet.show_stats()
    
    print("\nWhat would you like to do?")
    print("1. Feed")
    print("2. Play")
    print("3. Put to sleep")
    print("4. Wake up")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        my_pet.feed()
    elif choice == "2":
        my_pet.play()
    elif choice == "3":
        my_pet.sleep()
    elif choice == "4":
        my_pet.wake_up()
    elif choice == "5":
        print(f"Goodbye! Take care of {my_pet.name}!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

print("\n" + "="*50)
# print("Congratulations on completing Day 9! You've built a complete, interactive program using OOP principles.")
