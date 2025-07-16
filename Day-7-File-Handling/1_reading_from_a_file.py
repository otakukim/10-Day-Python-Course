# ==========================================
# DAY 7: Reading From and Writing to Files
# ==========================================

# print("Welcome to Day 7! Today, we'll learn how to make our programs remember information.")
# print("We'll do this by reading from and writing to text files!")
# print("\n" + "="*50)

# ==========================================
# SECTION 1: Reading From a File
# ==========================================

print("SECTION 1: Reading From a File")
print("-" * 30)

# First, let's create a sample file to read from.
# This code block writes a file named 'poem.txt'.
with open('poem.txt', 'w') as file:
    file.write("Roses are red,\n")
    file.write("Violets are blue,\n")
    file.write("Python is awesome,\n")
    file.write("And so are you!\n")

# Exercise 1.1: Reading an Entire File
# The 'with open(...) as ...' syntax is the standard way to handle files.
# It automatically closes the file for you when you're done.
print("Reading the entire file at once:")
with open('poem.txt', 'r') as file: # 'r' stands for 'read mode'
    contents = file.read()
    print(contents)

print("\n" + "="*50)

# Exercise 1.2: Looping Through a File's Lines
# You can read a file line by line, which is great for large files.
print("Reading the file line by line:")
with open('poem.txt', 'r') as file:
    for line in file:
        # The .strip() method removes any leading/trailing whitespace, including the newline character.
        print(line.strip())

print("\n" + "="*50)
