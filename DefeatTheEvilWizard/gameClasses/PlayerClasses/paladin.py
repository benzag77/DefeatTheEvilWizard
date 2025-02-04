import random
from characterInfo.characterBaseAttributes import Character

class Paladin(Character):

    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20, heal=12)


    def special_ability(self, opponent):

        while True:
            print('''
--- Choose Special Ability: ---
1. Holy Strike (+10 bonus damage)
2. Divine Shield (blocks the next attack)
''')
        
            choice = input("Choose what special ability you want to use (1 or 2): \n")
        
            if not choice.isdigit():
                print("Invalid input. Please enter a number between 1 and 2.")
                continue

            choice = int(choice)

            if choice == 1:
                random_attack = 10 + random.randint(1, self.attack_power)
                opponent.health -= random_attack
                print(f"{self.name} attacks {opponent.name} with Holy Strike for {random_attack} damage!")
                if opponent.health <= 0:
                    print(f"{opponent.name} has been defeated!")
                break

            elif choice == 2:
                self.evade_next_attack = True
                print(f"{self.name} uses Divine Shield to block the next attack!")
                break