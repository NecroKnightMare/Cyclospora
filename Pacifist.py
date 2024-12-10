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

def PacifistPath():

    def Travel_StoneAge():
        print("(You try to communicate with the Caveman)")
        #time.sleep(3)
        print("(The caveman seems confused)")

        time.sleep(2)
        print("(You see a fruit on the ground a few feet from you")
        time.sleep(3)

        #time.sleep(2)
        print("(The caveman notices and starts yelling profusely)")
        #time.sleep(3)

        print("{player_name}: 'What the....No, wait...'")
        time.sleep(2)
        print("(You start to backup and cower)")
        time.sleep(2)
        print("(He goes to grab the fruit)")
        time.sleep(3)
        print("(The caveman grabs the fruit and leaves you alone)")
        time.sleep(2)
        print("(Whats up with all this fruit and death being in the same topic?)")
        time.sleep(2)
        print("(You start feeling funny and notice a portal at your feet)")
        time.sleep(3)
        print("{player_name}: 'HOLY SHH...'(You have gone through the portal)")
        time.sleep(3)

        player = PlayerCharacter("You", 100, 10)
        Travel_CastleCamelot(player)

    time.sleep(3);


    def Travel_CastleCamelot2():
        # print("{player_name}: '....IIIIT!!'");
        # print("(the portal drops you on a cobblestone road)")
        # time.sleep(3)
        # print("{player_name}: 'OOOWW!!'")
        # print("(As you take a breathe in, you immediately start to feel sick)");
        # #time.sleep(3)
        # print("(You lean over to the side of a cobblestone ledge and vomit)")
        # time.sleep(5);
        # print("{player_name}: 'That taste just as bad as it did when I ate that pie'");
        # #time.sleep(2);
        # print("(Wiping off the sides of your mouth, clanging metal sounds come from the road south of your position)");
        # time.sleep(5);
        # print("Knight: 'HARK!! Who Goes There?!'")
        print("(You've decided to talk to the Knight)")
        time.sleep(3)
        print("{player_name}: 'I am not from here, I don't know why I'm here.'")
        print("(The knight looks at you while standing perfectly still)")
        print("(This isn't going well...)")
        time.sleep(3)
        print("Knight: 'Ho there, good fellow! You seem to have enjoyed too much of the inn's finest ale. Pray, steady yourself and take heed of your surroundings, lest you find yourself in further folly!'")
        time.sleep(3)
        print("({player_name}: 'Did he assume I'm drunk?!')")
        time.sleep(5);
        print("(The Knight turns and marches off)")
        time.sleep(3)
        print("(You sit and think {player_name}: 'Well at least he didn't kill me')")
        time.sleep(3)
        print("(You start feeling funny like you did after the caveman walked away)")
        time.sleep(3)
        print("{player_name}: 'Oh no.....'")
        print("(The ground starts to open and once again you fall through)")
        time.sleep(3)

        player = PlayerCharacter("You", 110, 15)
        #time.sleep(3);
        Travel_RedDistrict2(player)

    def Travel_RedDistrict2():
        # #time.sleep(2);
        # print("{player_name}: 'WHY IS THIS HAPPENING TO ME?!'");
        # #time.sleep(2);
        # print("(You start trembling with anger and feelings of helplessness...)");
        # #time.sleep(3);
        # print("{player_name}: 'Where am I now?!'");
        # #time.sleep(2);
        # print("(YOu hear a commotion to your left and see  Geisha in the midst of a crowd walking , almost like a parade)");
        # #time.sleep(3);
        # print("(The lights start turning on and the sun is setting, you realize it's getting dark out)");
        # #time.sleep(2);
        # print("{player_name}: 'Crap, gotta find somewhere to sleep'");
        # #time.sleep(2);
        # print("(You wonder the district and see food vendors and the area becoming livelier)");
        # time.sleep(4);
        # print("(You're stomach still hurts from that pie you ate. But you feel an insatuated hunger)");
        # time.sleep(5);
        # print("{player_name}: 'Can I get some food please?'(You ask a vendor, she clearly doesn't understand you)");
        # #time.sleep(3);
        # print("{player_name}: 'Well damn...'");
        # #time.sleep(2);
        # print("{player_name}: 'Well maybe if I...'(You start to rummage your pockets and pull out your wallet. The vendor starts to panic)");
        # time.sleep(6);
        # print("(You gaze to see what she's fretting about. As you try to see where your gaze ends, you realize it's the weapons you've collected along the way. )");
        # #time.sleep(3);
        # print("(You're shocked, and start explaining that you mean no harm, but fail)");
        # time.sleep(4);
        # print("(Some person you can only describe as a stereotypical ninja approaches you with sword drawn.)")
        print("(You've decided to talk to the Ninja)")
        time.sleep(3)
        print("{player_name}: 'Look, I didn't mean to scare her'")
        print("(The ninja slowly starts walking towards you)")
        print("({player_name}: 'Why is this happening to me, I just want this to be over...')")
        time.sleep(3)
        print("Ninja: 'あなたは誰ですか'")
        time.sleep(3)
        print("('{player_name}: Oh crap..This is worse than the Caveman...This guy is waaay smarter and will be more difficult to persuade.')")
        time.sleep(6)
        print("(You start pointing at your clothes)")
        time.sleep(3)
        print("(The ninja stops and seems to wait for you to finish whatever it is you think you're doing.)")
        time.sleep(3)
        print("(You point at your wrist and look at the ninja. He doesn't understand watches yet dummy.)")
        time.sleep(3)
        print("(You start feeling helplessness all over again. You slump over in defeat)")
        print("(The ninja hands you a stick)")
        time.sleep(4)
        print("{player_name}: 'What am I suppose to do with this?'")
        print("(The ninja waves his hand as if he's drawing something)")
        time.sleep(3)
        print("(You start drawing yourself and your house with a question mark to see if he gets that you are lost and need to go home)")
        time.sleep(5)
        print("Ninja: 'ああ、なるほど'")
        time.sleep(3)
        print("(He hands you a gourd, bows and leaves)")
        time.sleep(3)
        print("(You stand there in shock... 'What just happened?')")
        time.sleep(3)
        print("(You look at the gourd he left you and open it. Water sloshes inside)")
        time.sleep(3)
        print("{player_name}: 'Huh. That was thoughtful'")
        print("(You put the gourd to your lips and suddenly your stomach hurts. You drop the gourd to hold your stomach)")
        time.sleep(3)
        print("{player_name}: 'OH MY GOD!'")
        time.sleep(5)
        print("(You feel a tinge in your abdomen as if something were moving)")
        time.sleep(3)
        print("(You see the hole opening up beneath your feet. You're in too much pain to put another thought to it.)")
        print("(The lights vanish and you're pulled in once again)")
        time.sleep(3)
        player = PlayerCharacter("You", 115, 20)
        time.sleep(4);

        Travel_Lexington2(player)

    def Travel_Lexington2():
        # print("(You awake and look around, you notice plains of grass and tents vicarously placed on the end that you're in and the opposite end.)")
        # print("{player_name}: 'I must have passed out from the pain'")
        # #time.sleep(3);
        # print("Concord Militiaman: 'Halt! Who goes there? State your business on this land, or prepare to face the consequences!'")
        # #time.sleep(2);
        # print("(You stop and slowly turn around)")
        # #time.sleep(2);
        # print("(You are face to face with a Concord militiaman.)")
        # time.sleep(3)
        # print("{player_name}: '...guns...'")
        # print("(You need too tread carefully or there will be a bullet between your eyes.)")
        # time.sleep(3)
        player = PlayerCharacter("You", 120, 25)

        print("(You chose to speak with the soldier)")
        #time.sleep(2);
        print("{player_name}: 'Hey.'")
        #time.sleep(2);
        print("(The soldier looks at you questionably)")
        #time.sleep(3);
        print("(You start to feel light headed)")
        #time.sleep(2);
        print("{player_name}: 'I don't belong here'")
        #time.sleep(2);
        time.sleep(3)
        print("Concord Militiaman: 'HA! Bit of a wanka, innit ya?'")
        time.sleep(4)
        print("{player_name}: 'You do realize y'all are gonna lose right?'")
        time.sleep(3)
        print("(The concord soldier laughs)")
        time.sleep(3) 
        print("Concord Militiaman: 'By the heavens, man! Have you been at the ale?'")
        time.sleep(6)
        print("Concord Militiaman: 'Eyes on me, lad! Watch closely as I take aim and fire! This is how we defend our land!'")
        time.sleep(6)
        print("(You watch as you realize you are witnessing the shot heard round the world)")
        print("{player_name}: 'Ooops..'")
        time.sleep(3)
        print("(You also may have just messed up history)")
        time.sleep(4)
        print("(Without missing a beat, the portal opens at your feet again, you'll never know if you single-handedly rewrote history)")
        time.sleep(6)

        Travel_WWII2(player)

    def Travel_WWII2():
        # print("(You start to panic and ponder, if wherever you landed will be changed from the history you know or if it remains the same)")
        # #time.sleep(3);
        # print("(You look around and you notice a city-scape, bombed to a point it resembled rubble more than a city)")
        # #time.sleep(2);
        # print("{player_name: 'Where am I now?'")
        # #time.sleep(2);
        # print("(You see a soldier patrolling the area)")
        # #time.sleep(2);
        # print("Soldier: 'Hey! This is no place for you! Get to safety, now!'")
        # #time.sleep(3)
        # print("(You realize you are in another battlezone and start to panic.)")
        # time.sleep(3)
        # print("{player_name}: 'Wooah...I just need some help...'")
        # time.sleep(3)
        # print("(The soldier you believe is American due to the uniform they have on.)")
        # time.sleep(3)
        # print("Soldier 'Identify yourself! What are you doing here? You better have a good reason, or you'll be answering to the higher-ups.'")
        # time.sleep("({player_name}: 'Okay what do I say now?')")
        print("(You've decided to speak to the Soldier)")
        time.sleep(3)
        print("({player_name}: 'Maybe if I tell him the truth')")
        time.sleep(3)
        print("{player_name}: 'I'm American, but I'm not from here....or Wait! What war am I standing in?!'")
        time.sleep(4)
        print("(The soldier seems skeptical but doesn't lower his weapon.)")
        time.sleep(3)
        print("Soldier: 'We're fighting the Germans...'")
        time.sleep(3)
        print("{player_name}: 'Oh thank god!!!!'")
        print("(You didn't rewrite history, You were just Lucky to keep it as nothing happened, guess Concord did shoot first, mystery solved)")
        time.sleep(6)
        print("(The soldier starts to get anxious)")
        time.sleep(3)
        print("{player_name}: 'I am not from this timeline....I don't know how it works. But I ate some parasite I think, the news was saying something about it.'")
        time.sleep(5)
        print("(The soldier's eyes widen in shock, but he maintains his composure.)")
        time.sleep(4)
        print("{player_name}: 'It happens after I interact with people in that timeline. And I just need to get home'")
        time.sleep(5)
        print("Soldier: 'From the future? This isn't a time for tall tales, but... if what you say is true, we need to figure this out quickly. Follow me, and we'll find someone who can help.'")
        time.sleep(8)
        print("({player_name}: 'He believes me?!')")
        print("(You follow him and suddenly Pain starts to surge from your abdomen, it's worse than before. You feel big movement in your abdomen)")
        time.sleep(6)
        print("{player_name}: 'WHAT THE ####!!!!'")
        time.sleep(4)
        print("(The soldier turns around and starts to rush over to you as you kneel over in pain. You see the hole opening beneath you. You look at the soldier with pain and desperation.)")
        time.sleep(8)
        print("(The soldier is saying something but you can't hear anything. You focus on his face that shared the same fear you feel.)")
        time.sleep(6)
        print("(You blackout from the shock)")
        time.sleep

        player = PlayerCharacter("You", 125, 30)

    Travel_AlienWorld2(player)

    def Travel_AlienWorld2():
        # print("(As you wake up, you feel cold metal on the backside of your entire body)")
        # time.sleep(3)
        # print("(Your gaze is met with what you believe to be an Alien)")
        # #time.sleep(3);
        # print("Alien: 'Awaken, human. You are now part of the great harvest. Your existence will contribute to the advancement of our species. Resistance is futile. Accept your fate.'")
        # print("(You scramble to your feet)")
        # #time.sleep(10);
        # print("{player_name}: 'What is going on?!'")
        # time.sleep(3)
        # print("Alien: 'Do not attempt to resist. Your kind has brought this upon yourselves. In the future, humans initiated a genocide against my people. I lost my arms in that war. Now, you will pay for your crimes.'")
        # time.sleep(3)
        # print("(You feel a surge of panic but try to think of a way out.)")
        # time.sleep(3)
        # print("{player_name}: 'Genocide? I... I had no idea. There must be another way. I can help you without... without this.'")
        # time.sleep(3)
        # print("(The Alien's eyes narrow, filled with anger and pain.)")
        # time.sleep(3)
        # print("Alien: 'Help?! You are the one that needs help! Aren't You wondering about the pain and circumstances that you are experiencing?'")
        # time.sleep(3)
        # print("(The alien laughs)")
        # time.sleep(2)
        # print("{player_name}: 'Well why am I here then?'")
        # print("Alien: 'We are harvesting your kind to help restore ours. The parasites that were on the berries, have the ability to travel through time, hence you being here.'")
        # time.sleep(10)
        # print("{player_name}: 'What? then how did the parasites get there if what we did was in the future and I'm in the past?'")
        # time.sleep(8)
        # print("Alien: 'As we foraged the planet for resources this parasite was of your planet once, but it had arrived on a meteor. It had evolved to survive the travel in space'")
        # print("Alien: 'We took it as an opportunity to go back in time after ingesting it. We failed many times'")
        # time.sleep(10)
        # print("Alien: 'But grew closer and closer to success. The spread of the coronavirus wasn't as successful as we'd hoped. We had scraped virus outbreaks from the plan.'")
        # time.sleep(10)
        # print("Alien: 'So why not use the parasite as we have been, to get revenge, to be the catalyst of our plight? Evidently ingesting this parasite for you humans has volatile symptoms.'")
        # time.sleep(8)
        # print("{player_name}: 'What do you mean?'")
        # time.sleep(4)
        # print("Alien: 'Well the time travel being one of them, although it doesn't really matter how or if you humans got to us or died beforehand. The less of you vermin, the better'")
        # time.sleep(10)
        # print("(You crouch once more, the pain is getting worse by the minute)")
        # time.sleep(5)
        # print("Alien: 'Well, I better harvest you whilst I can, The parasites love human flesh and the only way to kill it is by drinking our blood and even though it would give me time to harvest you, I'd rather you be in as much pain as possible'")
        # #time.sleep(12);
        # print("(The alien is getting ready to probe you, what shall you do?)")

        player = PlayerCharacter("You", 130, 35)

        print("(You chose to speak with the Alien...Good Luck)")
        print("Alien: 'Didn't you hear what I said?! The prompt you just read said 'Good Luck' and you didn't think you may have made a mistake?'")
        time.sleep(8)
        print("({player_name}: 'Prompt? what is he talking about?')")
        print("(.....)")
        print("Alien: 'Make it quick as you won't be able to speak in the next five minutes.'")
        time.sleep(8)
        print("{player_name}: 'On my way here, I didn't kill anyone.'")
        time.sleep(6)
        print("Alien: 'Is that so?'")
        time.sleep(4)
        print("(The alien makes it's way toward you and examines you're abdomen)")
        time.sleep(6)
        print("Alien: 'It's not as engorged as the other specimens...perhaps. But if any case why would I let you go? To come back and have genocide happen? No.'")
        time.sleep(8)
        print("{player_name}: 'I was able to convince everyone to not fight me. That has to count for something! I can do the same for my people so we don't commit genocide on your kind'")
        time.sleep(8)
        print("(The Alien is certain you'd commit genocide but, .....)")
        time.sleep(8)
        print("(The alien's eyes narrow, and it emits a low, guttural growl, followed by a series of sharp clicks and hisses. Its body shudders, and a faint, acrid smell fills the air, signaling its intense displeasure.)")
        time.sleep(15)
        print("Alien: 'If what you promise is true, there shall be a moment that happens in five years in your time that starts the genocide. Change that moment and we'll leave your kind be with a close watch.'")
        time.sleep(12)
        print("Alien: 'Otherwise we proceed as planned.'")
        time.sleep(6)
        print("(You stand there shocked in disbelief, did you dream it?)")
        time.sleep(6)
        print("Alien: 'It will be a dream if you proceed to speak'")
        time.sleep(6)
        print("({player_name}: 'Seriously who is it talking to?')")
        time.sleep(4)
        print("(....)")
        time.sleep(6)
        print("Alien: 'I know I said blood was the only cure but we also created this to eradicate the parasite if we needed to harvest a human that was too far gone.'")
        time.sleep(8)
        print("(The Alien looks at a vial with red liquid)")
        time.sleep(6)
        print("(You walk toward the vial)")
        time.sleep(6)
        print("Alien: 'Drink it and you'll awaken in your home as if the outbreak never happened. But your memories will stay. Just yours.'")
        time.sleep(8)
        print("(You hesitate. And without another thought you down the contents of the vial)")
        time.sleep(6)
        print("(You faint)")
        # ... (Ending sequence thats super cool with blood and victory)
        Travel_Home2(player)

    def Travel_Home2():
        # time.sleep(3)
        # print("(No longer do you feel cold metal but soft sheets and cushions, You jolt up)")
        # time.sleep(6)
        # print("{player_name}: 'Oh my god....I'm back home'")
        # time.sleep(6)
        # print("(You start getting up, relieved. As you make your way to the bedroom door and into the hallway.)")
        # time.sleep(8)
        # print("(CRASH!!......SCREACH!!)")
        # time.sleep(8)
        # print("(CYCLOSPORA)")

        time.sleep(3)
        print("(No longer do you feel cold metal but soft sheets and cushions, You jolt up)")
        time.sleep(6)
        print("{player_name}: 'Oh my god....I'm back home'")
        time.sleep(6)
        print("(You start getting up, relieved. As you make your way to the bedroom door and into the hallway.)")
        time.slep(8)
        print("TV: 'In Other News, berries are the best balance to add to your diet....'")
        time.sleep(8)
        print("{player_name}: 'No thank you! No more berries for me!'")
        time.sleep(6)
        print("{player_name}: 'I hope I can do as I promised...'")
        time.sleep(8)
        print("(I hope you can too...)")
        time.sleep(6)
        print("CYCLOSPORA")
        time.sleep(4)

    # Call the travel functions
    Travel_StoneAge()
    Travel_CastleCamelot2()
    Travel_RedDistrict2()
    Travel_Lexington2()
    Travel_WWII2()
    Travel_AlienWorld2()
    Travel_Home2()

if __name__ == "__main__":()
    start_game()
