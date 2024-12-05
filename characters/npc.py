from creature import Creature
import random
from weapon import Weapon
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

    npc1 = NPC(name="Caveman", health=20, defense=5)
    npc2 = NPC(name="knight", health=30, defense=10)
    npc3 = NPC(name="Ninja", health=35, defense=15)
    npc4 = NPC(name="British Soldier", health=40, defense=20)
    npc5 = NPC(name="Nazi Soldier", health=50, defense=25)
    npc6 = NPC(name="Alien", health=100, defense=50)
    
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

        def attack(self, target):
            """
            Cavemen have a chance to throw rocks for ranged damage.
            """
            if random.random() < 0.5:  # 50% chance to throw a rock
                super().attack(target, Weapon("Rock", "ranged", 8, range=3, accuracy=0.6))
                print(f"{self.name} throws a rock at {target.name}!")
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

        def attack(self, target):
            """
            Knights have a chance to sling stones for ranged damage.
            """
            if random.random() < 0.5:  # 50% chance to sling a stone
                super().attack(target, Weapon("stone", "ranged", 5, range=4, accuracy=2))
                print(f"{self.name} slings a stone at {target.name}!")
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

        def attack(self, target):
            """
            Ninja have a chance to throw Shurikens for ranged damage.
            """
            if random.random() < 0.5:  # 50% chance to throw a rock
                super().attack(target, Weapon("Shuriken", "ranged", 6, range=5, accuracy=4))
                print(f"{self.name} throws a rock at {target.name}!")
            else:  # Otherwise, use club for melee attack
                super().attack(target, Weapon("Club", "melee", 6))

    class British_Soldier(NPC):
        """
        Represents a British Soldier, a Battle smart and hostile human.
        """

        def __init__(self, name="British Soldier", hp=40, ac=5):
            """
            Initializes a British Soldier instance.
            """
            super().__init__(name, hp, ac)

        def attack(self, target):
            """
            British soldiers have a chance to shoot their musket for ranged damage.
            """
            if random.random() < 0.5:  # 50% chance to shoot musket
                super().attack(target, Weapon("Rock", "ranged", 9, range=7, accuracy=3))
                print(f"{self.name} shoots at {target.name}!")
            else:  # Otherwise, use club for melee attack
                super().attack(target, Weapon("Bayonett", "melee", 8))

    class Nazi_Soldier(NPC):
        """
        Represents a Caveman, a primitive and hostile human.
        """

        def __init__(self, name="Nazi Soldier", hp=50, ac=15):
            """
            Initializes a Nazi Soldier instance.
            """
            super().__init__(name, hp, ac)

        def attack(self, target):
            """
            NAzi Soldiers have a chance to shoot their pistol for ranged damage.
            """
            if random.random() < 0.5:  # 50% chance to shoot with their Luger
                super().attack(target, Weapon("Luger ", "ranged", 8, range=9, accuracy=3.5))
                print(f"{self.name} throws a rock at {target.name}!")
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

        def attack(self, target):
            """
            Aliens have a chance to shoot a raygun for ranged damage.
            """
            if random.random() < 0.5:  # 50% chance to shoot raygun
                super().attack(target, Weapon("Raygun", "ranged", 8, range=10, accuracy=5))
                print(f"{self.name} shoots a raygun blast at {target.name}!")
            else:  # Otherwise, use Plasma sword for melee attack
                super().attack(target, Weapon("Plasma sword", "melee", 15))