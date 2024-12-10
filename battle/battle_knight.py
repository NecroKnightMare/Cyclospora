import random
from items.weapon import club, sword
from characters.player import PlayerCharacter
from characters.npc import Knight
from characters.npc import health_roll


def battle_knight(player):
    """
    Simulates a battle between the player and a Knight.
    The player is granted a sword for this battle.
    """
    enemy = Knight()
    health_roll()
    
    while player.hp > 0 and enemy.hp > 0:
        # Player's turn
        print("\nPlayer's turn:")
        print("Available actions:")
        print("1. Attack with Club")
        print("2. Attack with Sword")  # Add sword, should we keep all the weapons acquired throughout?
        print("3. Run away")
        print("4. Try to intimidate")
        print("5. Do nothing")

        action_choice = input("Choose an action (1/2/3/4/5): ")

        if action_choice == "1":
            player.attack(enemy, club)
        elif action_choice == "2":  # Attack with sword
            player.attack(enemy, sword)
        elif action_choice == "3":
            escape_chance = player.special["Luck"] * 0.1
            if random.random() < escape_chance:
                print("You successfully escaped!")
                break
            else:
                print("You failed to escape!")
                if random.random() < 0.05:  # 5% chance to be killed
                    print(f"{enemy.name} strikes you down as you try to flee!")
                    player.hp = 0  # Instantly kill the player
                    break
        elif action_choice == "4":
            intimidate_chance = player.special["Strength"] * 0.05
            if random.random() < intimidate_chance:
                print("You successfully intimidated the Knight! He backs down.")
                break
            else:
                print("The Knight is not intimidated and attacks!")
                if random.random() < 0.2:  # 20% chance for a critical hit
                    crit_damage = enemy.attack(player, critical_hit=True)  # Force a crit
                    print(f"{enemy.name} lands a critical hit for {crit_damage} damage!")
        elif action_choice == "5":
            print("You do nothing. That was silly")
        else:
            print("Invalid action choice!")

        if enemy.hp <= 0:
            print(f"{player.name} wins!")
            break

        # Enemy's turn
        print("\nEnemy's turn:")
        enemy.attack(player)

        if player.hp <= 0:
            print(f"{enemy.name} has slain you!")
            break