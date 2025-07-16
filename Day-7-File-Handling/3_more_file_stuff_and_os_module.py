# ==========================================
# SECTION 3: More File Concepts and the 'os' Module
# ==========================================
import os # The 'os' module lets us interact with the operating system.

print("SECTION 3: More File Concepts")
print("-" * 28)

# Exercise 3.1: Reading a File into a List
# The .readlines() method reads all lines into a list of strings.
print("Reading file contents into a list:")
with open('poem.txt', 'r') as file:
    lines = file.readlines()

print("The 'lines' variable is a list:")
print(lines)
# You can then access specific lines by index.
print(f"The second line is: {lines[1].strip()}")

print("\n" + "="*50)

# Exercise 3.2: Checking if a File Exists
# It's good practice to check if a file exists before trying to read it.
# os.path.exists() returns True or False.

file_to_check = 'poem.txt'
if os.path.exists(file_to_check):
    print(f"Success! The file '{file_to_check}' exists.")
else:
    print(f"Sorry, the file '{file_to_check}' does not exist.")

file_to_check = 'non_existent_file.txt'
if os.path.exists(file_to_check):
    print(f"Success! The file '{file_to_check}' exists.")
else:
    print(f"Sorry, the file '{file_to_check}' does not exist.")

print("\n" + "="*50)


# YOUR CODE HERE - Safely Read and Process a File
# 1. Create a variable `data_filename` with the value 'my_data.txt'.
# 2. First, check if `data_filename` exists using `os.path.exists()`.
# 3. If it exists, open it, read the contents, and print: "[FILENAME] exists. Contents: [CONTENTS]".
# 4. If it does NOT exist, create it in write mode ('w') and write the line "This is my new data file.\n".
#    Then print "[FILENAME] did not exist, so I created it."
# 5. Run your script TWICE. Observe how the output changes between the first and second run.
# YOUR CODE HERE:



print("\n" + "="*50)
