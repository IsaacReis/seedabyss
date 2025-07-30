# SeedAbyss

**SeedAbyss** is a simple procedural dungeon exploration game for the command line (CLI). Players venture into the Abyss, encounter randomly generated enemies, and collect loot with unique effects.

## 🎮 How to Play

When you start the game, you'll be greeted with a welcome message and prompted to explore or quit.

During exploration:
- A random enemy will appear with a procedurally generated name and a random amount of HP.
- You can choose to **attack** or **run**.
- If you defeat the enemy, you'll receive a random item with a special effect.
- Loot is saved to a JSON file (`items.json`) for persistence.

## 📁 File Structure

- `data/monster_names.json`: Contains prefixes and suffixes used to generate monster names.
- `data/item_names.json`: Contains prefixes and suffixes used to generate item names.
- `data/items.json`: Stores the items collected by the player.

## 🧠 Key Features

- Procedural generation of monster and item names.
- Simple combat system based on user input.
- Loot system with randomized effects.
- Persistent inventory saved in JSON format.

## 🚀 Running the Game

Make sure the required JSON files are in the `data/` folder, then run the main script:

```bash
python main.py
```

## 📌 Requirements

- Python 3.x
- No external dependencies (uses only the standard library)

## 🔮 Future Improvements

- Leveling system and player progression
- Inventory management
- More enemy types and item effects
- Graphical interface or web version

Made with 💀 by Isaac Adriano de Andrade Reis