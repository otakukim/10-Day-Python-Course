# ==========================================
# DAY 9: OOP Project - Building an Interactive System
# ==========================================

# print("Welcome to Day 9! Today, we'll use our OOP skills to build a complete, interactive program.")
# print("We'll see how objects from classes can work together to create a fun simulation!")
# print("\n" + "="*50)

# ==========================================
# SECTION 1: The Pet Class - Our Project Blueprint
# ==========================================

print("SECTION 1: The Pet Class")
print("-" * 25)

# This project will be a "Mini Pet Simulator".
# First, we need a blueprint for our pet.

class Pet:
    """A class to represent a virtual pet."""
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        # Attributes with default values
        self.hunger = 50
        self.happiness = 50
        self.is_awake = True

    # The __str__ method is a special method that provides a user-friendly string
    # representation of the object. It's what runs when you try to print(my_object).
    def __str__(self):
        return f"Pet Name: {self.name} ({self.animal_type})"

    def feed(self):
        """Reduces hunger and slightly increases happiness."""
        if self.is_awake:
            print(f"You feed {self.name}. Yum!")
            self.hunger -= 10
            self.happiness += 5
            if self.hunger < 0: self.hunger = 0
        else:
            print(f"{self.name} is sleeping and cannot be fed.")

    def play(self):
        """Increases happiness and slightly increases hunger."""
        if self.is_awake:
            print(f"You play with {self.name}. It looks happy!")
            self.happiness += 15
            self.hunger += 5
            if self.happiness > 100: self.happiness = 100
        else:
            print(f"{self.name} is sleeping and cannot play right now.")

    def sleep(self):
        """Puts the pet to sleep."""
        self.is_awake = False
        print(f"{self.name} curls up and goes to sleep. Zzz...")

    def wake_up(self):
        """Wakes the pet up."""
        self.is_awake = True
        print(f"{self.name} wakes up and stretches!")

    def show_stats(self):
        """Displays the pet's current stats."""
        print(f"\n--- {self.name}'s Stats ---")
        print(f"Hunger: {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100")
        status = "Awake" if self.is_awake else "Sleeping"
        print(f"Status: {status}")
        print("--------------------")

print("The Pet class blueprint has been defined.")
print("\n" + "="*50)
