# Exercise 1.3: Drawing a Shape with a Loop
# Since turtle graphics don't work in all online IDEs, let's draw with text!
# We can use a loop to print a square made of asterisks.
print("\n🎨 Drawing a square with a for loop:")

size = 5
# The top border
print("*" * size)

# The middle part: loop `size - 2` times for the inner rows
for _ in range(size - 2):
    # Print a star, then spaces, then a star
    print("*" + " " * (size - 2) + "*")

# The bottom border (only if size > 1)
if size > 1:
    print("*" * size)

print("Square drawing complete!")


print("\n" + "="*50)
