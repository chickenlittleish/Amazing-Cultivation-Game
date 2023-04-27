import sys 
import time
import os

class MainCharacter():
    def __init__(self):
        self.name = None
        self.main_weapon = None
        self.secondary_weapon = None
        self.hidden_weapon = None
        self.alive = True
        self.health = None
        self.qi = None
        self.strength = None
        self.stealth = None
        self.dexterity = None
        self.endurance = None
        self.intelligence = None
        self.victories = None
        self.loses = None
        self.fame = None
        self.traits = []
        self.skills = []
        self.martial_arts = []
        self.weapons = []
        self.tools = []
        self.titles = []
    def stats(self):
        print("Name: " + MC.name)
        print("Health: " + MC.health)
        print("Qi: " + MC.qi)
        print("Strength:" + MC.strength)
        print("Stealth: " + MC.stealth)
        print("Dexterity: " + MC.dexterity)
        print("Endurance:" + MC.endurance)
        print("Intelligence: " + MC.intelligence)
if __name__ == "__main__":
    while True:
        MC = MainCharacter()
        print("As you awake in a strange stone room, you stand up slowly as you try to think about where you are when you're hit with a strong headache as memories flood into your head.")
        time.sleep(9)
        print("[Choose from the options below]")
        print("  富      重生      高貴      孤      悔")
        print("Wealth  Rebirth  Nobility   Alone   Regret")
        identification = input()
        if identification in ["Wealth","wealth","富"]:
            print("You are Hàoyú Fu, heir to the Thousand Treasures Commerce House, the biggest trading company in the whole company. Ever since he was young, he's lived a life unlike any, surrounded by luxury with his every desire met at the ring of a bell but one day when he was walking out in town with his guards, some strange men attacked them. They killed his guards and grabbed him running away before reinforcements could arrive to save the young master.")
            time.sleep(25)
            MC.name = "Hàoyú Fu"
            MC.health = 100
            MC.qi = 50
            MC.strength = 6
            MC.stealth = 1
            MC.dexterity = 8
            MC.endurance = 4
            MC.intelligence = 18
            print("Your stats are:")
            MC.stats()
        if identification in ["Rebirth","rebirth","重生"]:
            print("You are Master Oogway, a master martial artist who managed to become one of the 'Ten Seats of Heaven' signifying thatyou managed to reach the top of the world. But you never were satisfied, you had plenty of regrets from your youth and even though you were on your death bed, you still felt like you weren't done, you still hadn't fully mastered your martial arts or became the strongest. What a sad ending.")
            time.sleep(20)
            print("But as you close your eyes and take your final breath, you feel as if someone has grabbed your soul and removed it from your body. As you open your eyes you see your soul being dragged by a strange giant white hand but as you're flying with this hand, you suddenly pass out when it coems to a sudden halt.")
            time.sleep(18)
            MC.name == "Chao Gang"
        if identification in ["Nobility","nobility","高貴"]:
            print("")
        if identification in ["Alone","alone","孤"]:
            print("EPI")
        if identification in ["Regret","regret","悔"]:
            print("c")
        else:
            print("please choose one of the choices above")
            identification = input()
        print("As you try to absorb your surroundings, you hear a loud sound as a wall infront of you opens up shining a bright light into your dark room.")
        time.sleep(7)
        print("A man covering his face wtih a hood walks in and drags you by the hand out of the room.")
        time.sleep(4)
        print("As you follow the man through the hallways, you question how big is this place but you guys soon arrive at a large room where you say many other children standing there.")
        time.sleep(10)
        print("The man who was dragging you lets go and walks away and as you stand there, questioning what is going on, you suddenly hear a loud sound on the stage as you see the man who was dragging you and many other similar men standing on a stage as an old man with a scar on his left eye walks on infront of them.")
        time.sleep(18)
        print("The man clears his through and suddenly yells out loud for the children to be quiet, the room filled with whispers and chatter quickly became silent.")
        time.sleep(7)
        print("'Ahem. You all must be confused as to why you've been brought here. The reason is that you've all been chosen to become the key forces of the cult and assist the cult as spies and assassins to further are goal.'")
        time.sleep(15)
        print("'Even though there may be many of you, I'll tell you right now, most of you will die. Only those who evolve and become true apex predators among all of you, those who become the best of the best will survive. The rest shall just become a stepping stone for the others rise.'")
        time.sleep(17)
        print("'But before your instructor comes up to talk to you all, I will ask only once, are there any among you who wish to leave before we start'")
        time.sleep(7)
        print("As you questioned whether to raise your hand, you saw a hand raise up, and then another, and another, and soon, there where more than 50 hands raised among the sea of children there.")
        time.sleep(13)
        print("[Do you raise your hand?]")
        hand_raising_choice = input()
        if hand_raising_choice[0] == "y":
            print("'Those who've raised their hands please stand in front of the stage.'") 
            time.sleep(3)
            print("'Ok great.' The man said as he snapped his fingers")
            time.sleep(2)
            print("Immediately the men behind him walked off the stage and towards all of us as they pulled their swords.")
            time.sleep(6)
            print("One second you're looking straight and the next everything seems upside down as you realize you've been decapitated. All the children who raised their hands were killed.")
            time.sleep(11)
            print("When the men finished cutting you all down, they placed their swords back in their scabbards and walked back onto the stage as men entered from the sides and started removing the corpses.")
            time.sleep(13)
            print("'That's what happens to those who aren't dedicated to the cause, you trash.'")
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("Dead.")
        if hand_raising_choice[0] == "n":
            print("'Those who've raised their hands please stand in front of the stage.'") 
            time.sleep(3)
            print("'Ok great.' The man said as he snapped his fingers")
            time.sleep(2)
            print("Immediately the men behind him walked off the stage and towards the children who raised their hands as they pulled their swords and began mercillesly slaughtering the children.")
            time.sleep(12)
            print("When the men finished cutting all of them down, they placed their swords back in their scabbards and walked back onto the stage as men entered from the sides and started removing the corpses.")
            time.sleep(13)
            print("'Great, now that we've gotten rid of the waste, your instructor shall give you a few words before dismissing you. But before I leave, remember, those who aren't dedicated to the cause aren't needed.'")
            time.sleep(14)
            print("Now that we've gotten done with the entrance ceremony, you all shall be taken to the grand archive to pick out your martial arts that you shall train as long as you are here")




#os.system('clear')


#ADD CHOICE TO RAISE HAND
#ASK HIM IF OKAY TO USE THE TRAITS FROM THREE KINGDOMS WEBSITE YES
#https://totalwar.fandom.com/wiki/Traits_(Total_War:_Three_Kingdoms)
#you can use it