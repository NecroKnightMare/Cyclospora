
import random
import time
from battle import battle_caveman
from battle import battle_knight
from battle import battle_modern
from battle import battle_nazi
from battle import battle_ninja
from battle import battle_alien
from characters.player import PlayerCharacter

def start_game():
    print("Cyclospora");
    time.sleep(3);
    print("In recent events, there has been an outbreak of parasitic contamination of our local berries including; blueberries, raspberries, blackberries and strawberries to name a few");
    time.sleep(3);
    print("Ugh, I'm starving....");
    time.sleep(3);
    print("What's in the fridge?")
    time.sleep(3);
    print("You walk into the kitchen and open the fridge");
    time.sleep(1);
    print("You see there's nothing to prepare for breakfast, other than a boysenberry pie your neighbor brought over, that looked older tha a week old");
    time.sleep(2);
    print("Well it's not the worst thing I've eaten and I need to at least eat it to be respectful");
    time.sleep(2);
    print("As you munch on the pie, you remember the news and say...");
    time.sleep(1);
    print("Did the news say boysenberry?")
    time.sleep(3);
    print("Meh. Should be fine.");
    time.sleep(2);
    print("You've eaten the pie");
    time.sleep(2);
    print("That wasn't too bad");
    time.sleep(2);
    print("Ugh, spoke too soon...");
    time.sleep(2);
    print("(Stomach starts bubbling and hurting)");
    time.sleep(2);
    print("ugh...I think I'll sleep it off...");
    time.sleep(2);
    print("You lay down");
    time.sleep(3);

    def Travel_StoneAge():
        print("(There's an unfamiliar cold hard surface that you knew couldn't be you're bed)");
        time.sleep(3);
        print("Oww, my back...");
        time.sleep(2);
        print("(As you start adjusting yourself to your surroundings, You see foliage and start hearing loud noises you feel like you've heard in a movie)")
        time.sleep(3);
        print("What the....");
        time.sleep(1);
        print("(You shoot up and start scrambling around)");
        time.sleep(2);
        print("How did I get here?!");
        time.sleep(3);
        print("Am I dreaming?");
        time.sleep(2);
        print("(As you look around you see what you believe to be a man)");
        time.sleep(3);
        print("Excuse Me!");
        time.sleep(2);
        print("(He notices you and starts sprinting with explosive power towards you");

        battle_caveman(player);

    def Travel_CastleCamelot():
        print("(Your head is pounding and your arms and legs are aching)");
        time(3);
        print("Damn it...(You hold your head in your hands)");
        time.sleep(3);
        print("(As you lay in pain from the unexpected battle, the sound of metal clanging together gets louder and louder)")
        time.sleep(5);
        print("HARK!! Who goes there?!");
        time.sleep(2);
        print("(You hurriedly stand up and adrenaline courses through you're veins. As you look around, you notice your in some medeival era)");
        time.sleep(5);
        print("Please, not again");
        
        battle_knight(player);
        time.sleep(3);

    def Travel_RedDistrict():
        time.sleep(2);
        print("WHY IS THIS HAPPENING TO ME?!");
        time.sleep(2);
        print("(You start trembling with anger and feelings of helplessness...)");
        time.sleep(3);
        print("Where am I now?!");
        time.sleep(2);
        print("(A Geisha in the midst of a crowd starts walking , almost like a parade)");
        time.sleep(3);
        print("(The sun setting, you realize it's getting dark out)");
        time.sleep(2);
        print("Crap, gotta find somewhere to sleep");
        time.sleep(2);
        print("(You wonder the district and see food vendors and the area becoming livelier)");
        time.sleep(4);
        print("(You're stomach still hurts from that pie you ate. But you feel an insatuated hunger)");
        time.sleep(5);
        print("Can I get some food please?(You ask a vendor, she clearly doesn't understand you)");
        time.sleep(3);
        print("Well damn...");
        time.sleep(2);
        print("Well maybe if I...(You start to rummage your pockets and pull out your wallet, with your wallet drops a pocket knife)");
        time.sleep(6);
        print("I had that with me too? (You unsheath it and the vendor yells)");
        time.sleep(3);
        print("(You're shocked, and start explaining that you mean no harm, but fail )");
        time.sleep(4);
        print("(Some person you can only describe as a stereotypical ninja approaches you with sword drawn.)")
        battle_ninja(player);  # Ninja battle here

        print("(You quickly pick the knife back up and sheathe it and apologize profusely to the lady and wander away from the body you just left in the street.)");
        time.sleep(3);
        print("(After panic walking away from the murder you just commited. You find another vender and ask about a nearby inn. She seems to understand and points you in the direction of an Inn)");
        time.sleep(3);
        print("(You thank her and start walking towards the Inn, as you walk you begin to feel light-headed and blackout again.)"); 
        time.sleep(4);
        print("(You awake and look around, you notice a city-scape bombed to a point it resembled rubble more than a city.)");
        time.sleep(3);
        print("Halt! You there!");
        time.sleep(2);
        print("(You stop and slowly turn around)");
        time.sleep(2);
        print("(You are face to face with a Nazi soldier, obviously there isn't much to say at this point, you look to your right and find a discarded rifle, pick it up and point)");

        battle_nazi(player);  # Nazi battle here

        print("(Well, that one doesn't feel as bad as the previous ones. That was a choice.)");
        time.sleep(2);
        print("(You begin to look around, you debate just laying down and waiting for the next one to happen. You're just guessing at this point.)");
        time.sleep(2);
        print("(You lay down to go to sleep)");
        time.sleep(3);
        print("(You start to feel light headed)");
        time.sleep(2);
        print("Here we go again...");
        time.sleep(2);

    def Travel_ModernEra():
        print("(You awaken to the sound of cars and people talking)");
        time.sleep(3);
        print("(You look around and realize you're in a modern city)");
        time.sleep(2);
        print("Where am I now?");
        time.sleep(2);
        print("(You see a soldier patrolling the street)");
        time.sleep(2);
        print("Hey, you! Stop right there!");
        time.sleep(3)
        print("(You realize you're just a dude holding a bunch of weapons in the middle of what appears to be the United Kingdom. They don't like guns and obviously do not like you right now.)")

        battle_modern(player);

        print("Well, guess I'm just a murderer now with some kind of berry monster helping me commit more crimes in various ages.");
        time.sleep(3)
        print("(You begin to wander off attempting to hide somewhere not in the middle of the street. You find yourself wandering down an alley.)")
        time.sleep(3)
        print("(At the end of the alley, a bright light suddenly bursts out of the wall. It resembles a portal that you would see in Star Trek or something else sci-fi.)");
        time.sleep(3);
        print("Well guess I really don't have much to lose now.")
        time.sleep(3)
        print("(You reload your rifle, take a look around and walk through the portal.)")

    def Travel_AlienWorld():
        print("(You step through the portal and find yourself on an alien planet)");
        time.sleep(3);
        print("(The landscape is strange and unfamiliar)");
        time.sleep(2);
        print("(You see an Alien approaching)");
        time.sleep(2);

        battle_alien(player);  # Alien boss battle here

        # ... (Ending sequence thats super cool with blood and victory)


    # Call the travel functions
    Travel_StoneAge()
    Travel_CastleCamelot()
    Travel_RedDistrict()
    Travel_ModernEra()
    Travel_AlienWorld()

if __name__ == "__main__":
    start_game()

    




# class Creature:
#     """
#     Represents a generic creature in the RPG game.
#     """

#     def __init__(self, name, hp, ac):
#         """
#         Initializes a Creature instance.

#         Args:
#             name (str): The name of the creature.
#             hp (int): The creature's hit points.
#             ac (int): The creature's armor class.
#         """
#         self.name = name
#         self.hp = hp
#         self.ac = ac

#     def take_damage(self, damage):
#         """
#         Reduces the creature's HP by the given damage amount.
#         """
#         self.hp -= damage
#         if self.hp < 0:
#             self.hp = 0
#         print(f"{self.name} takes {damage} damage! HP: {self.hp}")

#     def attack(self, target, weapon):
#         """
#         Attacks the target creature using the specified weapon, considering S.P.E.C.I.A.L. stats.
#         """
#         if weapon.range > 0 and self.distance_to(target) > weapon.range:
#             print(f"{self.name} is too far away to attack with {weapon.name}!")
#             return

#         # Accuracy calculation
#         hit_chance = weapon.accuracy
#         if weapon.range > 0:  # Ranged weapon
#             if isinstance(self, PlayerCharacter):
#                 hit_chance += (
#                     self.special["Perception"] - 5
#                 ) * 0.05  # Adjust based on Perception which has logic I dunno yet but itsa cookin'.

#         if random.random() > hit_chance:
#             print(f"{self.name}'s attack with {weapon.name} missed!")
#             return

#         # Damage calculation
#         damage = weapon.damage
#         if weapon.damage_type == "melee" and isinstance(self, PlayerCharacter):
#             damage += (self.special["Strength"] - 5) * 2  # Adjust based on Strength

#         # Critical hit calculation (Luck influences crit chance)
#         crit_chance = weapon.crit_chance
#         if isinstance(self, PlayerCharacter):
#             crit_chance += (self.special["Luck"] - 5) * 0.01

#         if random.random() <= crit_chance:
#             damage *= weapon.crit_multiplier
#             print("Critical hit!")

#         target.take_damage(damage)
#         print(
#             f"{self.name} attacks {target.name} with {weapon.name} for {damage} damage!"
#         )

#     def distance_to(self, other):
#         """
#         Calculates the distance between this creature and another creature.

#         Args:
#             other (Creature): The other creature.

#         Returns:
#             int: The distance between the two creatures. (logic here)
#         """
#         # Placeholder- logic here which I dunno currently
#         return 5  # Assume a distance of 5 units currently until I can figure out the way to implement actual distance.


# class PlayerCharacter(Creature):
#     """
#     Represents a player-controlled character in the RPG game.
#     """

#     def __init__(self, name, hp, ac):
#         """
#         Initializes a PlayerCharacter instance.

#         Args:
#             name (str): The name of the player character.
#             hp (int): The player character's hit points.
#             ac (int): The player character's armor class.
#         """
#         super().__init__(name, hp, ac)
#         self.special = {  # S.P.E.C.I.A.L. stats, all 5 currently. Will implement some way to vary them eventually maybe.
#             "Strength": 5,
#             "Perception": 5,
#             "Endurance": 5,
#             "Charisma": 5,
#             "Intelligence": 5,
#             "Agility": 5,
#             "Luck": 5,
#         }
#         self.perks = []  # List to store acquired perks

#     def add_perk(self, perk_name):
#         """
#         Adds a perk to the player character's perk list.
#         """
#         self.perks.append(perk_name)
#         print(f"{self.name} acquired the perk: {perk_name}")


# class NPC(Creature):
#     """
#     Represents a non-player character in the RPG game.
#     """

#     def __init__(self, name, hp, ac):
#         """
#         Initializes an NPC instance.

#         Args:
#             name (str): The name of the NPC.
#             hp (int): The NPC's hit points.
#             ac (int): The NPC's armor class.
#         """
#         super().__init__(name, hp, ac)


# class FeralGhoul(NPC):
#     """
#     Represents a Feral Ghoul, a dangerous mutated creature.
#     """

#     def __init__(self, name="Feral Ghoul", hp=30, ac=6):
#         """
#         Initializes a Feral Ghoul instance.
#         """
#         super().__init__(name, hp, ac)

#     def attack(self, target):
#         """
#         Feral Ghouls have a chance to inflict radiation poisoning which will not be a good time.
#         """
#         super().attack(target, Weapon("Claws", "melee", 12))  # Base claw attack
#         if random.random() < 0.3:  # 30% chance to inflict radiation poisoning
#             target.take_damage(5)  # Additional radiation damage cause fuck you.
#             print(f"{target.name} suffers from radiation poisoning!")


# class Deathclaw(NPC):
#     """
#     Represents a Deathclaw,
#     an extremely powerful and deadly creature that will definitely kill you.
#     """

#     def __init__(self, name="Deathclaw", hp=200, ac=15):
#         """
#         Initializes a Deathclaw instance.
#         """
#         super().__init__(name, hp, ac)

#     def attack(self, target):
#         """
#         Deathclaws have a high critical hit chance and will pwn you
#         """
#         if random.random() < 0.5:  # 50% chance for power attack
#             super().attack(target, Weapon("Power Attack", "melee", 50, crit_chance=0.4))
#         else:
#             super().attack(target, Weapon("Claws", "melee", 25, crit_chance=0.2))


# class Raider(NPC):
#     """
#     This represents a raider of the wasteland, 
#     typically pretty easy to kill but has a chance
#     to inflict pretty decent damage with crits
#     """

#     def __init__(self, name="Raider", hp=75, ac=5):
#         """
#         initializes a raider instance
#         """

#         super().__init__(name, hp, ac)

#     def attack(self, target):
#         """
#         Raider has a gun and can probably kill you if you are not cool
#         """
#         if random.random() < 0.1:  # 10% chance of headshot
#             super().attack(target, Weapon("Headshot", "range", 35, crit_chance=0.1))
#         else:
#             super().attack(target, Weapon("Gunshot", "range", 15, crit_chance=0.2))


# class Weapon:
#     """
#     Represents a weapon.
#     """

#     def __init__(
#         self,
#         name,
#         damage_type,
#         damage,
#         range=0,
#         accuracy=0.8,
#         crit_chance=0.1,
#         crit_multiplier=1.5,
#     ):
#         """
#         Initializes a Weapon.

#         Args:
#             name (str): The name of the weapon.
#             damage_type (str): The type of damage the weapon inflicts (e.g., "melee", "ballistic", "energy")
#             damage (int): The base damage the weapon deals.
#             range (int,): The weapon's range in units (0 for melee). Defaults to 0.
#             accuracy (float): The probability of hitting the target (0.0 to 1.0).
#             crit_chance (float): The probability of landing a critical hit (0.0 to 1.0).
#             crit_multiplier (float): The damage multiplier for critical hits.
#         """
#         self.name = name
#         self.damage_type = damage_type
#         self.damage = damage
#         self.range = range
#         self.accuracy = accuracy
#         self.crit_chance = crit_chance
#         self.crit_multiplier = crit_multiplier


