import random

class Character:

    """Base class for all game characters with basic attributes and actions"""
    def __init__(self, name, health, attack_power, heal):

        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.heal_amount = heal
        self.is_stunned = False
        self.ability_cooldown = 0

    def attack(self, opponent):

        random_attack = random.randint(1, self.attack_power)
        opponent.health -= random_attack
        print(f"{self.name} attacks {opponent.name} for {random_attack} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")


    def heal(self):

        # Only heal up to max_health to avoid overhealing
        healing_needed = self.max_health - self.health
        actual_heal = min(self.heal_amount, healing_needed)
    
        if actual_heal >= 0:
            self.health += actual_heal
            print(f"{self.name} heals for {actual_heal} health! Current health: {self.health}")
        else:
            print(f"{self.name} is at full health! Current health: {self.health}")

    def can_use_special(self):
        return self.ability_cooldown == 0


class EvilWizard(Character):

    #Main enemy class
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, heal=5)


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


def create_character():

    """
    Character creation function that:
    1. Displays available classes
    2. Takes user input for class selection and name
    3. Returns the created character instance
    """

    print('''
--- Choose your character class: ---
1. Warrior
2. Mage
3. Archer
4. Paladin
5. Orc
''' )

    class_choice = input("Enter the number of your class choice: \n")
    name = input("Enter your character's name: \n")

    options = {
        '1': Warrior,
        '2': Mage,
        '3': Archer,
        '4': Paladin,
        '5': Orc
    }

    chosen_class = options.get(class_choice, Warrior)
    if chosen_class is Warrior and class_choice not in options:
        print("Invalid choice. Defaulting to Warrior.")

    return chosen_class(name)

def battle(player, wizard):

    """
    Main battle loop that manages:
    - Turn-based combat with player and wizard actions
    - Ability cooldowns and status effects (stun, evade, reflect)
    - Health tracking and battle outcome
    """

    player.evade_next_attack = False
    turn_count = 0
    
    # Battle loop continues until someone dies
    while wizard.health > 0 and player.health > 0:

        if player.ability_cooldown > 0:
            player.ability_cooldown -= 1

        valid_action = False

        if isinstance(player, Orc):
            player.regrowth()
        
        while not valid_action:
            print('''
--- Your Turn: ---
1. Attack
2. Use Special Ability
3. Heal
4. View Stats
''')
            if player.ability_cooldown > 0:
                print(f"Special ability on cooldown for {player.ability_cooldown} more turns!")

            choice = input("Choose an action: \n")

            if choice == '1':
                player.attack(wizard)
                valid_action = True
            elif choice == '2':
                if player.can_use_special():
                    player.special_ability(wizard)
                    player.ability_cooldown = 6
                    valid_action = True
                else:
                    print(f"Special ability is on cooldown for {player.ability_cooldown} more turns!")
                    print("Please choose a different action.")
            elif choice == '3':
                player.heal()
                valid_action = True
            elif choice == '4':
                player.display_stats()
                print("\nViewing stats does not use your turn.")
            else:
                print("Invalid choice. Try again.")

        # Wizard's turn only happens after valid player action to avoid special ability use when on cooldown to have the wizard never attack or heal
        if wizard.health > 0:
            if wizard.is_stunned:
                print(f"{wizard.name} is stunned and cannot attack!")
                wizard.is_stunned = False
            elif not getattr(player, 'evade_next_attack', False):
                wizard_attack = random.randint(1, wizard.attack_power)
                player.health -= wizard_attack
                print(f"{wizard.name} attacks {player.name} for {wizard_attack} damage!")
                
                # Handle Mage's reflect ability
                if isinstance(player, Mage) and player.reflect_active:
                    reflect_damage = int(wizard_attack * 0.75)
                    wizard.health -= reflect_damage
                    player.health += reflect_damage
                    print(f"{player.name} reflects {reflect_damage} damage back to {wizard.name}!")
                    player.reflect_active = False
            else:
                print(f"{player.name} evades the attack!")
                player.evade_next_attack = False
            
            wizard.heal()

        if player.health <= 0:
            print(f"Game Over! {player.name} has been defeated! Wizard's health: {wizard.health}")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}! Congragulations! Player health: {player.health}")


def main():

    #Entry point of the game - creates characters and initiates battle
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()