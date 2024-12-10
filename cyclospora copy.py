
import random
import time
from battle.battle import start_battle, render_battle_screen
from characters.player import PlayerCharacter, Creature
from characters.npc import Caveman, Knight, Ninja, British_Soldier, Nazi_Soldier, Alien
import pygame
import sys

class ScrollingText:
    def __init__(self, text, font, color, screen_width, screen_height, scroll_speed=1, line_spacing=50):
        self.text = text
        self.font = font
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.scroll_speed = scroll_speed
        self.line_spacing = line_spacing
        self.text_surface = self.render_text()
        self.y = 0

    def render_text(self):
        lines = self.text.split('\n')
        max_width = self.screen_width - 25  # Leave some margin on the sides
        total_height = 0
        for line in lines:
            width, height = self.font.size(line)
            total_height += height + self.line_spacing

        surface = pygame.Surface((max_width, total_height), pygame.SRCALPHA)
        y = 0
        for line in lines:
            text_surface = self.font.render(line, True, self.color)
            surface.blit(text_surface, (0, y))
            y += text_surface.get_height() + self.line_spacing

        return surface

    def update(self):
        self.y -= self.scroll_speed
        if self.y < -self.text_surface.get_height():
            self.y = 0

    def draw(self, screen):
        screen.blit(self.text_surface, (self.screen_width // 2 - self.text_surface.get_width() // 2, self.y))

def start_game():
    global player, enemy, battle_turn
    pygame.init()
    pygame.mixer.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Cyclospora")

    font = pygame.font.Font(None, 36)
    text_color = (255, 255, 255)

    # Load images
    main_menu_image = pygame.image.load("images/main.jpeg").convert()
    intro_image = pygame.image.load("images/deaths_via_berry.jpg").convert()
    stone_age_bg = pygame.image.load("images/caveman-bg.jpg").convert()
    battle_bg = pygame.Surface((screen_width, screen_height))
    battle_bg.fill((128, 128, 128))  # Gray background for battle scene

    main_menu_image = pygame.transform.scale(main_menu_image, (screen_width, screen_height))
    intro_image = pygame.transform.scale(intro_image, (screen_width, screen_height))
    stone_age_bg = pygame.transform.scale(stone_age_bg, (screen_width, screen_height))

    # Load sounds
    intro_music = pygame.mixer.Sound("Ambience/ObservingTheStar.ogg")
    stone_age_music = pygame.mixer.Sound("Ambience/caveman-bg.ogg")
    battle_music = pygame.mixer.Sound("Ambience/ST_1_Fight(wave).wav")
    club_hit_sound = pygame.mixer.Sound('Sounds/CyclosporaSFX/Bonk Sound Effect.mp3')

    # Text-related variables
    text_lines = [
        "Cyclospora",
        "In recent events, there has been an outbreak.",
        "A parasitic contamination of our local berries",
        "including; blueberries, raspberries, blackberries and strawberries",
        "Ugh, I'm starving....",
        "What's in the fridge?",
        "You walk into the kitchen and open the fridge",
        "You see there's nothing to prepare for breakfast,",
        "Well there's a boysenberry pie your neighbor brought over,",
        "that definitely looks older than a week",
        "Well it's not the worst thing I've eaten...",
        "I should at least try it to be respectful",
        "As you munch on the pie, you remember the news and think...",
        "Did the news say boysenberry?...",
        "Meh. Should be fine.",
        "(You've eaten the pie)",
        "That wasn't too bad",
        "Ugh, spoke too soon...",
        "(Stomach starts bubbling and hurting)",
        "ugh...I think I'll sleep it off...",
        "You lay down..."
    ]
    stone_age_text_lines = [
        "(There's an unfamiliar cold hard surface that you knew couldn't be you're bed)",
        "Oww, my back...",
        "(As you start adjusting yourself to your surroundings, You see foliage and start hearing loud noises you feel like you've heard in a movie)",
        "What the....",
        "(You shoot up and start scrambling around)",
        "How did I get here?!",
        "Am I dreaming?",
        "(As you look around you see what you believe to be a man)",
        "Excuse Me!",
        "(He notices you and starts sprinting with explosive power towards you)"
    ]

    # Game variables
    current_scene = "main_menu"
    player = None
    menu_options = ["Play", "Quit"]
    selected_option = 0

    # Scrolling text objects
    intro_text = ScrollingText('\n'.join(text_lines), font, text_color, screen_width, screen_height, scroll_speed=1, line_spacing=180)
    stone_age_text = ScrollingText('\n'.join(stone_age_text_lines), font, text_color, screen_width, screen_height, scroll_speed=1, line_spacing=180)

    # Battle variables
    battle_active = False
    enemy = None
    battle_turn = "player"
    battle_actions = ["Attack", "Run away", "Try to reason", "Do nothing"]
    selected_action = 0

    # --- Game loop ---
    running = True
    clock = pygame.time.Clock()
    while running:
        # 1. Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:  
                    selected_option = (selected_option + 1) % len(menu_options)
                    selected_action = (selected_action + 1) % len(battle_actions)
                elif event.key == pygame.K_UP:  
                    selected_option = (selected_option - 1) % len(menu_options)
                    selected_action = (selected_action - 1) % len(battle_actions)
                elif event.key == pygame.K_RETURN:  
                    if selected_option == 0:  
                        current_scene = "intro"
                    elif selected_option == 1:  
                        running = False
                elif event.key == pygame.K_SPACE and current_scene == "battle":
                    handle_battle_action()

        # 2. Update game state
        if current_scene == "intro":
            if intro_text.y == 0:  
                intro_music.play(-1)
            intro_text.update()
            if intro_text.y == 0:
                current_scene = "stone_age"
                intro_music.stop()
        elif current_scene == "stone_age":
            if stone_age_text.y == 0:  
                stone_age_music.play(-1)
            stone_age_text.update()
            if stone_age_text.y == 0:
                player = PlayerCharacter("You", 100, 10)
                enemy = Caveman()
                battle_turn = "player"
                start_battle()
                current_scene = "battle"
                stone_age_music.stop()
                battle_music.play(-1)
        elif current_scene == "battle":
            if player is None:
                player = PlayerCharacter("You", 100, 10)
            update_battle_state()
            check_battle_end()

        # 3. Render
        screen.fill((0, 0, 0))  # Clear the screen with a black background

        if current_scene == "main_menu":
            screen.blit(main_menu_image, (0, 0))
            for i, option in enumerate(menu_options):
                text_surface = font.render(option, True, text_color)
                text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2 + i * 50))
                if i == selected_option:  
                    pygame.draw.rect(screen, (255, 0, 0), text_rect.inflate(20, 10))  
                screen.blit(text_surface, text_rect)
        elif current_scene == "intro":
            screen.blit(intro_image, (0, 0))
            intro_text.draw(screen)
        elif current_scene == "stone_age":
            screen.blit(stone_age_bg, (0, 0))
            stone_age_text.draw(screen)
        elif current_scene == "battle":
            render_battle_screen(screen, font, text_color, player, enemy, battle_turn, battle_actions, selected_action)
        elif current_scene == "game_over":
            screen.fill((0, 0, 0))
            if player.hp > 0:
                game_over_text = font.render("You defeated the enemy! Congratulations!", True, text_color)
            else:
                game_over_text = font.render("The enemy defeated you. Game over.", True, text_color)
            screen.blit(game_over_text, (50, screen_height // 2))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def start_battle():
    global player, enemy, battle_active
    if player is None:
        player = PlayerCharacter("You", 100, 10)
    enemy = choose_enemy()
    battle_active = True

def choose_enemy():
    enemies = [Caveman(), Knight(), Ninja(), British_Soldier(), Nazi_Soldier(), Alien()]
    return random.choice(enemies)

def handle_battle_action():
    global battle_turn, current_scene, selected_action
    if battle_turn == "player":
        if selected_action == 0:
            player.attack(enemy)
        elif selected_action == 1:
            if random.random() < player.special["Luck"] * 0.1:
                print("You successfully escaped!")
                current_scene = "stone_age"
                return
            else:
                print("You failed to escape!")
        elif selected_action == 2:
            if random.random() < player.special["Perception"] * 0.05:
                print("You successfully reasoned with the enemy!")
                current_scene = "stone_age"
                return
            else:
                print(f"The {enemy.name} doesn't understand you.")
        elif selected_action == 3:
            print("You do nothing.")
        battle_turn = "enemy"

def update_battle_state():
    global battle_turn, player, enemy
    if battle_turn == "enemy":
        enemy.attack(player)
        battle_turn = "player"

def check_battle_end():
    global battle_active, current_scene
    if player.hp <= 0:
        print("You were defeated! Game over.")
        battle_active = False
        current_scene = "game_over"
    elif enemy.hp <= 0:
        print(f"You defeated the {enemy.name}!")
        battle_active = False
        current_scene = "stone_age"

if __name__ == "__main__":
    start_game()


#     def Travel_CastleCamelot():
#         print("(Your head is pounding and your arms and legs are aching)");
#         #time.sleep(3);
#         print("Damn it...(You hold your head in your hands)");
#         #time.sleep(3);
#         print("(As you lay in pain from the unexpected battle, the sound of metal clanging together gets louder and louder)")
#         time.sleep(5);
#         print("HARK!! Who goes there?!");
#         #time.sleep(2);
#         print("(You hurriedly stand up and adrenaline courses through you're veins. As you look around, you notice your in some medeival era)");
#         time.sleep(5);
#         print("Please, not again");

#         player = PlayerCharacter("You", 110, 15)
#         battle_knight(player)
#         #time.sleep(3);

#     def Travel_RedDistrict():
#         #time.sleep(2);
#         print("WHY IS THIS HAPPENING TO ME?!");
#         #time.sleep(2);
#         print("(You start trembling with anger and feelings of helplessness...)");
#         #time.sleep(3);
#         print("Where am I now?!");
#         #time.sleep(2);
#         print("(YOu hear a commotion to your left and see  Geisha in the midst of a crowd walking , almost like a parade)");
#         #time.sleep(3);
#         print("(The lights start turning on and the sun is setting, you realize it's getting dark out)");
#         #time.sleep(2);
#         print("Crap, gotta find somewhere to sleep");
#         #time.sleep(2);
#         print("(You wonder the district and see food vendors and the area becoming livelier)");
#         time.sleep(4);
#         print("(You're stomach still hurts from that pie you ate. But you feel an insatuated hunger)");
#         time.sleep(5);
#         print("Can I get some food please?(You ask a vendor, she clearly doesn't understand you)");
#         #time.sleep(3);
#         print("Well damn...");
#         #time.sleep(2);
#         print("Well maybe if I...(You start to rummage your pockets and pull out your wallet. The vendor starts to panic)");
#         time.sleep(6);
#         print("(You gaze to see what she's fretting about. As you try to see where your gaze ends, you realize it's the weapons you've collected along the way. )");
#         #time.sleep(3);
#         print("(You're shocked, and start explaining that you mean no harm, but fail)");
#         time.sleep(4);
#         print("(Some person you can only describe as a stereotypical ninja approaches you with sword drawn.)")

#         player = PlayerCharacter("You", 115, 20)
#         battle_ninja(player)

#         print("(You quickly put your weapon away, back up and sheathe it and apologize profusely to the lady and wander away from the body you just left in the street.)");
#         #time.sleep(3);
#         print("(After panic walking away from the murder you just commited. You find another vender and ask about a nearby inn. She seems to understand and points you in the direction of an Inn)");
#         #time.sleep(3);
#         print("(You thank her and start walking towards the Inn, as you walk you begin to feel light-headed and blackout again.)"); 
#         time.sleep(4);

#         Travel_Lexington

#     def Travel_Lexington():
#         print("(You awake and look around, you notice a city-scape bombed to a point it resembled rubble more than a city.)");
#         #time.sleep(3);
#         print("Halt! You there!");
#         #time.sleep(2);
#         print("(You stop and slowly turn around)");
#         #time.sleep(2);
#         print("(You are face to face with a Nazi soldier, obviously there isn't much to say at this point, you look to your right and find a discarded rifle, pick it up and point)");

#         player = PlayerCharacter("You", 120, 25)
#         battle_nazi(player)

#         print("(Well, that one doesn't feel as bad as the previous ones. That was a choice.)");
#         #time.sleep(2);
#         print("(You begin to look around, you debate just laying down and waiting for the next one to happen. You're just guessing at this point.)");
#         #time.sleep(2);
#         print("(You lay down to go to sleep)");
#         #time.sleep(3);
#         print("(You start to feel light headed)");
#         #time.sleep(2);
#         print("Here we go again...");
#         #time.sleep(2);

#     def Travel_WW2():
#         print("(You awaken to the sound of cars and people talking)");
#         #time.sleep(3);
#         print("(You look around and realize you're in a modern city)");
#         #time.sleep(2);
#         print("Where am I now?");
#         #time.sleep(2);
#         print("(You see a soldier patrolling the street)");
#         #time.sleep(2);
#         print("Hey, you! Stop right there!");
#         #time.sleep(3)
#         print("(You realize you're just a dude holding a bunch of weapons in the middle of what appears to be the United Kingdom. They don't like guns and obviously do not like you right now.)")

#         player = PlayerCharacter("You", 125, 30)
#         battle_british_soldier(player)

#         print("Well, guess I'm just a murderer now with some kind of berry monster helping me commit more crimes in various ages.");
#         #time.sleep(3);
#         print("(You begin to wander off attempting to hide somewhere not in the middle of the street. You find yourself wandering down an alley.)");
#         #time.sleep(3);
#         print("(At the end of the alley, a bright light suddenly bursts out of the wall. It resembles a portal that you would see in Star Trek or something else sci-fi.)");
#         #time.sleep(3);
#         print("Well guess I really don't have much to lose now.");
#         #time.sleep(3);
#         print("(You reload your rifle, take a look around and walk through the portal.)");

#     def Travel_AlienWorld():
#         print("(You step through the portal and find yourself on an alien planet)");
#         #time.sleep(3);
#         print("(The landscape is strange and unfamiliar)");
#         #time.sleep(2);
#         print("(You see an Alien approaching)");
#         #time.sleep(2);

#         player = PlayerCharacter("You", 130, 35)
#         battle_alien(player)

#         # ... (Ending sequence thats super cool with blood and victory)


#     # Call the travel functions
#     #Travel_StoneAge()
#     Travel_CastleCamelot()
#     Travel_RedDistrict()
#     Travel_Lexington()
#     Travel_WW2()
#     Travel_AlienWorld()

# pygame.quit()

# if __name__ == "__main__":
#     start_game()
