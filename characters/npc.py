from creature import Creature
import random
from weapon import Weapon
class NPC(Creature):
    """
    Represents a non-player character in the RPG game.
    """

    def __init__(self, name, hp, df):
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
    
    super().__init__(name, hp, df)

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