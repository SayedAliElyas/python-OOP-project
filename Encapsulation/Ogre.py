import random
from Enemy import *

class Ogre(Enemy):
    def __init__(self,healthPoints, attackDamage):
        super().__init__(type_of_enemy="Ogre",
                         healthPoints=healthPoints,
                         attackDamage=attackDamage)

    def talk(self):
        print("Ogre is slamming hands all around!")

    def specialAttack(self):
        did_special_attack_work = random.random() < 0.2
        if did_special_attack_work:
            self.attackDamage += 50
            print("Orge attack's damage increased by 200AD")
