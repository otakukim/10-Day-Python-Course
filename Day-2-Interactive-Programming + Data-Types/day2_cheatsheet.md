# 🐍 Python Day 2 Cheat Sheet
## Interactive Programming & Data Types

---

## 📝 Table of Contents
1. [User Input](#-user-input)
2. [Data Types](#-data-types)
3. [If Statements](#-if-statements--decision-making)
4. [Type Conversion](#-type-conversion)
5. [User-Driven Programs](#-user-driven-programs)
6. [Quick Reference](#-quick-reference)

---

## 💬 User Input

### Basic Input
```python
# Getting user input (always returns a string)
name = input("What is your name? ")
age = input("How old are you? ")

# Responding to user
print("Hello,", name, "!")
print(f"Wow, {age} is a great age!")
```

### Multi-Question Programs
```python
# Interactive survey example
movie = input("What's your favorite movie? ")
food = input("What's your favorite food? ")

print(f"""
🌟 Your Profile 🌟
━━━━━━━━━━━━━━━━━━━━━
🎬 Movie: {movie}
🍕 Food: {food}
━━━━━━━━━━━━━━━━━━━━━
""")
```

**Key Points:**
- `input()` always returns a **string**
- Use f-strings `f"text {variable}"` for formatting
- Use `"""` for multi-line strings

---

## 🔢 Data Types

### The Four Main Types
```python
# String (text)
text_data = "Hello World"
user_input = input("Enter something: ")  # Always string!

# Integer (whole numbers)
whole_number = 42
negative_number = -10

# Float (decimal numbers)
decimal_number = 3.14
price = 19.99

# Boolean (True/False)
is_student = True
is_raining = False
```

### Checking Types
```python
value = "25"
print(type(value))  # <class 'str'>

number = 25
print(type(number))  # <class 'int'>
```

### How Types Behave
```python
# String behaviors
"Hello" + " World"    # "Hello World" (concatenation)
"Hi! " * 3           # "Hi! Hi! Hi! " (repetition)
"5" + "3"            # "53" (not math!)

# Number behaviors  
5 + 3                # 8 (actual math)
10 * 2               # 20
```

---

## 🤔 If Statements & Decision Making

### Basic If Statements
```python
age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult!")

if age < 18:
    print("You are a minor.")
```

### Comparison Operators
```python
==    # Equal to
!=    # Not equal to
>     # Greater than
<     # Less than
>=    # Greater than or equal
<=    # Less than or equal
```

### If-Elif-Else Chains
```python
grade = int(input("Enter your grade: "))

if grade >= 90:
    print("Excellent! You got an A!")
elif grade >= 80:
    print("Great job! You got a B!")
elif grade >= 70:
    print("Good work! You got a C!")
elif grade >= 60:
    print("You passed with a D.")
else:
    print("You need to work harder.")
```

### Multiple Conditions
```python
temperature = int(input("Temperature: "))

if temperature > 80:
    print("It's hot! Wear light clothes.")
elif temperature > 60:
    print("Nice weather!")
elif temperature > 40:
    print("It's cool. Maybe a jacket?")
else:
    print("It's cold! Bundle up!")
```

---

## 🔄 Type Conversion

### String to Number
```python
# For whole numbers
age_string = input("Enter age: ")      # User types "25"
age_number = int(age_string)           # Convert to 25
# Or in one line:
age = int(input("Enter age: "))

# For decimal numbers
price_string = input("Enter price: ")  # User types "19.99"
price_number = float(price_string)     # Convert to 19.99
# Or in one line:
price = float(input("Enter price: "))
```

### Calculator Example
```python
# Simple calculator
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} × {num2} = {multiplication}")
```

### Working with Decimals
```python
# Financial calculator
price = float(input("Enter price: $"))
tax_rate = float(input("Tax rate (like 0.08): "))

tax_amount = price * tax_rate
total = price + tax_amount

print(f"Price: ${price:.2f}")           # .2f shows 2 decimal places
print(f"Tax: ${tax_amount:.2f}")
print(f"Total: ${total:.2f}")
```

---

## 👤 User-Driven Programs

### Personalized Responses
```python
name = input("What's your name? ")
time_of_day = input("Morning, afternoon, or evening? ")

# Make input case-insensitive
time_response = time_of_day.lower()

if "morning" in time_response:
    print(f"Good morning, {name}!")
    print("Hope you have a great start!")
elif "afternoon" in time_response:
    print(f"Good afternoon, {name}!")
    print("Hope your day is going well!")
elif "evening" in time_response:
    print(f"Good evening, {name}!")
    print("Hope you have a restful evening!")
else:
    print(f"Hello, {name}!")
```

### Dynamic Content Generation
```python
# Story generator
character = input("Character name: ")
age = int(input("Character age: "))
setting = input("Setting: ")
magic_item = input("Magic item found: ")

# Age-appropriate content
if age < 12:
    adventure = "went on a fun adventure"
    challenge = "solve a friendly puzzle"
elif age < 18:
    adventure = "embarked on an exciting quest"
    challenge = "overcome a challenging obstacle"
else:
    adventure = "began a dangerous mission"
    challenge = "face a formidable enemy"

# Generate story
story = f"""
🌟 The Adventure of {character} 🌟

{character}, age {age}, {adventure} in a {setting}.
They discovered a mysterious {magic_item}!

Their mission: {challenge} using the {magic_item}.
"""

print(story)
```

### Smart Input Handling
```python
# Handling different user responses
favorite_color = input("Favorite color: ").lower().strip()

if favorite_color in ["blue", "navy", "azure"]:
    print("Blue is calming and peaceful!")
elif favorite_color in ["red", "crimson", "scarlet"]:
    print("Red is bold and energetic!")
elif favorite_color in ["green", "emerald", "forest"]:
    print("Green represents nature and growth!")
else:
    print(f"{favorite_color.title()} is a great choice!")
```

---

## ⚡ Quick Reference

### Essential Functions
```python
input("prompt")          # Get user input (returns string)
print("message")         # Display output
int("25")               # Convert to integer
float("25.5")           # Convert to decimal
type(variable)          # Check data type
len("text")             # Get length of string
```

### String Methods
```python
text.lower()            # Convert to lowercase
text.upper()            # Convert to uppercase
text.strip()            # Remove spaces from ends
text.title()            # Capitalize Each Word
"word" in text          # Check if word is in text
```

### Common Patterns
```python
# Safe number input
age = int(input("Age: "))

# Formatted output
print(f"Hello {name}, you are {age} years old")

# Multi-choice decision
if condition1:
    # do something
elif condition2:
    # do something else
else:
    # default action

# Case-insensitive input
response = input("Yes or no? ").lower()
if response in ["yes", "y", "yeah"]:
    print("Great!")
```

### Format Specifiers
```python
price = 19.99
print(f"${price:.2f}")     # $19.99 (2 decimal places)

percentage = 0.856
print(f"{percentage:.1%}") # 85.6% (1 decimal as percent)
```

---

## 💡 Pro Tips

1. **Always convert input to numbers** when doing math: `int(input())` or `float(input())`

2. **Use `.lower()` for user input** to handle different cases: `response.lower()`

3. **Use f-strings for clean output**: `f"Hello {name}!"` instead of `"Hello " + name + "!"`

4. **Chain elif statements** instead of multiple separate if statements for related conditions

5. **Use meaningful variable names**: `user_age` instead of `x`

6. **Test edge cases**: What happens if user enters 0? Negative numbers? Empty input?

---

## 🎯 Common Mistakes to Avoid

❌ **Trying to do math with strings**
```python
# Wrong
num1 = input("Number: ")    # This is a string!
num2 = input("Number: ")    # This is a string!
result = num1 + num2        # This concatenates: "5" + "3" = "53"
```

✅ **Convert to numbers first**
```python
# Correct
num1 = int(input("Number: "))
num2 = int(input("Number: "))
result = num1 + num2        # This adds: 5 + 3 = 8
```

❌ **Case-sensitive comparisons**
```python
# Problem: user might type "YES", "yes", "Yes"
response = input("Continue? ")
if response == "yes":       # Only matches exact lowercase
```

✅ **Make it case-insensitive**
```python
response = input("Continue? ").lower()
if response in ["yes", "y", "yeah"]:
```

---

*Happy coding! 🐍✨*
