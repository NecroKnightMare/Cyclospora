from creature import Creature
class PlayerCharacter(Creature):
    """
    Represents a player-controlled character in the RPG game.
    """

    def __init__(self, name, hp, ac):
        """
        Initializes a PlayerCharacter instance.

        Args:
            name (str): The name of the player character.
            hp (int): The player character's hit points.
            ac (int): The player character's armor class.
        """
        super().__init__(name, hp, ac)
        self.special = {  # S.P.E.C.I.A.L. stats, all 5 currently. Will implement some way to vary them eventually maybe.
            "Strength": 5,
            "Perception": 5,
            "Endurance": 5,
            "Charisma": 5,
            "Intelligence": 5,
            "Agility": 5,
            "Luck": 5,
        }
        self.perks = []  # List to store acquired perks

    def add_perk(self, perk_name):
        """
        Adds a perk to the player character's perk list.
        """
        self.perks.append(perk_name)
        print(f"{self.name} acquired the perk: {perk_name}")