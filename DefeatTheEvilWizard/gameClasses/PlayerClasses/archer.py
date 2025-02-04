import random
from characterInfo.characterBaseAttributes import Character

class Archer(Character):

    def __init__(self, name):
        super().__init__(name, health=120, attack_power=28, heal=5)


    def special_ability(self, opponent):

        while True:
            print('''
--- Choose Special Ability: ---
1. Quick Shot (double arrow attack)
2. Evade (evades the next attack)
''')
        
            choice = input("Choose what special ability you want to use (1 or 2): \n")
        
            if not choice.isdigit():
                print("Invalid input. Please enter a number between 1 and 2.")
                continue

            choice = int(choice)

            if choice == 1:
                random_attack = 2 * random.randint(1, self.attack_power)
                opponent.health -= random_attack
                print(f"{self.name} attacks {opponent.name} with Quick Shot for {random_attack} damage!")
                if opponent.health <= 0:
                    print(f"{opponent.name} has been defeated!")
                break

            elif choice == 2:
                self.evade_next_attack = True
                print(f"{self.name} uses Evade to avoid the next attack!")
                break