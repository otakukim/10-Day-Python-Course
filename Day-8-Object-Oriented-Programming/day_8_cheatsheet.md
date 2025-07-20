# 🐍 Python Day 8 Cheat Sheet
## Introduction to Object-Oriented Programming (OOP)

---

## 📝 Table of Contents
1. [Core Definitions](#-core-definitions)
2. [Class Syntax](#-class-syntax)
3. [Creating and Using Objects](#-creating-and-using-objects)
4. [Quick Reference](#-quick-reference)
5. [Common Mistakes to Avoid](#-common-mistakes-to-avoid)

---

## 🧠 Core Definitions

* **Class:** A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
* **Object (or Instance):** A specific item created from a class. If `Dog` is the class, a specific dog named Fido is an object.
* **Attribute:** A variable that belongs to an object. It represents a piece of data about the object (e.g., `dog.name`, `dog.age`).
* **Method:** A function that belongs to an object. It represents an action the object can perform (e.g., `dog.bark()`).
* **`__init__()`:** A special method called the "constructor". It runs automatically when a new object is created and is used to set up the object's initial attributes.
* **`self`:** A special parameter that must be the first parameter of every method in a class. It refers to the object instance itself, giving the method access to the object's attributes and other methods.

---

## 🏛️ Class Syntax

### Defining a Simple Class
The basic structure of a class with an `__init__` method and another method.
```python
# Class names are typically written in PascalCase (first letter of each word capitalized).
class Dog:
    # The constructor method to initialize the object's attributes.
    def __init__(self, name, age):
        # 'self' refers to the instance being created.
        # These are the attributes.
        self.name = name
        self.age = age

    # This is a method. It's a function that belongs to the class.
    # It must have 'self' as its first parameter.
    def bark(self):
        print(f"{self.name} says: Woof!")
```

### Attributes with Default Values
You can set a default value for an attribute directly in the `__init__` method.
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        # This attribute has a default value and doesn't need a parameter.
        self.odometer_reading = 0
```

---

## 📦 Creating and Using Objects

### Creating an Object (Instantiation)
To create an object, you call the class name as if it were a function, providing arguments for the `__init__` parameters.
```python
# Create two separate Dog objects from the Dog class blueprint.
my_dog = Dog("Fido", 5)
your_dog = Dog("Lucy", 3)
```

### Accessing Attributes
Use dot notation (`.`) to get the value of an object's attribute.
```python
print(f"My dog's name is {my_dog.name}.") # My dog's name is Fido.
print(f"Your dog is {your_dog.age} years old.") # Your dog is 3 years old.
```

### Modifying Attributes
You can change an attribute's value directly.
```python
my_dog.age = 6
print(f"My dog is now {my_dog.age} years old.") # My dog is now 6 years old.
```

### Calling Methods
Use dot notation with parentheses to call an object's method.
```python
my_dog.bark() # Fido says: Woof!
your_dog.bark() # Lucy says: Woof!
```

---

## ⚡ Quick Reference

| Term | Syntax | Description |
| :--- | :--- | :--- |
| **Class Definition** | `class ClassName:` | The blueprint for your objects. |
| **Constructor** | `def __init__(self, p1, p2):` | Special method to set up new objects. |
| **Attribute** | `self.attribute = value` | A variable that belongs to the object. |
| **Method** | `def method_name(self, p1):` | A function that belongs to the object. |
| **Object Creation** | `my_object = ClassName(a1, a2)` | Creating an instance of a class. |
| **Access Attribute** | `my_object.attribute` | Get the value of an attribute. |
| **Call Method** | `my_object.method_name(a1)` | Execute a method. |

---

## 🎯 Common Mistakes to Avoid

❌ **Forgetting `self` as the first parameter in a method.**
```python
class Player:
    # Wrong: bark() is missing 'self'.
    def bark(name): # This will cause a TypeError when called.
        print(f"{name} barks.")
```
✅ **Always include `self` as the first parameter.**
```python
class Player:
    # Correct
    def bark(self, name):
        print(f"{name} barks.")
```

❌ **Forgetting to use `self.` to access attributes inside a method.**
```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    # Wrong: 'name' is not defined here. It should be 'self.name'.
    def greet(self):
        print(f"Hello, my name is {name}.") # NameError
```
✅ **Always use `self.` to access the object's own attributes.**
```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    # Correct
    def greet(self):
        print(f"Hello, my name is {self.name}.")
```

---

*Happy coding! 🐍✨*
