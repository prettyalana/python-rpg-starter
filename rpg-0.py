"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

from random import random


class Character:
    # When a keyword argument is used, all arguments that follow must be a keyword argument
    # ex: name=None
    def __init__(self, name, health, power):
        self.name = name if name else self.__class__.__name__.lower()
        self.health = health
        self.power = power

    def __str__(self):
        return self.name

    def attack(self, other_character):
        other_character.health -= self.power
        print(f"{self.name} does {self.power} damage to {other_character}.")

    def alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        if self.health <= 0:
            if self.name != "you":
                print(f"{self} is dead.")
            else:
                print("You are dead.")


class Enemy(Character):
    def __init__(self, name, health, power, bounty):
        super().__init__(name, health, power)
        self.bounty = bounty

    def attack(self, hero):
        super().attack(hero)


class Hero(Character):
    def __init__(self, name, health, power, coins):
        super().__init__(name, health, power)
        self.coins = coins

    def attack(self, goblin):
        super().attack(goblin)

    def buy(self, item):
        self.coins -= item


class Goblin(Enemy):
    def __init__(self, name, health, power, bounty):
        super().__init__(name, health, power, bounty)


class Shadow(Enemy):
    def __init__(self, name, health, power, bounty):
        super().__init__(name, health, power, bounty)

    def will_take_damage(self, damage_amount):
        if random() < 0.1:
            self.health -= damage_amount


class Zombie(Enemy):
    def __init__(self, name, health, power, bounty):
        super().__init__(name, health, power, bounty)

    def alive(self):
        return True


class Wizard(Character):
    pass


class Archer(Character):
    pass


class Scribe(Character):
    pass


class Store:
    # class variable shared across all instances of a class
    items = ["Tonic", "Sword"]

    def __init__(self, name):
        # instance variable, which is unique to each object
        self.name = name

    def do_shopping(self):
        print(f"Welcome! You have a balance of {Hero.coins} coins.")
        print(f"We have {", ".join(self.items)} in stock.")


def main():
    hero = Hero(name="you", health=10, power=5, coins=20)
    goblin = Goblin(name="the goblin", health=6, power=2, bounty=6)
    shadow = Shadow(name="Shadow", health=1, power=1, bounty=5)
    zombie = Zombie(name="Zombie", health=1, power=1, bounty=0)

    while goblin.alive() and hero.alive():
        print(f"You have {hero.health} health and {hero.power} power.")
        print(f"The goblin has {goblin.health} health and {goblin.power} power")
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print(
            "> ",
        )
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            goblin.print_status()
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {user_input}")

        if goblin.health > 0:
            goblin.attack(hero)
            hero.print_status()


main()
