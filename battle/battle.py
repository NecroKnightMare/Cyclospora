import pygame
import random


def start_battle(player, enemy):
    # Initialize battle variables
    battle_active = True
    battle_turn = "player"
    selected_action = 0
    
    while battle_active:
        if battle_turn == "player":
            handle_player_turn(player, enemy, selected_action)
        else:
            handle_enemy_turn(player, enemy)
        
        battle_active = check_battle_end(player, enemy)
        
        if battle_active:
            battle_turn = "enemy" if battle_turn == "player" else "player"
            selected_action = 0

def handle_player_turn(player, enemy, selected_action):
    battle_actions = ["Attack", "Run away", "Try to reason", "Do nothing"]

    if selected_action == 0:
        player.attack(enemy)
    elif selected_action == 1:
        if random.random() < player.special["Luck"] * 0.1:
            print("You successfully escaped!")
            return False
        else:
            print("You failed to escape!")
    elif selected_action == 2:
        if random.random() < player.special["Perception"] * 0.05:
            print("You successfully reasoned with the enemy!")
            return False
        else:
            print(f"The {enemy.name} doesn't understand you.")
    elif selected_action == 3:
        print("You do nothing.")
    
    return True

def handle_enemy_turn(player, enemy, battle_log):
        damage = random.randint(enemy.weapon["Damage"][0], enemy.weapon["Damage"][1])
        battle_log.append(f"{enemy.name} attacks Player with {enemy.weapon['Name']} for {damage} damage!")

def check_battle_end(player, enemy, battle_log):
    if player.hp <= 0:
        battle_log.append("You were defeated! Game over.")
        return False
    elif enemy.hp <= 0:
        battle_log.append(f"You defeated the {enemy.name}!")
        return False
    return True

def render_battle_screen(screen, font, text_color, player, enemy, battle_turn, battle_actions, selected_action, battle_log):
    if player is None or enemy is None:
        print("Error: Player or enemy is None")
        return
    pygame.draw.rect(screen, (0, 0, 0), (50, 400, 700, 200))
    # Display battle log
    log_y = 400  # Adjust the starting y-position as needed
    for message in battle_log:
        log_text = font.render(message, True, text_color)
        screen.blit(log_text, (50, log_y))
        log_y += log_text.get_height() + 5
    
    # Draw player health bar
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 200, 20))  # Background
    pygame.draw.rect(screen, (0, 255, 0), (50, 50, (player.hp / player.max_hp) * 200, 20))  # Health bar

    player_health_text = font.render(f"Player HP: {player.hp}/{player.max_hp}", True, text_color)
    screen.blit(player_health_text, (50, 30))
    
    # Draw enemy health bar
    pygame.draw.rect(screen, (255, 0, 0), (400, 50, 200, 20))  # Background
    pygame.draw.rect(screen, (0, 255, 0), (400, 50, (enemy.hp / enemy.max_hp) * 200, 20))  # Health bar
    
    enemy_health_text = font.render(f"{enemy.name} HP: {enemy.hp}/{enemy.max_hp}", True, text_color)
    screen.blit(enemy_health_text, (400, 30))
    
    # Display current turn
    turn_text = font.render(f"Turn: {battle_turn.capitalize()}", True, text_color)
    screen.blit(turn_text, (50, 100))
    
    # Display available actions
    action_text = font.render("Available actions:", True, text_color)
    screen.blit(action_text, (50, 150))
    
    # Draw action buttons
    for i, action in enumerate(battle_actions):
        pygame.draw.rect(screen, (255, 0, 0), (100, 200 + i * 50, 200, 40))  # Button background
        action_text = font.render(action, True, text_color)
        screen.blit(action_text, (110, 210 + i * 50))
        if i == selected_action:
            pygame.draw.rect(screen, (255, 255, 0), (100, 200 + i * 50, 200, 40), 3)  # Highlight selected action

    # Draw scroll indicators
    pygame.draw.polygon(screen, (255, 255, 255), [(350, 200), (370, 220), (350, 240)])
    pygame.draw.polygon(screen, (255, 255, 255), [(350, 400), (370, 380), (350, 360)])
