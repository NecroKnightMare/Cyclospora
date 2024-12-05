import random
from items.weapon import club, sword, bow
from characters.player import PlayerCharacter
from characters.npc import Ninja


def battle_ninja(player):
    """
    Simulates a battle between the player and a Ninja.
    Includes consequences for failed run and negotiate attempts.
    """
    enemy = Ninja()

    while player.hp > 0 and enemy.hp > 0:
        # Player's turn
        print("\nPlayer's turn:")
        print("Available actions:")
        print("1. Attack with Club")
        print("2. Attack with Sword")
        print("3. Attack with Bow")
        print("4. Run away")
        print("5. Try to negotiate")
        print("6. Do nothing")

        action_choice = input("Choose an action (1/2/3/4/5/6): ")

        if action_choice == "1":
            player.attack(enemy, club)
        elif action_choice == "2":
            player.attack(enemy, sword)
        elif action_choice == "3":
            player.attack(enemy, bow)
        elif action_choice == "4":  # Run away
            escape_chance = player.special["Luck"] * 0.1
            if random.random() < escape_chance:
                print("You successfully escaped!")
                break
            else:
                print("You failed to escape!")
                if random.random() < 0.15:  # 15% chance of lethal ninja star
                    print("A ninja star finds its mark in your back as you flee!")
                    player.hp = 0
                    break
        elif action_choice == "5":  # Try to negotiate
            negotiate_chance = player.special["Perception"] * 0.05
            if random.random() < negotiate_chance:
                print("You successfully negotiated with the Ninja! He disappears into the shadows.")
                break
            else:
                print("The Ninja ignores your attempts at negotiation!")
                if random.random() < 0.15:  # 15% chance of critical hit
                    crit_damage = enemy.attack(player, critical_hit=True)  # Force a crit
                    print(f"{enemy.name} lands a critical hit for {crit_damage} damage!")
        elif action_choice == "6":
            print("You do nothing.")
        else:
            print("Invalid action choice!")

        if enemy.hp <= 0:
            print(f"{player.name} wins!")
            break

        # Enemy's turn
        print("\nEnemy's turn:")
        enemy.attack(player)

        if player.hp <= 0:
            print(f"{enemy.name} has vanished you from this plane of existence!")
            break