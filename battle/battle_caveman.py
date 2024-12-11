import random
from items.weapon import club
from characters.player import PlayerCharacter
from characters.npc import Caveman
import pygame

from characters.npc import health_roll

from decorators import game_over_check


@game_over_check
def battle_caveman(player):
    """
    Simulates a battle between the player and a Caveman.
    """
    enemy = Caveman()  # Create the Caveman enemy

    health_roll()

    pygame.init()
    pygame.mixer.init()

    club_hit_sound = pygame.mixer.Sound('Sounds/CyclosporaSFX/Bonk Sound Effect.mp3')


    while player.hp > 0 and enemy.hp > 0:
        # Player's turn
        print("\nPlayer's turn:")
        print("Available actions:")
        print("1. Attack with Club")
        print("2. Run away") 
        print("3. Try to reason")
        print("4. Do nothing")

        action_choice = input("Choose an action (1/2/3/4): ")

        if action_choice == "1":
            player.attack(enemy, club)
            club_hit_sound.play()
        elif action_choice == "2":
            print("You try to run away...")
            escape_chance = player.special["Luck"] * 0.1  # 10% per Luck point
            if random.random() < escape_chance:
                print("You successfully escaped!")
                break
            else:
                print("You failed to escape!")
        elif action_choice == "3":
            print("You try to reason with the Caveman...")
            reasoning_chance = player.special["Perception"] * 0.05  # 5% per Perception
            if random.random() < reasoning_chance:
                print("You successfully reasoned with the Caveman! He leaves peacefully, surprisingly.")
                break
            else:
                print("The Caveman doesn't understand you cause he's a caveman with very limited\
                    communication skills and attacks!")
        elif action_choice == "4":
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
            print(f"{enemy.name} killed yo ass!")
            break


if __name__ == "__main__":
    player_name = input("Enter your character's name: ")
    player = PlayerCharacter(player_name, 100, 10)

    # Start the battle! 
    battle_caveman(player)