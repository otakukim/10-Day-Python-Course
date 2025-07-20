# ==========================================
# DAY 8: Introduction to Object-Oriented Programming (OOP)
# ==========================================

# print("Welcome to Day 8! Today, we're learning a new way to think about programming.")
# print("With Object-Oriented Programming, we can create our own custom data types!")
# print("\n" + "="*50)

# ==========================================
# SECTION 1: Classes and Objects - The Blueprint and the House
# ==========================================

print("SECTION 1: Classes and Objects")
print("-" * 30)

# A 'class' is like a blueprint. It defines the properties and behaviors that something can have.
# Here, we define a blueprint for a 'Dog'.
class Dog:
    # The __init__ method is a special function that runs when you create a new object.
    # It's called the "constructor". 'self' refers to the object being created.
    def __init__(self, name, breed, age):
        # These are called 'attributes'. They are variables that belong to the object.
        self.name = name
        self.breed = breed
        self.age = age
        print(f"A new dog named {self.name} has been created!")

    # This is a 'method'. It's a function that belongs to the object.
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# An 'object' is an instance of a class. It's the actual house built from the blueprint.
# Here, we are creating two different Dog objects from our Dog class.
dog1 = Dog("Fido", "Golden Retriever", 5)
dog2 = Dog("Lucy", "Poodle", 3)

# We can access the attributes of each object using dot notation.
print(f"\nDog 1's name is {dog1.name}.")
print(f"Dog 2 is a {dog2.breed} and is {dog2.age} years old.")

# We can also call the methods of each object.
print("\nLet's hear them bark:")
dog1.bark()
dog2.bark()

print("\n" + "="*50)
