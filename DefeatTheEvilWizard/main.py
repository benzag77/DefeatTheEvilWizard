from characterInfo.characterCreation import create_character
from gameClasses.Enemies.wizard import EvilWizard
from battle.battleWizard import battle

def main():

    #Entry point of the game - creates characters and initiates battle
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()