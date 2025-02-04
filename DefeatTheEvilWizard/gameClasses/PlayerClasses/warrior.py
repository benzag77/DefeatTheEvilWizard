import random
from characterInfo.characterBaseAttributes import Character


class Warrior(Character):

    def __init__(self, name):
        super().__init__(name, health=135, attack_power=25, heal=5)
        self.dragon_turns = 0
    
    # Adds dragon damage when summoned
    def attack(self, opponent):

        random_attack = random.randint(1, self.attack_power)
        if self.dragon_turns > 0:
            opponent.health -= 15
            self.health -= 5
            self.dragon_turns -= 1
            print(f"Dragon deals 15 additional damage to {opponent.name} and 5 damage to {self.name}!")
        opponent.health -= random_attack
        print(f"{self.name} attacks {opponent.name} for {random_attack} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def special_ability(self, opponent):

        while True:
            print('''
--- Choose Special Ability: ---
1. Summon Dragon (deals 15 damage to opponent but 5 to self for two turns)
2. Ground Smash (stuns opponent for one turn and deals 8 damage)
''')
            choice = input("Choose what special ability you want to use (1 or 2): \n")
            
            if not choice.isdigit():
                print("Invalid input. Please enter a number between 1 and 2: \n")
                continue

            choice = int(choice)

            if choice == 1:
                self.dragon_turns = 2
                opponent.health -= 15
                self.health -= 5
                print(f"{self.name} summons a dragon! It deals 15 damage to {opponent.name} and 5 damage to {self.name}!")
                break
            elif choice == 2:
                opponent.is_stunned = True
                opponent.health -= 8
                print(f"{self.name} performs Ground Smash! {opponent.name} is stunned for the next turn and takes 8 damage!")
                break