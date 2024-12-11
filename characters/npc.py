from .creature import Creature
import random
from items.weapon import Weapon
class NPC(Creature):
    """
    Represents a non-player character in the RPG game.
    """

    def __init__(self, name, hp, ac):
        """
        Initializes an NPC instance.

        Args:
            name (str): The name of the NPC.
            hp (int): The NPC's hit points.
            df (int): The NPC's defense points.
        """

        super().__init__(name, hp, ac)


class Caveman(NPC):
        """
        Represents a Caveman, a primitive and potentially hostile human.
        """

        def __init__(self, name="Caveman", hp=20, ac=5):
            """
            Initializes a Caveman instance.
            """
            super().__init__(name, hp, ac)
            super().__init__("Caveman", 30, 5)  # You can adjust health and AC as needed
            self.weapon = {  # weapon is now a dictionary
            "Name": "Club",
            "Damage": (6, 10),
        }

        def attack(self, target, battle_log):
            """
            Cavemen have a chance to throw rocks for ranged damage.
            """
            if random.random() < 0.5:  # 50% chance to throw a rock
                super().attack(target, Weapon("Rock", "ranged", 8, range=3, accuracy=0.6))
                battle_log.append(f"{self.name} throws a rock at {target.name}!")
            else:  # Otherwise, use club for melee attack
                super().attack(target, Weapon("Club", "melee", 6))

class Knight(NPC):
        """
        Represents a Knight, an Honourable and potentially hostile human.
        """

        def __init__(self, name="Knight", hp=30, ac=25):
            """
            Initializes a Knight instance.
            """
            super().__init__(name, hp, ac)
            self.weapon = {
            "Name": "Longsword",
            "Damage": (8, 12),  # Damage range
        }

        def attack(self, target, battle_log):
            """
            Knights have a chance to sling stones for ranged damage.
            """
            if random.random() < 0.5:  # 50% chance to sling a stone
                super().attack(target, Weapon("stone", "ranged", 5, range=4, accuracy=2))
                battle_log.append(f"{self.name} slings a stone at {target.name}!")
            else:  # Otherwise, use Longsword for melee attack
                super().attack(target, Weapon("Longsword", "melee", 10))

class Ninja(NPC):
        """
        Represents a Ninja, a stealthy and hostile human.
        """

        def __init__(self, name="Ninja", hp=35, ac=10):
            """
            Initializes a Ninja instance.
            """
            super().__init__(name, hp, ac)
            self.weapon = {
            "Name": "Tanto",
            "Damage": (8, 12)
        }
        def attack(self, target, battle_log):
            """
            Ninja have a chance to throw Shurikens for ranged damage.
            """
            if random.random() < 0.5:  # 50% chance to shoot a bow
                super().attack(target, Weapon("Bow", "ranged", 6, range=5, accuracy=4))
                battle_log.append(f"{self.name} shoots their Bow at {target.name}!")
            else:  # Otherwise, use Tanto for melee attack
                super().attack(target, Weapon("Tanto", "melee", 8))

class British_Soldier(NPC):
        """
        Represents a British Soldier, a Battle smart and hostile human.
        """

        def __init__(self, name="British Soldier", hp=40, ac=5):
            """
            Initializes a British Soldier instance.
            """
            super().__init__(name, hp, ac)
            self.weapon = {
            "Name": "SA80",
            "Damage": (8, 12)
            }
        def attack(self, target, battle_log):
            """
            British soldiers have a chance to shoot their musket for ranged damage.
            """
            if random.random() < 0.7:  # 70% chance to shoot rifle
                super().attack(target, Weapon("SA80", "ranged", 9, range=25, accuracy=9))
                battle_log.append(f"{self.name} shoots at {target.name}!")
            else:  # Otherwise, use club for melee attack
                super().attack(target, Weapon("Bayonett", "melee", 8))

class Nazi_Soldier(NPC):
        """
        Represents a Nazi Soldier, a primitive and hostile human.
        """

        def __init__(self, name="Nazi Soldier", hp=50, ac=15):
            """
            Initializes a Nazi Soldier instance.
            """
            super().__init__(name, hp, ac)
            self.weapon = {
            "Name": "Luger",
            "Damage": (8, 12)
            }
        def attack(self, target, battle_log):
            """
            NAzi Soldiers have a chance to shoot their pistol for ranged damage.
            """
            if random.random() < 0.5:  # 50% chance to shoot with their Luger
                super().attack(target, Weapon("Luger ", "ranged", 8, range=7, accuracy=3.5))
                battle_log.append(f"{self.name} throws a rock at {target.name}!")
            else:  # Otherwise, use  for melee attack
                super().attack(target, Weapon("Combat Knife", "melee", 7))

class Alien(NPC):
        """
        Represents an Alien, a genius and hostile lifeform.
        """

        def __init__(self, name="Alien", hp=100, ac=50):
            """
            Initializes an Alien instance.
            """
            super().__init__(name, hp, ac)
            self.weapon = {
            "Name": "Raygun",
            "Damage": (10, 15)
            }

        def attack(self, target, battle_log):
            """
            Aliens have a chance to shoot a raygun for ranged damage.
            """
            if random.random() < 0.5:  # 50% chance to shoot raygun
                super().attack(target, Weapon("Raygun", "ranged", 8, range=10, accuracy=5))
                battle_log.append(f"{self.name} shoots a raygun blast at {target.name}!")
            else:  # Otherwise, use Plasma sword for melee attack
                super().attack(target, Weapon("Plasma sword", "melee", 15))
