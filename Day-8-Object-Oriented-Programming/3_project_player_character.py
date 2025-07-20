# ==========================================
# SECTION 3: Day 8 Project - The Player Character
# ==========================================

print("SECTION 3: Day 8 Project - The Player Character")
print("-" * 50)

# This project uses a class to represent a player in a game.

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 100
        self.inventory = []

    def show_stats(self):
        """Prints the player's current stats in a formatted way."""
        print("\n--- PLAYER STATS ---")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"HP: {self.hp}/100")
        print(f"Inventory: {self.inventory}")
        print("--------------------")

    def take_damage(self, amount):
        """Reduces the player's HP."""
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0 # HP can't go below zero
        print(f"{self.name} takes {amount} damage! Current HP: {self.hp}")

    def heal(self, amount):
        """Increases the player's HP."""
        self.hp += amount
        if self.hp > 100:
            self.hp = 100 # HP can't go above the max
        print(f"{self.name} heals for {amount} HP! Current HP: {self.hp}")
    
    def add_to_inventory(self, item):
        """Adds an item to the player's inventory list."""
        self.inventory.append(item)
        print(f"{item} was added to {self.name}'s inventory.")

# --- Let's create and use a Player object ---

# Create a new player
player1 = Player("Arin")
player1.show_stats()

# Perform some actions
player1.add_to_inventory("Health Potion")
player1.add_to_inventory("Sword")
player1.take_damage(25)
player1.heal(10)

# Show the final stats
player1.show_stats()

print("\n" + "="*50)
# print("Congratulations on completing Day 8! You now understand the basics of Object-Oriented Programming.")
