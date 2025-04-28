"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""


class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def __str__(self):
        return self.__class__.__name__
        # TODO: return "goblin" or "you" instead of class name

    def attack(self, other_character):
        other_character.health -= self.power
        print(f"You do {self.power} damage to {other_character}.")

    def alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        if self.health <= 0:
            print(f"{self} is dead.")


class Hero(Character):
    def __init__(self, health, power):
        super().__init__(health, power)

    def attack(self, goblin):
        super().attack(goblin)


class Goblin(Character):
    def __init__(self, health, power):
        super().__init__(health, power)

    def attack(self, hero):
        hero.health -= self.power
        damage = self.power
        print(f"The goblin does {damage} damage to you.")

    def print_status(self):
        if self.health <= 0:
            print("The goblin is dead.")


def main():
    hero = Hero(health=10, power=5)
    goblin = Goblin(health=6, power=2)

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
