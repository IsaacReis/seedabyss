import json
import os
import random

DATA_DIR = "data"

def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), 'r') as f:
        return json.load(f)

def save_json(filename, data):
    with open(os.path.join(DATA_DIR, filename), 'w') as f:
        json.dump(data, f, indent=2)

def generate_name(name_data):
    return f"{random.choice(name_data['prefixes'])} {random.choice(name_data['suffixes'])}"

def generate_enemy():
    name_data = load_json("monster_names.json")
    name = generate_name(name_data)
    hp = random.randint(10, 30)
    return {"name": name, "hp": hp}

def generate_loot():
    name_data = load_json("item_names.json")
    name = generate_name(name_data)
    effect = random.choice(["+5 Strength", "+10 HP", "+3 Agility", "Fire Resistance"])
    return {"name": name, "effect": effect}

def fight(enemy):
    print(f"A wild {enemy['name']} appears with {enemy['hp']} HP!")
    while enemy["hp"] > 0:
        cmd = input("Command (attack/run): ").strip().lower()
        if cmd == "attack":
            dmg = random.randint(5, 15)
            enemy["hp"] -= dmg
            print(f"You hit the {enemy['name']} for {dmg} damage. Remaining HP: {max(enemy['hp'], 0)}")
        elif cmd == "run":
            print("You fled the battle!")
            return False
        else:
            print("Unknown command.")
    print(f"You defeated the {enemy['name']}!")
    return True

def main():
    print("Welcome to the Abyss!")
    while True:
        action = input("Explore abyss? (yes/quit): ").strip().lower()
        if action == "yes":
            enemy = generate_enemy()
            if fight(enemy):
                loot = generate_loot()
                print(f"You found loot: {loot['name']} with effect {loot['effect']}")
                items = load_json("items.json")
                items.append(loot)
                save_json("items.json", items)
        elif action == "quit":
            print("Exiting the abyss. Goodbye!")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
