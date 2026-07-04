from Weapon import *

class Hero:
    def __init__(self, healthPoints, attackDamage):
        self.healthPoints = healthPoints
        self.attackDamage = attackDamage
        self.is_weapon_equipped = False
        self.weapon: Weapon = None
        print(f'Hero has {healthPoints} points And can do attack of {attackDamage} ')


    def equippedWeapon(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            self.attackDamage += self.weapon.attack_increase
            self.is_weapon_equipped = True

    def attack(self):
        print(f"Hero attacks for {self.attackDamage} damage.")