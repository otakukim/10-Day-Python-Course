# ==========================================
# SECTION 4: Day 6 Project - The Magic 8-Ball
# ==========================================

print("SECTION 4: Day 6 Project - The Magic 8-Ball")
print("-" * 45)

# This project uses the random module to create a classic Magic 8-Ball game.

import random

# A list of possible responses
responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

print("🎱 Welcome to the Magic 8-Ball! �")
print("Ask a yes/no question to receive your fortune.")

# We use a loop to allow the user to ask multiple questions.
while True:
    question = input("\n> What is your question? (or type 'quit' to exit): ")

    if question.lower() == 'quit':
        print("May your future be bright. Goodbye!")
        break
    
    # Check if the user actually asked a question
    if '?' not in question:
        print("Please ask a question ending with a '?'")
        continue # Skip to the next iteration of the loop

    # Get a random response from our list
    fortune = random.choice(responses)

    print(f"\nShake... Shake... Shake...")
    print(f"The Magic 8-Ball says: '{fortune}'")

print("\n" + "="*50)
# print("Congratulations on completing Day 6! You can now expand your programs with Python's vast ecosystem of modules.")
�
