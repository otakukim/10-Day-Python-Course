# ==========================================
# SECTION 5: User-Driven Programs
# ==========================================

print("SECTION 5: Programs That Adapt to Users")
print("-" * 37)

# Exercise 5.1: Personalized Responses
# Learn to create programs that respond differently to different users
print("👋 Smart Greeting System")

name = input("What's your name? ")
time_of_day = input("Is it morning, afternoon, or evening? ")

# Handle various ways people might respond
time_response = time_of_day.lower()

if "morning" in time_response:
    greeting = f"Good morning, {name}!"
    print(greeting)
    print("Hope you have a great start to your day!")
elif "afternoon" in time_response:
    greeting = f"Good afternoon, {name}!"
    print(greeting)
    print("Hope your day is going well!")
elif "evening" in time_response or "night" in time_response:
    greeting = f"Good evening, {name}!"
    print(greeting)
    print("Hope you have a restful evening!")
else:
    greeting = f"Hello, {name}!"
    print(greeting)
    print("Have a wonderful day!")


print("\n" + "="*50)

# YOUR CODE HERE - Create a personalized study assistant:
# Ask for name, grade level, and subject difficulty
# Give personalized study advice based on their answers
# YOUR CODE HERE:


print("\n" + "="*50)

# Exercise 5.2: Dynamic Content Generation
# Learn to create content based on user preferences
print("\n📝 Dynamic Story Generator")

character_name = input("Enter a character name: ")
character_age = int(input("How old is the character? "))
setting = input("Enter a setting (like 'forest' or 'city'): ")
object_found = input("What magical object does the character find? ")

# Create age-appropriate story elements
if character_age < 12:
    adventure_type = "went on a fun adventure"
    challenge = "solve a friendly puzzle"
elif character_age < 18:
    adventure_type = "embarked on an exciting quest"
    challenge = "overcome a challenging obstacle"
else:
    adventure_type = "began a dangerous mission"
    challenge = "face a formidable enemy"

story = f"""
🌟 The Adventure of {character_name} 🌟

{character_name}, age {character_age}, {adventure_type} in a {setting}.
Suddenly, they discovered a mysterious {object_found}!

"What could this {object_found} be?" wondered {character_name}.

Their mission: {challenge} using the power of the {object_found}.

And so the adventure began...
"""

print(story)

print("\n" + "="*50)

# YOUR CODE HERE - Create a recipe customizer:
# Ask for dietary preferences and generate a custom recipe description
# YOUR CODE HERE:




print("\n" + "="*50)
