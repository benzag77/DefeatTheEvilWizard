from characterInfo.characterBaseAttributes import Character

class Orc(Character):

    def __init__(self, name):
        super().__init__(name, health=135, attack_power=30, heal=5)
        self.regrowth_turns = 0
        self.regrowth_amount = 10

    def regrowth(self):
        
        if self.regrowth_turns > 0:
            self.health += self.regrowth_amount
            self.regrowth_turns -= 1
            print(f"{self.name} heals for {self.regrowth_amount} health due to Regrowth! Current health: {self.health}")

    def special_ability(self, opponent):

        while True:
            print('''
--- Choose Special Ability: ---
1. Manic Strike (30 damage for one turn but can't attack next turn)
2. Regrowth (heals for 10 health for 2 turns)
''')

            choice = input("Choose what special ability you want to use (1 or 2): \n")
        
            if not choice.isdigit():
                print("Invalid input. Please enter a number between 1 and 2.")
                continue

            choice = int(choice)

            if choice == 1:
                opponent.health -= 30
                self.is_stunned = True
                print(f"{self.name} uses Manic Strike! Deals 30 damage to {opponent.name} but can't attack next turn!")
                if opponent.health <= 0:
                    print(f"{opponent.name} has been defeated!")
                break

            elif choice == 2:
                self.regrowth_turns = 2
                print(f"{self.name} uses Regrowth to heal for {self.regrowth_amount} health for the next two turns!")
                break