import random
from weapon import Weapon
from weapon import club, sword, m16, ray_gun  # Import the ray gun
from player import PlayerCharacter
from npc import Alien


def battle_alien(player):
    """
    Simulates a battle between the player and an Alien boss.
    The player has access to an M16 and a ray gun.
    The Alien is very difficult, with lower escape/negotiate chances
    and harsher consequences.
    """
    enemy = Alien()

    while player.hp > 0 and enemy.hp > 0:
        # Player's turn
        print("\nPlayer's turn:")
        print("Available actions:")
        print("1. Attack with Club")
        print("2. Attack with Sword")
        print("3. Attack with M16")
        print("4. Attack with Ray Gun")  # Add ray gun attack option
        print("5. Run away")
        print("6. Try to negotiate")
        print("7. Do nothing")  # Adjust choice numbers

        action_choice = input("Choose an action (1/2/3/4/5/6/7): ")

        if action_choice == "1":
            player.attack(enemy, club)
        elif action_choice == "2":
            player.attack(enemy, sword)
        elif action_choice == "3":
            player.attack(enemy, m16)
        elif action_choice == "4":
            player.attack(enemy, ray_gun)
        elif action_choice == "5":  # Run away
            escape_chance = player.special["Luck"] * 0.02  # Very low escape chance
            if random.random() < escape_chance:
                print("You successfully escaped!")
                break
            else:
                print("You failed to escape!")
                if random.random() < 0.5:  # High chance of consequence
                    print("The Alien blasts you with a powerful energy beam!")
                    player.hp -= 25  # Severe damage
        elif action_choice == "6":  # Try to negotiate
            negotiate_chance = player.special["Perception"] * 0.01  # Extremely low chance
            if random.random() < negotiate_chance:
                print("Somehow, you managed to negotiate with the Alien! It leaves peacefully.")
                break
            else:
                print("The Alien is not interested in your petty negotiations human!")
                if random.random() < 0.6:  # Very high chance of consequence
                    print("The Alien unleashes a psychic attack!")
                    if random.random() < 0.4:  # 40% chance of doing nothing
                        print("You feel a strange compulsion to do nothing...")
                        continue  # Skip to the next iteration (Alien's turn)
        elif action_choice == "7":  # Do nothing
            print("You stand motionless, leaving yourself completely vulnerable!")
            catastrophic_damage = enemy.attack(player, catastrophic=True)  # New parameter
            print(f"The Alien seizes the opportunity and deals a catastrophic blow for {catastrophic_damage} damage!")
        else:
            print("Invalid action choice!")

        if enemy.hp <= 0:
            print(f"{player.name} wins! You have defeated the Alien boss!")
            break

        # Enemy's turn
        print("\nEnemy's turn:")
        enemy.attack(player)

        if player.hp <= 0:
            print(f"{enemy.name} has beamed you up! Game Over.")
            break