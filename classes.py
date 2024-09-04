import re
import random
class Mob:
    def __init__(self, name, hp: int, is_alive = True):
        self.name = name
        self._hp = int(hp)
        self.is_alive = is_alive

    def __sub__(self, other: int):
        self.hp -= other
        return self.hp

    def __str__(self):
        return f"{self.name} is at {self.hp} hit points"

    def attack(self, other):
        dmg = int(input("damage: "))
        other.hp -= dmg
        return other.hp

    def heal(self):
        health = int(input("healing: "))
        self.hp += health
        return self.hp



    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp
        if hp <= 0:
            print(f"a {self.name} has been slain!")
            self.is_alive = False
            return self.is_alive

class Player(Mob):
    def __init__(self, name, armor, hp, is_alive = True):
        super().__init__(name, hp)
        self.is_alive = is_alive
        self.armor = int(armor)


    @classmethod
    def get(cls):
        players = input("player, armor class, and hp: ")
        match = re.search(r"(?P<name>\w+) (?P<armor>\d+) (?P<hp>\d+)", players)
        if match:
            return cls(match.group("name"), match.group("armor"), match.group("hp"), is_alive = True)
        else:
            raise ValueError



class Bandit(Mob):
    def __init__(self, name="bandit", hp=11, is_alive = True):
        self.is_alive = is_alive
        self._hp = hp
        self.name = name

    def attack(self, other: Player):
        if random.randint(0, 20) + 3 > other.armor:
            other.hp -= 4
            print(f"{other.name} has been slashed with a scimitar! HP: {other.hp}")
            return other.hp
        else:
            print(f"{self.name} did not make {other.name}'s armor class")

class Owlbear(Mob):
    def __init__(self, name="owlbear", hp=59, is_alive = True):
        self._hp = hp
        self.name = name
        super().__init__(is_alive)
    def attack(self, other: Player):
        if random.randint(0, 20) + 7 > other.armor:
            other.hp -= 10
            print(f"{other.name} has been bitten by an owlbear! HP: {other.hp}")
            return other.hp
        else:
            print(f"{self.name} did not make {other.name}'s armor class")
            return 0
