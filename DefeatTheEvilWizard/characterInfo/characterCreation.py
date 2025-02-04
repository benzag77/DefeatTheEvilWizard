from gameClasses.PlayerClasses.archer import Archer
from gameClasses.PlayerClasses.warrior import Warrior
from gameClasses.PlayerClasses.mage import Mage
from gameClasses.PlayerClasses.paladin import Paladin
from gameClasses.PlayerClasses.orc import Orc

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