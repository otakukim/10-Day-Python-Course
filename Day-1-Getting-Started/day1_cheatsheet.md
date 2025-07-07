# 🐍 Python Day 1 Cheat Sheet
## Print Statements & Variables

---

## 📝 Table of Contents
1. [Basic Print Statements](#-basic-print-statements)
2. [Single vs Double Quotes](#-single-vs-double-quotes)
3. [Multi-line Printing](#-multi-line-printing)
4. [Variables - Information Storage](#-variables---information-storage)
5. [Quick Reference](#-quick-reference)

---

## 🖨️ Basic Print Statements

### Simple Print
```python
print("Hello, World!")
print("I am learning Python!")
print("This is awesome!")
```

### Print with Spacing
```python
print("My Information:")
print()  # Creates a blank line
print("Name: Alex")
print("Age: 16")
print()  # Another blank line
print("Thank you!")
```

### Special Characters & Emojis
```python
print("★ Special Characters ★")
print("→ Arrow pointing right")
print("♦ Diamond symbol")
print("🎉 Party emoji")
print("▓▓▓ Block characters")
```

**Key Points:**
- `print()` displays text on screen
- Empty `print()` creates blank lines
- Special characters and emojis make output fun!

---

## 📝 Single vs Double Quotes

### Both Work the Same
```python
print("This uses double quotes")
print('This uses single quotes')
```

### Smart Quote Choice
```python
# Use single quotes when text contains double quotes
print('My favorite movie is "The Lion King"')

# Use double quotes when text contains single quotes  
print("It's a beautiful day outside!")

# Mix and match for readability
print('She said "Hello!" to me')
print("I can't believe it's working!")
```

### Escaping Quotes with Backslash
```python
# When you need the same quote type inside
print("She said \"Hello!\" with a smile")
print('It\'s working perfectly!')

# Conversations with contractions
print("He said \"I can't do it!\"")
print('The teacher said \'Don\'t give up!\'')
```

**Quick Rule:**
- If your text has "double quotes" → use 'single quotes'
- If your text has 'single quotes' → use "double quotes"
- Use backslash `\` to escape same quote type

---

## 📋 Multi-line Printing

### Method 1: Multiple Print Statements
*Best for: Lists, structured information*
```python
print("My Daily Schedule:")
print("8:00 AM - Wake up")
print("9:00 AM - Breakfast") 
print("10:00 AM - Study Python")
print("12:00 PM - Lunch")
```

### Method 2: Newline Character (\n)
*Best for: Compact text with line breaks*
```python
print("Grocery List:\n🥛 Milk\n🍞 Bread\n🥚 Eggs")
print("Goals:\n✓ Learn Python\n✓ Practice coding\n✓ Have fun!")
```

### Method 3: Triple Quotes
*Best for: Stories, poems, long paragraphs*
```python
print('''Welcome to Python Programming!
This is a longer message that spans
multiple lines without needing \n
or multiple print statements.
Perfect for stories and poems!
Happy coding! 🐍''')
```

### When to Use Each Method

| Method | Best For | Example Use |
|--------|----------|-------------|
| Multiple `print()` | Lists, menus, schedules | Shopping lists, daily tasks |
| `\n` character | Compact formatting | Short lists, simple breaks |
| Triple quotes `'''` | Long text, stories | Poems, paragraphs, instructions |

---

## 📦 Variables - Information Storage

### Creating Basic Variables
```python
# Different types of information
name = "Alex"           # Text (string)
age = 16               # Number (integer)
height = 5.8           # Decimal (float)
is_student = True      # True/False (boolean)

# Using variables in print statements
print("My name is", name)
print("I am", age, "years old")
print("Height:", height, "feet")
print("Student status:", is_student)
```

### Variable Naming Rules
```python
# ✅ Good variable names
student_name = "Alice"
test_score = 95
favorite_color = "blue"

# ❌ Bad variable names (avoid these)
# 1student = "Bob"        # Can't start with number
# test-score = 85         # Can't use hyphens
# favorite color = "red"  # Can't have spaces
```

### Modifying Variables
```python
# Variables can change!
score = 0
print("Starting score:", score)

score = score + 10      # Add to score
print("After bonus:", score)

score = score * 2       # Double the score  
print("Final score:", score)

# Text variables can change too
status = "Beginner"
print("Current status:", status)

status = "Expert"
print("New status:", status)
```

### Variables in Calculations
```python
# Age calculation
birth_year = 2008
current_year = 2024
age = current_year - birth_year
print("You are", age, "years old")

# Temperature conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equals {fahrenheit}°F")

# Shopping total
item1_price = 12.99
item2_price = 8.50
tax = 2.15
total = item1_price + item2_price + tax
print(f"Total cost: ${total}")
```

### F-String Formatting (Modern Python)
```python
name = "Sarah"
age = 17
grade = 11

# Old way (still works)
print("Hi, my name is", name, "and I'm", age, "years old")

# New way (f-strings - preferred!)
print(f"Hi, my name is {name} and I'm {age} years old")
print(f"I'm in grade {grade}")

# With calculations
hours_studied = 5
print(f"I studied for {hours_studied} hours today!")
print(f"That's {hours_studied * 60} minutes!")
```

---

## ⚡ Quick Reference

### Essential Commands
```python
print("text")              # Display text
print()                    # Blank line
print("text", variable)    # Mix text and variables
print(f"text {variable}")  # F-string formatting
```

### Variable Operations
```python
# Create variables
name = "value"
number = 42

# Use in calculations  
result = number + 10
result = number * 2

# Update variables
score = 0
score = score + 5    # Add 5 to score
```

### Special Characters
```python
\n    # New line
\"    # Escape double quote
\'    # Escape single quote
\\    # Backslash character

# Common symbols: ★ → ♦ ● ◆ ▲ ▼ ✓ ✗ 
# Emojis: 🎯 🚀 💻 🐍 🎉 📚 ⭐
```

### String Formatting Options
```python
# Method 1: Comma separation
print("Hello", name, "you are", age)

# Method 2: F-strings (recommended)
print(f"Hello {name}, you are {age}")

# Method 3: Plus operator (text only)
print("Hello " + name + "!")
```

---

## 💡 Pro Tips

1. **Use descriptive variable names**: `student_grade` instead of `x`

2. **F-strings are your friend**: `f"Hello {name}!"` is cleaner than `"Hello " + name + "!"`

3. **Empty print() for spacing**: Use `print()` to make output more readable

4. **Choose quotes wisely**: Use the quote type that doesn't appear in your text

5. **Variables are containers**: Think of them as labeled boxes storing information

6. **Practice calculations**: Variables make math in programming powerful

---

## 🎯 Common Mistakes to Avoid

❌ **Forgetting quotes around text**
```python
# Wrong
print(Hello World)

# Correct  
print("Hello World")
```

❌ **Using reserved words as variables**
```python
# Wrong - 'print' is a Python command
print = "my name"

# Correct
name = "my name"
```

❌ **Mixing quote types incorrectly**
```python
# Wrong
print("Hello World')

# Correct
print("Hello World")
```

❌ **Trying to add text and numbers**
```python
# Wrong
print("I am " + 16 + " years old")

# Correct options
print("I am", 16, "years old")
print(f"I am {16} years old")
```

---

## 🏗️ Building Blocks Learned

By the end of Day 1, you can:
- ✅ Display any text or information with `print()`
- ✅ Format output nicely with spacing and special characters
- ✅ Handle quotes properly in your text
- ✅ Create multi-line output in three different ways
- ✅ Store information in variables
- ✅ Perform calculations with variables
- ✅ Update and modify stored information

**You're ready for Day 2: Interactive Programming! 🚀**

---

*Happy coding! 🐍✨*
