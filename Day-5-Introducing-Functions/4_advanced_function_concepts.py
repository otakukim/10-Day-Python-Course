# ==========================================
# SECTION 4: Advanced Function Concepts
# ==========================================

print("SECTION 4: Advanced Function Concepts")
print("-" * 35)

# Exercise 4.1: A Function Calling Another Function
# Functions can call other functions to help them do their job. This is great for breaking down complex problems.

def calculate_tax(price):
    """Calculates an 8% tax for a given price."""
    return price * 0.08

def calculate_final_price(price):
    """Calculates the final price by adding tax."""
    tax_amount = calculate_tax(price) # Calling our helper function
    final_price = price + tax_amount
    print(f"Price: ${price:.2f}, Tax: ${tax_amount:.2f}, Total: ${final_price:.2f}")

print("Calculating final price for a $50 item:")
calculate_final_price(50)

print("\n" + "="*50)

# Exercise 4.2: A Function Calling Itself (Recursion)
# This is an advanced topic, but cool to see! Recursion is when a function calls itself.
# It MUST have a "base case" to know when to stop, otherwise it creates an infinite loop.

def countdown(number):
    # BASE CASE: If the number is zero or less, stop.
    if number <= 0:
        print("Blast off! 🚀")
        return # This stops the function

    # RECURSIVE STEP: Print the number, then call itself with a smaller number.
    print(number)
    countdown(number - 1)

print("Starting a recursive countdown from 3:")
countdown(3)

print("\n" + "="*50)
