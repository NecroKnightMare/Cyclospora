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