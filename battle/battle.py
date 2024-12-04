import random
from weapon import Weapon
from weapon import club
from player import PlayerCharacter


def battle(player, enemy):
    """
    Simulates a battle between the player and an enemy which is why its named battle.
    """
    while player.hp > 0 and enemy.hp > 0:
        # Player's turn
        print("\nPlayer's turn:")
        print("Available actions:")
        print("1. Attack with Club")
        print("2. Run away")
        print("3. Negotiate")
        print("4. Do nothing")
        # ... (If I felt more creative I would add more actions. )

        action_choice = input("Choose an action (1/2/3/4): ")

        if action_choice == "1":
            player.attack(enemy, club)
        elif action_choice == "2":
            player.attack(enemy, )
        elif action_choice == "3":
            player.attack(enemy, )
        elif action_choice == "4":
            player.attack(enemy, )
        else:
            print("Invalid action choice!")

        if enemy.hp <= 0:
            print(f"{player.name} wins!")
            break

        # Enemy's turn
        print("\nEnemy's turn:")
        enemy.attack(player)  # Surprise! The enemy can attack too.

        if player.hp <= 0:
            print(f"{enemy.name} killed yo ass!")
            break


if __name__ == "__main__":
    # Create the player character
    player_name = input("Enter your character's name: ")
    player = PlayerCharacter(player_name, 100, 10)
    player.special["Strength"] = 10
    player.special["Perception"] = 9
    player.special["Luck"] = 5

    # Choose an enemy
    enemy_choice = input("Choose an enemy (Name/s): ")
    if enemy_choice == "Name here":
        enemy = ()
    elif enemy_choice == "Name here":
        enemy = ()
    elif enemy_choice == "Name Here":
        enemy = ()
    else:
        print("Invalid enemy choice!")
        exit()

    # Create weapons


    # Start the battle! or dont, its your choice I guess.
    battle(player, enemy)
