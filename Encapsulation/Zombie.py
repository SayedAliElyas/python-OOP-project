import random
from Enemy import *

class Zombie(Enemy):
    def __init__(self,healthPoints, attackDamage):
        super().__init__(type_of_enemy="Zombie",
                         healthPoints=healthPoints,
                         attackDamage=attackDamage)

    def talk(self):
        print("Grumbling......")

    def specialAttack(self):
        did_special_attack_work = random.random() < 0.4
        if did_special_attack_work:
            self.healthPoints += 100
            print("Zombie regenerated 100HP")
