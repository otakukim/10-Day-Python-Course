# ==========================================
# SECTION 5: Day 3 Project - The User Profile
# ==========================================

print("SECTION 5: Day 3 Project - The User Profile")
print("-" * 45)

# This project uses a dictionary to build a user profile based on input.
# It combines everything we've learned about dictionaries and user input.

print("👤 Welcome to the User Profile Creator! 👤")

# 1. Create an empty dictionary to hold the profile data
profile = {}

# 2. Get information from the user
name = input("What is your name? ")
city = input("What city do you live in? ")
hobby = input("What is your favorite hobby? ")
age_str = input("How old are you? ")

# 3. Add the user's answers to the dictionary
profile["name"] = name
profile["city"] = city
profile["hobby"] = hobby
profile["age"] = int(age_str) # Convert age to a number

# 4. Add a list as a value inside the dictionary
skills_input = input("Enter two skills, separated by a comma (e.g., Python, public speaking): ")
# The .split(',') method breaks a string into a list
profile["skills"] = skills_input.split(',')

# 5. Print the final, formatted profile
print("\n--- Your Generated Profile ---")
print(f"👤 Name: {profile['name']}")
print(f"🎂 Age: {profile['age']}")
print(f"📍 City: {profile['city']}")
print(f"🎨 Hobby: {profile['hobby']}")
print(f"🛠️ Skills: {profile['skills']}")
print("----------------------------")


print("\n" + "="*50)
# print("Congratulations on completing Day 3! You now have a solid understanding of how to organize data using lists, dictionaries, tuples, and sets.")
# print("Tomorrow, we will learn how to use loops to work with these structures!")
