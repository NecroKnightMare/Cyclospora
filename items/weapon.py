class Weapon:
    """
    Represents a weapon.
    """

    def __init__(
        self,
        name,
        damage_type,
        damage,
        range=0,
        accuracy=0.8,
        crit_chance=0.1,
        crit_multiplier=1.5,
    ):
        """
        Initializes a Weapon.

        Args:
            name (str): The name of the weapon.
            damage_type (str): The type of damage the weapon inflicts (e.g., "melee", "ballistic", "energy")
            damage (int): The base damage the weapon deals.
            range (int,): The weapon's range in units (0 for melee). Defaults to 0.
            accuracy (float): The probability of hitting the target (0.0 to 1.0).
            crit_chance (float): The probability of landing a critical hit (0.0 to 1.0).
            crit_multiplier (float): The damage multiplier for critical hits.
        """
        self.name = name
        self.damage_type = damage_type
        self.damage = damage
        self.range = range
        self.accuracy = accuracy
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier


club = Weapon(
    name="Club",
    damage_type="melee",
    damage=5
    )

sword = Weapon(
    name="Excalibur",
    damage_type="melee",
    damage=10,
    crit_chance=0.15
    )

bow = Weapon(
name="Bow",
damage_type="ballistic",
damage=7,
range=5,
accuracy=0.75
)

musket = Weapon(
    name="Musket",
    damage_type="ballistic",
    damage=15,
    range=10,
    accuracy=0.6,
    crit_chance=0.2,
)

m1_garand = Weapon(
    name="M1 Garand",
    damage_type="ballistic",
    damage=20,
    range=15,
    accuracy=0.7,
    crit_chance=0.25,
)

ray_gun = Weapon(
    name="Ray Gun",
    damage_type="energy",
    damage=12,
    range=8,
    accuracy=0.9
    )
