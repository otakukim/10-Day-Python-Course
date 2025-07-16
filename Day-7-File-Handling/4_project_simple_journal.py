# ==========================================
# SECTION 4: Day 7 Project - Simple Journal
# ==========================================

print("SECTION 4: Day 7 Project - Simple Journal")
print("-" * 42)

# This project uses file I/O to create a simple journal that saves entries.
import datetime

JOURNAL_FILE = "my_journal.txt"

print("📖 Welcome to your Simple Journal! 📖")

while True:
    print("\n--- Journal Menu ---")
    print("1. Write a new entry")
    print("2. View all entries")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        # Get the current time for the entry's timestamp
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        entry = input("What are you thinking about?\n> ")

        # Open the journal in 'append' mode to add the new entry
        with open(JOURNAL_FILE, 'a') as file:
            file.write(f"--- Entry: {timestamp} ---\n")
            file.write(f"{entry}\n\n")
        
        print("Your entry has been saved!")

    elif choice == "2":
        try:
            # Try to open and read the journal file
            with open(JOURNAL_FILE, 'r') as file:
                journal_contents = file.read()
                if journal_contents:
                    print("\n--- Your Journal Entries ---")
                    print(journal_contents)
                    print("--------------------------")
                else:
                    print("\nYour journal is empty. Write an entry first!")
        except FileNotFoundError:
            # Handle the case where the journal file doesn't exist yet
            print("\nYour journal is empty. Write an entry first!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 3.")


print("\n" + "="*50)
# print("Congratulations on completing Day 7! Your programs can now remember information by saving it to files.")
