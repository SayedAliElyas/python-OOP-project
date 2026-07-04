from Zombie import *
from Ogre import *
from Hero import *
from Weapon import *

def battle(e1 : Enemy, e2: Enemy):
      e1.talk()
      e2.talk()
      print("#############BATTLE BEGINS###########")
      rounds = 0
      while e1.healthPoints > 0 and e2.healthPoints > 0:
            rounds += 1
            print(f"_____________Round {rounds}_____________________")
            e1.specialAttack()
            e2.specialAttack()
            print(f"{e1.get_type_of_enemy()}: {e1.healthPoints} HP left")
            print(f"{e2.get_type_of_enemy()}: {e2.healthPoints} HP left")
            e2.attack()
            e1.healthPoints -= e2.attackDamage
            e1.attack()
            e2.healthPoints -= e1.attackDamage

      print("#############BATTLE RESULT###########")
      if e1.healthPoints <= 0 and e2.healthPoints <= 0:
            print("Draw")
      elif e1.healthPoints > 0 >= e2.healthPoints:
            print(f"{e1.get_type_of_enemy()} wins")
      elif e2.healthPoints > 0 >= e1.healthPoints:
            print(f"{e2.get_type_of_enemy()} wins")
      else:
            print("No winner after max rounds (draw)")

def hero_battle(hero:Hero, enemy: Enemy):

      print("***********HERO BATTLE BEGINS**********")
      rounds = 0
      while hero.healthPoints > 0 and enemy.healthPoints > 0:
            rounds += 1
            print(f"_____________Round {rounds}_____________________")
            print(f"hero {hero.healthPoints} HP left")
            print(f"{enemy.get_type_of_enemy()}: {enemy.healthPoints} HP left")
            enemy.attack()
            hero.healthPoints -= enemy.attackDamage
            hero.attack()
            enemy.healthPoints -= hero.attackDamage

      print("***********HERO BATTLE RESULT**********")

      if hero.healthPoints <= 0 and enemy.healthPoints <= 0:
            print("Draw")
      elif hero.healthPoints > 0 >= enemy.healthPoints:
            print(f"Hero wins")
      elif enemy.healthPoints > 0 >= hero.healthPoints:
            print(f"{enemy.get_type_of_enemy()} wins")
      else:
            print("No winner after max rounds (draw)")



zombie = Zombie( 1000, 500)
ogre = Ogre( 1000, 50)
hero = Hero(1000, 30)
weapon = Weapon("sword", 100)
hero.weapon = weapon
hero.equippedWeapon()
hero_battle(hero, ogre)


