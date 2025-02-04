import random
from gameClasses.PlayerClasses.orc import Orc
from gameClasses.PlayerClasses.mage import Mage


def battle(player, wizard):

    """
    Main battle loop that manages:
    - Turn-based combat with player and wizard actions
    - Ability cooldowns and status effects (stun, evade, reflect)
    - Health tracking and battle outcome
    """
    print(f'''
--- The Battle Starts! ---
{player.name} vs {wizard.name}
{player.name} health: {player.health} {wizard.name} health: {wizard.health}
--- Good Luck! ---
    ''')
    
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
            
            if player.is_stunned == True:
                print(f"{player.name} is stunned and cannot attack!")
                player.is_stunned = False
                valid_action = True
                break

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

        # Wizard's turn only happens after valid player action or player is stunned. This is to avoid special ability use when on cooldown to have the wizard never attack or heal
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