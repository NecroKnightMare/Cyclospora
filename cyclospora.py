from PIL import Image
import random
import time
from battle.battle_caveman import battle_caveman
from battle.battle_knight import battle_knight
from battle.battle_modern import battle_british_soldier
from battle.battle_nazi import battle_nazi
from battle.battle_ninja import battle_ninja
from battle.battle_alien import battle_alien

from characters.player import PlayerCharacter, Player

def start_game():

    def get_limited_input(prompt, max_length):
        user_input = input(prompt)
        while len(user_input) > max_length:
            print(f"Input too long! Please enter up to {max_length} characters.")
            user_input = input(prompt)
        return user_input

    player_name = get_limited_input("Enter name: ")

    # filename = "image.png"
    # with image.open(filename) as image:
    #     width, height = image.size

from characters.player import PlayerCharacter
import pygame

def start_game():
    pygame.init()
    pygame.mixer.init()

    screen_width = 800  # Adjust as needed
    screen_height = 600  # Adjust as needed
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Cyclospora")

    main_image = pygame.image.load("images/main.jpeg").convert()
    screen.blit(main_image, (0, 0))
    pygame.display.flip()
    time.sleep(3)


    # Load background music
    pygame.mixer.music.load("Ambience/ObservingTheStar.ogg")
    pygame.mixer.music.play(-1)

    intro_image = pygame.image.load("images/deaths_via_berry.jpg").convert()
    screen.blit(intro_image, (0, 0))
    pygame.display.flip()


    print("Cyclospora");
    time.sleep(3);
    print("In recent events, there has been an outbreak of parasitic contamination of our local berries including; blueberries, raspberries, blackberries and strawberries to name a few");
    time.sleep(3);
    print("Ugh, I'm starving....");
    time.sleep(3);
    print("What's in the fridge?")
    time.sleep(3);
    print("You walk into the kitchen and open the fridge");
    time.sleep(1);
    print("You see there's nothing to prepare for breakfast, other than a boysenberry pie your neighbor brought over, that looked older tha a week");
    time.sleep(2);
    print("Well it's not the worst thing I've eaten and I need to at least eat it to be respectful");
    time.sleep(2);
    print("As you munch on the pie, you remember the news and say...");
    time.sleep(1);
    print("Did the news say boysenberry?...")
    time.sleep(3);
    print("Meh. Should be fine.");
    time.sleep(2);
    print("(You've eaten the pie)");
    time.sleep(2);
    print("That wasn't too bad");
    time.sleep(2);
    print("Ugh, spoke too soon...");
    time.sleep(2);
    print("(Stomach starts bubbling and hurting)");
    time.sleep(2);
    print("ugh...I think I'll sleep it off...");
    time.sleep(2);
    print("You lay down...");

    time.sleep(3);

    def Travel_StoneAge():
        stone_age_bg = pygame.image.load("images/caveman-bg.jpg").convert()
        screen.blit(stone_age_bg, (0, 0))
        pygame.display.flip()

        pygame.mixer.music.load("Ambience/caveman-bg.ogg")
        pygame.mixer.music.play(-1)

        print("(There's an unfamiliar cold hard surface that you knew couldn't be you're bed)");
        #time.sleep(3);
        print("Oww, my back...");

        time.sleep(2);
        print("(As you start adjusting yourself to your surroundings, You see foliage and start hearing loud noises you feel like you've heard in a movie");
        time.sleep(3);

        #time.sleep(2);
        print("(As you start adjusting yourself to your surroundings, You see foliage and start hearing loud noises you feel like you've heard in a movie)")
        #time.sleep(3);

        print("What the....");
        #time.sleep(1);
        print("(You shoot up and start scrambling around)");
        #time.sleep(2);
        print("How did I get here?!");
        #time.sleep(3);
        print("Am I dreaming?");
        #time.sleep(2);
        print("(As you look around you see what you believe to be a man)");
        #time.sleep(3);
        print("Excuse Me!");
        #time.sleep(2);
        print("(He notices you and starts sprinting with explosive power towards you");

        player = PlayerCharacter("You", 100, 10)
        battle_caveman(player)

    def Travel_CastleCamelot():
        print("(Your head is pounding and your arms and legs are aching)");
        #time.sleep(3);
        print("Damn it...(You hold your head in your hands)");
        #time.sleep(3);
        print("(As you lay in pain from the unexpected battle, the sound of metal clanging together gets louder and louder)")
        time.sleep(5);
        print("HARK!! Who goes there?!");
        #time.sleep(2);
        print("(You hurriedly stand up and adrenaline courses through you're veins. As you look around, you notice your in some medeival era)");
        time.sleep(5);
        print("Please, not again");

        player = PlayerCharacter("You", 110, 15)
        battle_knight(player)
        #time.sleep(3);

    def Travel_RedDistrict():
        #time.sleep(2);
        print("WHY IS THIS HAPPENING TO ME?!");
        #time.sleep(2);
        print("(You start trembling with anger and feelings of helplessness...)");
        #time.sleep(3);
        print("Where am I now?!");
        #time.sleep(2);
        print("(YOu hear a commotion to your left and see  Geisha in the midst of a crowd walking , almost like a parade)");
        #time.sleep(3);
        print("(The lights start turning on and the sun is setting, you realize it's getting dark out)");
        #time.sleep(2);
        print("Crap, gotta find somewhere to sleep");
        #time.sleep(2);
        print("(You wonder the district and see food vendors and the area becoming livelier)");
        time.sleep(4);
        print("(You're stomach still hurts from that pie you ate. But you feel an insatuated hunger)");
        time.sleep(5);
        print("Can I get some food please?(You ask a vendor, she clearly doesn't understand you)");
        #time.sleep(3);
        print("Well damn...");
        #time.sleep(2);
        print("Well maybe if I...(You start to rummage your pockets and pull out your wallet. The vendor starts to panic)");
        time.sleep(6);
        print("(You gaze to see what she's fretting about. As you try to see where your gaze ends, you realize it's the weapons you've collected along the way. )");
        #time.sleep(3);
        print("(You're shocked, and start explaining that you mean no harm, but fail)");
        time.sleep(4);
        print("(Some person you can only describe as a stereotypical ninja approaches you with sword drawn.)")

        player = PlayerCharacter("You", 115, 20)
        battle_ninja(player)

        print("(You quickly put your weapon away, back up and sheathe it and apologize profusely to the lady and wander away from the body you just left in the street.)");
        #time.sleep(3);
        print("(After panic walking away from the murder you just commited. You find another vender and ask about a nearby inn. She seems to understand and points you in the direction of an Inn)");
        #time.sleep(3);
        print("(You thank her and start walking towards the Inn, as you walk you begin to feel light-headed and blackout again.)"); 
        time.sleep(4);

        Travel_Lexington

    def Travel_Lexington():
        print("(You awake and look around, you notice a city-scape bombed to a point it resembled rubble more than a city.)");
        #time.sleep(3);
        print("Halt! You there!");
        #time.sleep(2);
        print("(You stop and slowly turn around)");
        #time.sleep(2);
        print("(You are face to face with a Nazi soldier, obviously there isn't much to say at this point, you look to your right and find a discarded rifle, pick it up and point)");

        player = PlayerCharacter("You", 120, 25)
        battle_nazi(player)

        print("(Well, that one doesn't feel as bad as the previous ones. That was a choice.)");
        #time.sleep(2);
        print("(You begin to look around, you debate just laying down and waiting for the next one to happen. You're just guessing at this point.)");
        #time.sleep(2);
        print("(You lay down to go to sleep)");
        #time.sleep(3);
        print("(You start to feel light headed)");
        #time.sleep(2);
        print("Here we go again...");
        #time.sleep(2);

    def Travel_WW2():
        print("(You awaken to the sound of cars and people talking)");
        #time.sleep(3);
        print("(You look around and realize you're in a modern city)");
        #time.sleep(2);
        print("Where am I now?");
        #time.sleep(2);
        print("(You see a soldier patrolling the street)");
        #time.sleep(2);
        print("Hey, you! Stop right there!");
        #time.sleep(3)
        print("(You realize you're just a dude holding a bunch of weapons in the middle of what appears to be the United Kingdom. They don't like guns and obviously do not like you right now.)")

        player = PlayerCharacter("You", 125, 30)
        battle_british_soldier(player)

        print("Well, guess I'm just a murderer now with some kind of berry monster helping me commit more crimes in various ages.");
        #time.sleep(3);
        print("(You begin to wander off attempting to hide somewhere not in the middle of the street. You find yourself wandering down an alley.)");
        #time.sleep(3);
        print("(At the end of the alley, a bright light suddenly bursts out of the wall. It resembles a portal that you would see in Star Trek or something else sci-fi.)");
        #time.sleep(3);
        print("Well guess I really don't have much to lose now.");
        #time.sleep(3);
        print("(You reload your rifle, take a look around and walk through the portal.)");

    def Travel_AlienWorld():
        print("(You step through the portal and find yourself on an alien planet)");
        #time.sleep(3);
        print("(The landscape is strange and unfamiliar)");
        #time.sleep(2);
        print("(You see an Alien approaching)");
        #time.sleep(2);

        player = PlayerCharacter("You", 130, 35)
        battle_alien(player)

        # ... (Ending sequence thats super cool with blood and victory)


    # Call the travel functions
    Travel_StoneAge()
    Travel_CastleCamelot()
    Travel_RedDistrict()
    Travel_Lexington()
    Travel_WW2()
    Travel_AlienWorld()

pygame.quit()

if __name__ == "__main__":
    start_game()
