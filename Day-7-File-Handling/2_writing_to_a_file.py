# ==========================================
# SECTION 2: Writing to a File
# ==========================================

print("SECTION 2: Writing to a File")
print("-" * 28)

# Exercise 2.1: Writing to an Empty File
# 'w' mode (write mode) will create a file if it doesn't exist.
# WARNING: If the file DOES exist, 'w' mode will ERASE everything in it!
filename = 'programming.txt'
print(f"Writing to a new file named '{filename}'...")
with open(filename, 'w') as file:
    file.write("I love programming.\n")
    file.write("It's a lot of fun!\n")

print(f"'{filename}' has been created. Check your folder!")

# Let's read it back to confirm
with open(filename, 'r') as file:
    print("\nContents of programming.txt:")
    print(file.read())

print("\n" + "="*50)


# Exercise 2.2: Appending to a File
# If you don't want to erase a file, use 'a' mode (append mode).
# This adds your new content to the end of the file.
print(f"Appending to '{filename}'...")
with open(filename, 'a') as file:
    file.write("Python is my favorite language.\n")

# Let's read it again to see the new line
with open(filename, 'r') as file:
    print("\nContents of programming.txt after appending:")
    print(file.read())

print("\n" + "="*50)
