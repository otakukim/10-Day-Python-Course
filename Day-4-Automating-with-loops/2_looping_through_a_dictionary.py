# Exercise 1.2: Looping Through a Dictionary
# When you loop through a dictionary, you get its keys by default.
print("\n📖 Looping through a dictionary:")

player_stats = {
    "name": "Alex",
    "level": 5,
    "health": 100
}

print("Player Stat Keys:")
for stat_key in player_stats:
    # You can use the key to access the value inside the loop
    stat_value = player_stats[stat_key]
    print(f"-> Key: '{stat_key}', Value: {stat_value}")

print("\n" + "="*50)
