# ==========================================
# SECTION 2: Modifying Attributes
# ==========================================

print("SECTION 2: Modifying Attributes")
print("-" * 30)

# You can change an object's attributes directly.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # An attribute with a default value

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    # A method to update an attribute's value
    def update_odometer(self, mileage):
        # Add some logic to prevent rolling back the odometer
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_car = Car("Toyota", "Camry", 2022)
print(my_car.get_description())
my_car.read_odometer()

# Modifying an attribute's value directly
print("\nUpdating odometer directly...")
my_car.odometer_reading = 100
my_car.read_odometer()

# Modifying an attribute's value through a method
print("\nUpdating odometer with a method...")
my_car.update_odometer(150)
my_car.read_odometer()

print("\nTrying to roll back the odometer...")
my_car.update_odometer(120) # This should fail
my_car.read_odometer()

print("\n" + "="*50)

# YOUR CODE HERE - Create a 'Book' class.
# 1. Define a class called `Book`.
# 2. In the `__init__` method, it should take `title`, `author`, and `pages` as parameters.
#    Assign these to attributes on the object.
# 3. Create a method called `get_info()` that prints a sentence like:
#    "[TITLE] by [AUTHOR] is [PAGES] pages long."
# 4. Create two different Book objects from your class.
# 5. Call the `get_info()` method on both of your book objects.
# YOUR CODE HERE:



print("\n" + "="*50)
