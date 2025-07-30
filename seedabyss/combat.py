import random

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
