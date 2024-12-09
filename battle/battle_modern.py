import random
from items.weapon import club, sword, m16
from characters.player import PlayerCharacter
from characters.npc import British_Soldier
from decorators import game_over_check
import pygame


game_over_check
def battle_british_soldier(player):
    """
    Simulates a battle between the player and a British Soldier.
    The player is granted an M16 for this battle.
    The British Soldier is from the modern era and more dangerous.
    Running away is harder, and failed negotiation has worse consequences.
    """
    enemy = British_Soldier()

    while player.hp > 0 and enemy.hp > 0:
        # Player's turn
        print("\nPlayer's turn:")
        print("Available actions:")
        print("1. Attack with Club")
        print("2. Attack with Sword")
        print("3. Attack with M16")  # Update to M16 attack option
        print("4. Run away")
        print("5. Try to negotiate")
        print("6. Do nothing")

        action_choice = input("Choose an action (1/2/3/4/5/6): ")

        if action_choice == "1":
            player.attack(enemy, club)
        elif action_choice == "2":
            player.attack(enemy, sword)
        elif action_choice == "3":  # Attack with M16
            player.attack(enemy, m16)
        elif action_choice == "4":
            escape_chance = player.special["Luck"] * 0.05
            if random.random() < escape_chance:
                print("You successfully escaped!")
                break
            else:
                print("You failed to escape!")
                if random.random() < 0.3:
                    print("The British Soldier shoots you as you try to run!")
                    player.hp -= 15
        elif action_choice == "5":
            negotiate_chance = player.special["Perception"] * 0.03
            if random.random() < negotiate_chance:
                print("You successfully negotiated with the British Soldier! He lowers his weapon.")
                break
            else:
                print("The British Soldier is not interested in negotiating!")
                if random.random() < 0.5:
                    print("The British Soldier calls for reinforcements!")
                    # ... (Add logic to spawn more enemies or increase difficulty)
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
            print(f"{enemy.name} has redcoated you!")
            break