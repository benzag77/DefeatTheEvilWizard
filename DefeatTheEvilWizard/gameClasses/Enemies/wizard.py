from characterInfo.characterBaseAttributes import Character

class EvilWizard(Character):

    #Main enemy class
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, heal=5)