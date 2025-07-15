# ==========================================
# SECTION 3: The 'datetime' and 'time' Modules
# ==========================================

print("SECTION 3: The 'datetime' and 'time' Modules")
print("-" * 42)

# Exercise 3.1: Getting the Current Date and Time
import datetime

now = datetime.datetime.now()
print(f"Current date and time: {now}")

# You can format the date and time to be more readable with strftime()
# %Y = full year, %m = month, %d = day, %H = hour, %M = minute, %S = second
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted time: {formatted_time}")

print("\n" + "="*50)

# Exercise 3.2: YOUR CODE HERE - Print the current year.
# 1. Get the current datetime object like in the example above.
# 2. The datetime object has an attribute called .year. Access it.
# 3. Print a message like "We are in the year [YEAR]."
# YOUR CODE HERE:



print("\n" + "="*50)
