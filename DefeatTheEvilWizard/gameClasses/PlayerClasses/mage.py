import random
from characterInfo.characterBaseAttributes import Character

class Mage(Character):

    def __init__(self, name):
        super().__init__(name, health=110, attack_power=32, heal=8)
        self.power_spell_turns = 0
        self.reflect_active = False

    def attack(self, opponent):

        # Apply power spell damage boost if active
        if self.power_spell_turns > 0:
            random_attack = random.randint(1, int(self.attack_power * 1.5))
            self.power_spell_turns -= 1
            print(f"Power Spell Active! Increased damage!")
        else:
            random_attack = random.randint(1, self.attack_power)
        
        opponent.health -= random_attack
        print(f"{self.name} attacks {opponent.name} for {random_attack} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def special_ability(self, opponent):

        while True:
            print('''
--- Choose Special Ability: ---
1. Reflect (reflects 75% of damage back to opponent)
2. Power Spell (increases damage by 50% for two turns)
''')
            choice = input("Choose what special ability you want to use (1 or 2): \n")
            
            if not choice.isdigit():
                print("Invalid input. Please enter a number between 1 and 2.")
                continue

            choice = int(choice)

            if choice == 1:
                self.reflect_active = True
                print(f"{self.name} casts Reflect! Next attack will be reflected by 75%!")
                break
            elif choice == 2:
                self.power_spell_turns = 2
                print(f"{self.name} casts Power Spell! Next two attacks will be 50% stronger!")
                break
            else:
                print("Invalid choice. Try again.")