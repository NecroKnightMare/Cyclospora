import random

class Creature:
    """
    Represents a generic creature in the RPG game.
    """

    def __init__(self, name, hp, ac):
        """
        Initializes a Creature instance.

        Args:
            name (str): The name of the creature.
            hp (int): The creature's hit points.
            ac (int): The creature's armor class.
        """
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.ac = ac

    def take_damage(self, damage):
        """
        Reduces the creature's HP by the given damage amount.
        """
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} takes {damage} damage! HP: {self.hp}")

    def attack(self, target, weapon):
        """
        Attacks the target creature using the specified weapon, considering S.P.E.C.I.A.L. stats.
        """
        if weapon.range > 0 and self.distance_to(target) > weapon.range:
            print(f"{self.name} is too far away to attack with {weapon.name}!")
            return

        # Accuracy calculation
        hit_chance = weapon.accuracy
        if weapon.range > 0:  # Ranged weapon
            if isinstance(self, PlayerCharacter):
                hit_chance += (
                    self.special["Perception"] - 5
                ) * 0.05  # Adjust based on Perception which has logic I dunno yet but itsa cookin'.

        if random.random() > hit_chance:
            print(f"{self.name}'s attack with {weapon.name} missed!")
            return

        # Damage calculation
        damage = weapon.damage
        if weapon.damage_type == "melee" and isinstance(self, PlayerCharacter):
            damage += (self.special["Strength"] - 5) * 2  # Adjust based on Strength

        # Critical hit calculation (Luck influences crit chance)
        crit_chance = weapon.crit_chance
        if isinstance(self, PlayerCharacter):
            crit_chance += (self.special["Luck"] - 5) * 0.01

        if random.random() <= crit_chance:
            damage *= weapon.crit_multiplier
            print("Critical hit!")

        target.take_damage(damage)
        print(
            f"{self.name} attacks {target.name} with {weapon.name} for {damage} damage!"
        )

    def distance_to(self, other):
        """
        Calculates the distance between this creature and another creature.

        Args:
            other (Creature): The other creature.

        Returns:
            int: The distance between the two creatures. (logic here)
        """
        # Placeholder- logic here which I dunno currently
        return 5  # Assume a distance of 5 units currently until I can figure out the way to implement actual distance.


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
        self.max_hp = hp
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