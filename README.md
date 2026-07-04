# python-OOP-project
# ⚔️ RPG Battle Simulator

A small Python project simulating turn-based battles between a **Hero** and fantasy **Enemies** (Zombies, Ogres). Built as a hands-on demonstration of core Object-Oriented Programming concepts.

## 📖 Overview

The Hero fights an Enemy in a turn-based loop: each side attacks, takes damage, and occasionally triggers a random special ability. The battle continues until one side's health drops to zero (with a safety cap to guarantee the fight always ends).

```
Hero has 1000 points And can do attack of 30
Ogre has 1000 health points And can do attack of 50
***********HERO BATTLE BEGINS**********
__________________________________
hero 1000 HP left
Ogre: 1000 HP left
Ogre attack for 50 damage.
Hero attacks for 130 damage.
...
Hero wins
```

## 🧱 The Four Pillars of OOP

This project was built specifically to showcase each pillar of object-oriented design in a real, working example.

### 1. Encapsulation
`Enemy` keeps its identity private using name-mangling (`__type_of_enemy`), exposing it only through a controlled getter. This protects the internal state from being changed directly from outside the class.

```python
class Enemy:
    def __init__(self, type_of_enemy, healthPoints=10.0, attackDamage=1.0):
        self.__type_of_enemy = type_of_enemy   # private attribute

    def get_type_of_enemy(self):               # controlled access
        return self.__type_of_enemy
```

### 2. Inheritance
`Zombie` and `Ogre` both inherit shared behavior (`healthPoints`, `attackDamage`, `attack()`, `talk()`) from the `Enemy` base class, avoiding duplicated code while adding their own personality.

```python
class Zombie(Enemy):
    def __init__(self, healthPoints, attackDamage):
        super().__init__(type_of_enemy="Zombie",
                          healthPoints=healthPoints,
                          attackDamage=attackDamage)
```

### 3. Composition
The `Hero` doesn't *inherit* from `Weapon` - it **has a** `Weapon`. This "has-a" relationship lets a Hero exist with or without a weapon, and lets weapons be swapped independently of the Hero class itself.

```python
class Hero:
    def __init__(self, healthPoints, attackDamage):
        self.weapon: Weapon = None   # composed, not inherited

    def equippedWeapon(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            self.attackDamage += self.weapon.attack_increase
```

### 4. Polymorphism
Every `Enemy` responds to `specialAttack()` — but each subclass defines its **own version** of what that means. The game loop can call `enemy.specialAttack()` on any enemy type without knowing (or caring) which one it is; the correct behavior runs automatically.

```python
zombie.specialAttack()   # 40% chance to heal 100 HP
ogre.specialAttack()     # 20% chance to gain 100 attack damage
```

## 🗂️ Project Structure

```
├── Enemy.py       # Base class — encapsulation & shared enemy behavior
├── Zombie.py      # Enemy subclass — regenerates health
├── Ogre.py        # Enemy subclass — gains attack power
├── Hero.py        # Player character — composed with a Weapon
├── Weapon.py      # Equipment class used via composition
└── main.py        # Battle loop / entry point

