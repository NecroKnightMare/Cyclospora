import random
from items.weapon import club, sword, m1_garand
from characters.player import PlayerCharacter
from characters.npc import Nazi_Soldier


def battle_nazi(player):
    """
    Simulates a battle between the player and a Nazi Soldier.
    The player is granted an M1 Garand for this battle.
    """
    enemy = Nazi_Soldier()

    while player.hp > 0 and enemy.hp > 0:
        # Player's turn
        print("\nPlayer's turn:")
        print("Available actions:")
        print("1. Attack with Club")
        print("2. Attack with Sword")
        print("3. Shoot with M1 Garand")  # Added M1 Garand
        print("4. Run away *10 percent chance of being captured and killed")
        print("5. Try to reason")
        print("6. Do nothing")

        action_choice = input("Choose an action (1/2/3/4/5/6): ")

        if action_choice == "1":
            player.attack(enemy, club)
        elif action_choice == "2":
            player.attack(enemy, sword)
        elif action_choice == "3":
            player.attack(enemy, m1_garand)
        elif action_choice == "4":
            escape_chance = player.special["Luck"] * 0.1
            if random.random() < escape_chance:
                print("You successfully escaped!")
                break
            else:
                print("You failed to escape!")
                if random.random() < 0.1:  # 10% chance to be captured and killed
                    print(f"{enemy.name} manages to capture you as you try to flee!")
                    player.hp = 0  # Since you're captured, it kills ya. Sad.
                    break
        elif action_choice == "5":
            reasoning_chance = player.special["Perception"] * 0.05
            if random.random() < reasoning_chance:
                print("You successfully reasoned with the Nazi Soldier! He stands down.")
                break
            else:
                print("The Nazi Soldier is not persuaded and attacks!")
                if random.random() < 0.2:  # 20% chance for a critical hit
                    crit_damage = enemy.attack(player, critical_hit=True)  # Force a crit
                    print(f"{enemy.name} You can't speak german at all,\
                        you take a critical hit for {crit_damage} damage!")
        elif action_choice == "6":
            print("You do nothing.")
        else:
            print("Invalid action choice!")

        if enemy.hp <= 0:
            print(f"{player.name} wins! American loses.")
            break

        # Enemy's turn
        print("\nEnemy's turn:")
        enemy.attack(player)  # Nazi Soldier will use their Luger pistol

        if player.hp <= 0:
            print(f"{enemy.name} has killed you! You have failed your country\
                and the parasite which sent you back in time.")
            break