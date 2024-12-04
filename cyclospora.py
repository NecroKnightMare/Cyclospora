import random

def battle(player, enemy):
    """
    Simulates a battle between the player and an enemy which is why its named battle.
    """
    while player.hp > 0 and enemy.hp > 0:
        # Player's turn
        print("\nPlayer's turn:")
        print("Available actions:")
        print("1. Attack with Combat Knife")
        print("2. Attack with Laser Rifle")
        print("3. Attack with Rifle")
        print("4. Attack with Lightsaber")
        # ... (If I felt more creative I would add more actions. )

        action_choice = input("Choose an action (1/2/3/4): ")

        if action_choice == "1":
            player.attack(enemy, knife)
        elif action_choice == "2":
            player.attack(enemy, laser_rifle)
        elif action_choice == "3":
            player.attack(enemy, rifle)
        elif action_choice == "4":
            player.attack(enemy, lightsaber)
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
    player_name = input("Enter your character's name, Nathan is a great one: ")
    player = PlayerCharacter(player_name, 100, 10)
    player.special["Strength"] = 10
    player.special["Perception"] = 9
    player.special["Luck"] = 5

    # Choose an enemy
    enemy_choice = input("Choose an enemy (raider/ghoul/deathclaw): ")
    if enemy_choice == "raider":
        enemy = Raider()
    elif enemy_choice == "ghoul":
        enemy = FeralGhoul()
    elif enemy_choice == "deathclaw":
        enemy = Deathclaw()
    else:
        print("Invalid enemy choice!")
        exit()

    # Create weapons, I dunno why I didn't create a lightsaber...jk just did.
    knife = Weapon("Combat Knife", "melee", 15)
    lightsaber = Weapon("Lightsaber", "melee", 60, range=5, accuracy=0.5, crit_chance=0.4)
    laser_rifle = Weapon(
        "Laser Rifle", "energy", 30, range=20, accuracy=0.8, crit_chance=0.2
    )
    rifle = Weapon(
        "Rusty Rifle", "ballistic", 45, range=15, accuracy=0.7, crit_chance=0.3
    )

    # Start the battle! or dont, its your choice I guess.
    battle(player, enemy)
