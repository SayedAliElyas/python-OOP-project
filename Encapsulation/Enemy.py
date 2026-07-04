"""
We use encapsulation mainly to prevent data from being changed directly after it has been initialized.
We use a double underscore (__) at the beginning of variable names to make them private.
We then define methods (getters and setters) to access or modify these private variables safely.
"""

class Enemy:
    def __init__(self,type_of_enemy, healthPoints = 10.0, attackDamage = 1.0):
        self.__type_of_enemy = type_of_enemy
        self.healthPoints = healthPoints
        self.attackDamage = attackDamage
        print(f"{self.get_type_of_enemy()} has {self.healthPoints} health points "
              f"And can do attack of {self.attackDamage}")


    def talk(self):
        print(f'I am a {self.__type_of_enemy}. Be prepared to fight!')

    def walk_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you.')

    def attack(self):
        print(f'{self.__type_of_enemy} attack for {self.attackDamage} damage.')

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def specialAttack(self):
        print("There is no special type of attack")