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