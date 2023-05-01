import sys 
import time
import os
import random
#Information about "os": https://www.geeksforgeeks.org/os-module-python-examples/
#Information about "random": https://www.w3schools.com/python/module_random.asp

class MainCharacter():
    def __init__(self):
        self.name = None
        self.main_weapon = None
        self.alive = True
        self.health = None
        self.qi = None
        self.strength = None
        self.stealth = None
        self.dexterity = None
        self.endurance = None
        self.intelligence = None
        self.traits = []
        self.skills = []
        self.martial_arts = []
        self.breathing_arts = []
        self.body_tempering_arts = []
        self.manuals = []
        self.weapons = []

    def stats(self):
        print("Name: ",(Main.name))
        print("Health: ",(Main.health))
        print("Qi: ",(Main.qi))
        print("Strength:",(Main.strength))
        print("Stealth: ",(Main.stealth))
        print("Dexterity: ",(Main.dexterity))
        print("Endurance:",(Main.endurance))
        print("Intelligence: ",(Main.intelligence))
        print("Main Weapon: ",(Main.main_weapon))
        if Main.martial_arts != []:
            print("Martial Arts: ",(Main.martial_arts))
        if Main.breathing_arts != []:
            print("Breathing Arts: ",(Main.breathing_arts))
        if Main.body_tempering_arts != []:
            print("Body Tempering Arts: ",(Main.body_tempering_arts))
        if Main.manuals != []:
            print("Manuals: ",(Main.manuals))
    
    def stats_alt(self):
        print("Name: ",(Main.name))
        print("Health: ",(Main.health))
        print("Qi: ",(Main.qi))
        print("Strength:",(Main.strength))
        print("Stealth: ",(Main.stealth))
        print("Dexterity: ",(Main.dexterity))
        print("Endurance:",(Main.endurance))
        print("Intelligence: ",(Main.intelligence))
        if Main.martial_arts != []:
            print("Martial Arts: ",(Main.martial_arts))
        if Main.breathing_arts != []:
            print("Breathing Arts: ",(Main.breathing_arts))
        if Main.body_tempering_arts != []:
            print("Body Tempering Arts: ",(Main.body_tempering_arts))
        if Main.manuals != []:
            print("Manuals: ",(Main.manuals))

    def Death(self):
        print("You Died.")
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print("Loser")
        print("Lol")
        print("Get Gud")

class Enemy():
    def __init__(self):
        name_list = ["Fan Xiaobo","Zeng Liqiu","Qin Tung-Mei","He Liang","Chen Yanmei","Tian Nianzu","Dai Tao","Xu Meng","Liang Guoliang","Sun Zhilan","Ma Huifang","Zeng Chen","Zhu Meihui","Duan Yanmei","Gong Guangli","Luó Jiaying","Meng Xiaosheng","Zhong Qiuyue","Xiong Jia","Hao Xiuying"]
        weapons_list = ["standard practice sword","standard practice bow","standard practice axe","standard practice spear","standard practice gauntlets","standard practice staff"] 
        traits_list = ["Agile","Ambitious","Arrogant","Artful","Awful","Ascetic","Beautiful","Brave","Bright","Brilliant","Careless","Cautious","Charismatic","Charitable","Cheerful","Clever","Clumsy","Committed","Competitive","Composed","Concerned","Co-ordinated","Cordial","Cowardly","Creative","Cruel","Cunning","Deceitful","Defiant","Determined","Direct","Disciplinarian","Disloyal","Distinguished","Dutiful","Elusive","Energetic","Enigmatic","Feared","Fiery","Formidable","Fraternal","Friendly","Frivolous","Fulfilled","Graceful","Gracious","Greedy","Handsome","Healed","Healthy","Honest","Honourable","Humble","Impeccable","Incompetent","Indecisive","Intimidating","Intrepid","Kind","Kind-hearted","Lame","Loyal","Lumbering","Maimed","Modest","Obstinate","One-Eyed","Pacifist","Patient","Perceptive","Philanthropic","Populist","Quiet","Reckless","Relentless","Resourceful","Scarred","Scholary","Selfless","Sickly","Sincere","Solitary","Spiteful","Stalwart","Stern","Strong","Stubborn","Superstitious","Suspicious","Temperamental","Tolerant","Tough","Tranquil","Trusting","Trustworthy","Uncomplicated","Understanding","Unobservant","Vain","Vengeful","Vigilant","Weak"]
        body_tempering_arts_list = ["Diamond Body Technique","One Mind One Body Technique","5 Elements Perfection Body Technique","Supreme Domineering Body Technique","Undying Warrior Body Technique","Yoga Exercises for Eighty Year Olds to Strengthen Joints and Hip Mobility"]
        self.name = random.choice(name_list)
        self.main_weapon = random.choice(weapons_list)
        self.alive = True
        self.health = random.randint(100,500)
        self.qi = random.randint(0,600)
        self.strength = random.randint(1,20)
        self.stealth = random.randint(1,20)
        self.dexterity = random.randint(1,20)
        self.endurance = random.randint(1,20)
        self.intelligence = random.randint(1,20)
        self.traits = random.sample(traits_list,3)
        self.body_tempering_arts = random.choice(body_tempering_arts_list)
        if self.main_weapon == "standard practice sword":
            martial_arts_list = ["Death Touch Art","Slashing Sword Art","Universal Severance Technique"]
            breathing_arts_list = ["River of Swords Breathing Technique","10,000 Sword Breathing Technique","One Mind Sword Breathing Technique"]
            self.martial_arts = random.choice(martial_arts_list)
            self.breathing_arts = random.choice(breathing_arts_list)
        if self.main_weapon == "standard practice bow":
            martial_arts_list = ["Heavenly Target Technique","Wind Guidance Art","Piercing Arrow Art"]
            breathing_arts_list = ["Unending Arrow Breathing Technique","Immortal Hunters Breathing Technique","All Seeing Arrow Breathing Technique"]
            self.martial_arts = random.choice(martial_arts_list)
            self.breathing_arts = random.choice(breathing_arts_list)
        if self.main_weapon == "standard practice axe":
            martial_arts_list = ["World Splitting Axe Art","Cleaving Axe Art","Demonic Cleaving Axe Technique"]
            breathing_arts_list = ["Living Forests Breath Breathing Technique","Wooden Cycle Breathing Technique","Howls of the Dying World Breathing Technique"]
            self.martial_arts = random.choice(martial_arts_list)
            self.breathing_arts = random.choice(breathing_arts_list)
        if self.main_weapon == "standard practice spear":
            martial_arts_list = ["Stabbing Spear Art","Piercing Dragons Flow Art","Sky Penetrating Art"]
            breathing_arts_list = ["Undying Soldiers Breathing Technique",")Point of Origin Breathing Technique","Vital Rush Breathing Technique"]
            self.martial_arts = random.choice(martial_arts_list)
            self.breathing_arts = random.choice(breathing_arts_list)
        if self.main_weapon == "fist":
            martial_arts_list = ["Drunken Buddha's Fist Art","Asuras Bloody Claw Art","Punching Fist Art"]
            breathing_arts_list = ["Unmoving Reaction Breathing Technique","Untempted Soul Breathing Technique","Focused Mind Breathing Technique"]
            self.martial_arts = random.choice(martial_arts_list)
            self.breathing_arts = random.choice(breathing_arts_list)
        if self.main_weapon == "staff":
            martial_arts_list = ["Swinging Staff Art","Dharma Wheel Turning Staff Art","Monkey Gods Divine Staff Art"]
            breathing_arts_list = ["Natural Monkey's Breathing Technique","Influx Breathing Technique","Divine Cycle Breathing Technique"]
            self.martial_arts = random.choice(martial_arts_list)
            self.breathing_arts = random.choice(breathing_arts_list)

    def Enemy_stats():
        print("Name: ", (Enemies.name))
        print("Health: ", (Enemies.health))
        print("Qi: ", (Enemies.qi))
        print("Strength:", (Enemies.strength))
        print("Stealth: ", (Enemies.stealth))
        print("Dexterity: ", (Enemies.dexterity))
        print("Endurance: ", (Enemies.endurance))
        print("Intelligence: ", (Enemies.intelligence))
        print("Main Weapon: ", (Enemies.main_weapon))
        print("Martial Arts: ", (Enemies.martial_arts))
        print("Breathing Arts: ", (Enemies.breathing_arts))
        print("Body Tempering Arts: ", (Enemies.body_tempering_arts))

    def Enemy_defeat(self):
        print("You managed to kill your enemy and succeed in the test ensuring your survival.")
        time.sleep(4)
        print("As you return to the stands, proud about your victory, you sit down and fall asleep as you relax and are glad that you get to live another day.")
        time.sleep(10)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print(" ")
        time.sleep(1)
        print("Good Job, Game Done.")
        sys.exit()

def identification(identification_choices):
    if identification_choices in ["Wealth","wealth","富"]:
        print("You are Hàoyú Fu, heir to the Thousand Treasures Commerce House, the biggest trading company in the whole company. Ever since he was young, he's lived a life unlike any, surrounded by luxury with his every desire met at the ring of a bell but one day when he was walking out in town with his guards, some strange men attacked them. They killed his guards and grabbed him running away before reinforcements could arrive to save the young master.")
        #time.sleep(25)
        Main.name = "Hàoyú Fu"
        Main.health = 200
        Main.qi = 50
        Main.strength = 6
        Main.stealth = 1
        Main.dexterity = 8
        Main.endurance = 4
        Main.intelligence = 18
        Main.traits.extend(["Calculative","Greedy","Arrogant"])
        Main.skills.extend(["Negotiation 4/10","Trading 6/10"])
        print("Your stats are:")
        Main.stats_alt()
    if identification_choices in ["Rebirth","rebirth","重生"]:
        print("You are Chao Gang, a master martial artist who managed to become the first of the 'Ten Seats of Heaven' signifying thatyou managed to reach the top of the world. But you never were satisfied, you had plenty of regrets from your youth and even though you were on your death bed, you still felt like you weren't done, you still hadn't fully mastered your martial arts or became the strongest. What a sad ending.")
        #time.sleep(20)
        print("But as you close your eyes and take your final breath, you feel as if someone has grabbed your soul and removed it from your body. As you open your eyes you see your soul being dragged by a strange giant white hand but as you're flying with this hand, you suddenly pass out when it coems to a sudden halt.")
        #time.sleep(18)
        Main.name == "Chao Gang"
        Main.health = 100
        Main.qi = 0
        Main.strength = 2
        Main.stealth = 1
        Main.dexterity = 2
        Main.endurance = 2
        Main.intelligence = 50
        print("Your stats are:")
        Main.traits.extend(["Relaxed","Patient","Calculative","Predetermined","Ambitious"])
        Main.martial_arts.append("Realm Splitting Sword Art")
        Main.breathing_arts.append("Void Gods Presence Breathing Technique")
        Main.body_tempering_arts.append("Chaos Immortal Body Technique")
        Main.manuals.extend(["World Grasping Formation Manual","Alchemy God's Inheritence","Ethereal Step Technique"])
        Main.skills.extend(["Martial Arts Knowledge 10/10", "Alchemy Knowledge 7/10", "Formation Knowledge 8/10", "Forging Knowledge 8/10", "Weapon Knowledge 10/10"])
        Main.stats_alt()
    if identification_choices in ["Nobility","nobility","高貴"]:
        print("You are Xingyi Namgoong, the main heir to the noble Namgoong family, that stands a top of the 5 noble families of the central murim alliance. Since birth, you've been taught to be noble and elegant and to reflect the values of the Namgoong family, ones of strength and loyalty. You've been taught by some of the best teachers and have been trained in the Namgoong family's martial arts to allow you to become a worthy heir. But unfortunalty one day, the Namgoong family was attacked by invaders and in this midst of chaos, you were taken by the invaders as they retreated.")
        #time.sleep(30)
        Main.name = "Xingyi Namgoong"
        Main.health = 300
        Main.qi = 200
        Main.strength = 15
        Main.stealth = 5
        Main.dexterity = 13
        Main.endurance = 10
        Main.intelligence = 13
        Main.traits.extend(["Noble","Arrogant","Stubborn","Calculative","Manipulative"])
        Main.martial_arts.append("Everlasting Sword Art")
        Main.breathing_arts.append("Flow Breathing Technique")
        Main.skills.extend(["Sword skill 5/10"])
        print("Your stats are:")
        Main.stats_alt()
    if identification_choices in ["Alone","alone","孤"]:
        print("You are a transmigrator, one who doesn't belong to this world but was sent to it, but the question is, who are you?")
        transmigrator = input()
        if transmigrator.lower() == "han jue":
            print("You are Han Jue.")
            Main.name = "Han Jue"
            Main.health = 999999999999
            Main.qi = 999999999999
            Main.strength = 999999999999
            Main.stealth = 999999999999
            Main.dexterity = 999999999999
            Main.endurance = 999999999999
            Main.intelligence = 999999999999
            Main.traits.append("all")
            Main.martial_arts.extend(["Perfection Sword Art", "Perfection Bow Art", "Perfection Spear Art", "Perfection Axe Art", "Perfection Fist Art", "Perfection Fist Art", "Perfection Staff Art"])
            Main.breathing_arts.append("Primordial Origin Breath Breathing Technique")
            Main.body_tempering_arts.append("Primordial Origin Body Body Technique")
            Main.manuals.extend(["Origin Alchemy Technique", "Origin Formation Technique", "Origin Step Technique"])
            Main.skills.extend(["Weapon Knowledge 10/10", "Sword Skill 10/10", "Saber Skill 10/10", "Bow Skill 10/10", "Axe Skill 10/10", "Spear Skill 10/10","Fist Skill 10/10", "Staff Skill 10/10", "Alchemy Knowledge 10/10", "Formation Knowledge 10/10", "Forging Knowledge 10/10"])
            print("Your stats are:")
            Main.stats_alt()
        else:
            print("You are Generic Character 1")
            Main.name = "Generic Character 1 "
            Main.health = 1
            Main.qi = 1
            Main.strength = 1
            Main.stealth = 1
            Main.dexterity = 1
            Main.endurance = 1
            Main.intelligence = 1
            print("Your stats are:")
            Main.stats_alt()

def Battle():
    print("'Welcome all to your first test since arrival. Now that you've all had time to choose your martial arts and to get yourself acquinted with your room, it's time to anounce your first test'")
    #time.sleep(12)
    print("'Your first test shall be a dueling competition between you all as you may have noticed that there are stil too many of you guys. We don't need all of you guys, we only need the very best of you so to cut down your numbers in half, you all shall fight to the death with the winner being allowed to remain.'")
    #time.sleep(20)
    print("'The first two contestants are " +Main.name+ " and " +Enemies.name+ ", please come up to the stage'")
    #time.sleep(5)
    print("As you get to the stage, you see your opponent")
    os.system('clear')
    print("Your Stats:")
    Main.stats()
    print(" ")
    print(" ")
    print(" ")
    print("Enemy Stats:")
    Enemies.Enemy_stats()
    while Main.health != 0:
        print("What would you like to do?")
        action = input()
        if action.lower() == "attack":
            print("You dealt " +str(Main.strength)+ " damage to your enemy")
            Enemies.health = Enemies.health - Main.strength
            if Enemies.health <= 0:
                Enemies.Enemy_defeat()
        print("Now it's your opponents turn to attack.")
        print("Your opponent dealt " +str(Enemies.strength)+ " damage to you.")
        Main.health = Main.health - Enemies.strength
        if Main.health <= 0:
            Main.Death()
        
def Battle_Initiation():
    print("You went to the door and opened it and to your surprise, an instructor was there. He told you to follow him")
    #time.sleep(6)
    print("He led you through the whole facility to a giant arena where you see the facility leader standing on the stage")
    Battle()

def Action_Sleep():
    print("you decided to go to bed due to your exhaustion from the long day")
    #time.sleep(20)
    print("A knocking sound woke you up from your slumber.")
    #time.sleep(3)
    Battle_Initiation()

def Action_Relax():      
    print("You decided to relax and enjoy your time by dancing.")
    time.sleep(4)
    print("What dance do you want to do?")
    dance_choice = input()
    print("How many hours do you want to dance for?")
    dance_time = input()
    dance_time = int(dance_time)
    time.sleep(2)
    dance_counter = 1
    for dance_counter in range(dance_counter, dance_time + 1):
        dance_counter = str(dance_counter)
        print("You danced the " +dance_choice+ " for " +dance_counter+ " hour(s)")
        dance_counter = int(dance_counter)
        time.sleep(1)
    dance_time = str(dance_time)
    dance_counter = str(dance_counter)
    print("After you danced for " +dance_counter+ " hour(s) and relaxed, you hear a knock at your door.")
    Battle_Initiation()
    
def Training(training_action):
    if training_action in ["1","Train Martial Arts"]:
        print("Which martial arts would you like to pracitce?")
        print(Main.martial_arts)
        martial_training = input()
        #time.sleep(15)
        print("After training the " +martial_training+ ", you get a knock on your door.")
        Battle_Initiation()
    if training_action in ["2","Exercise"]:
        print("Which exercise would you like to do?")
        exercise = input()
        print("How many " +exercise+ " would you like to do")
        amount = input()
        amount = int(amount)
        #time.sleep(2)
        amount_time = 1
        for amount_time in range(amount_time, amount + 1):
            amount_time = str(amount_time)
            print("[You bit the key " +amount_time+ " times]")
            amount_time = int(amount_time)
            #time.sleep(1)
        amount = str(amount)
        print("After you did " +amount+ +exercise+ "s, you heard a knock at your door.")
        Battle_Initiation()

def Action_Train():
    print("You decided to train your martial arts and develop your skills further. What would you like to do?")
    print("1)Train Martial Arts")
    print("2)Exercise")
    training_action = input()
    Training(training_action)

def Action_1(action1):
    if action1.lower() == "sleep":
        Action_Sleep()
    if action1.lower() == "relax":
        Action_Relax()
    if action1.lower() == "train":
        Action_Train()

def Dorms():
    print("As you entered your room, you fell on the bed and relaxed as you heard other kids outside getting into their dorms.")
    os.system('clear')
    print("Stats:")
    Main.stats()
    print("You still have time till the day is left, what would you like to do?")
    print("(1/1 actions left)")
    print("Choices:")
    print("1)Sleep")
    print("2)Relax")
    print("3)Train Martial Arts")
    action1 = input()
    Action_1(action1)

def First_Weapon(weapon_path_selection):
    print("Once you've chosen all your martial arts, you went to the head instructor at the gates of the library and shown him what martial arts you've chosen")
    #time.sleep(8)
    print("'It seems that you've chosen to focus on " +weapon_path_selection+ "s as your main focus. Now you may leave the library. Down the hall, you should find an instructor who'll give you your " +weapon_path_selection+ ". Good luck young one and don't fail us.'")
    #time.sleep(16)
    print("As you walk down the long, empty hall, you finally see an instructor with a lot of weapons around him.")
    #time.sleep(6)
    print("'So what weapon do you need, trainee.'")
    #time.sleep(3)
    print(weapon_path_selection)
    #time.sleep(1)
    print("Here, one standard practice " +weapon_path_selection+ "for a trainee.")
    if weapon_path_selection.lower() == "sword":
        Main.weapons.append("standard practice sword")
        Main.main_weapon = "sword"
    if weapon_path_selection.lower() == "bow":
        Main.weapons.append("standard practice bow")
        Main.main_weapon = "bow"
    if weapon_path_selection.lower() == "axe":
        Main.weapons.append("standard practice axe")
        Main.main_weapon = "axe"
    if weapon_path_selection.lower() == "spear":
        Main.weapons.append("standard practice spear")
        Main.main_weapon = "spear"
    if weapon_path_selection.lower() == "fist":
        Main.weapons.append("standard practice gauntlets")
        Main.main_weapon = "gauntlets"
    if weapon_path_selection.lower() == "staff":
        Main.weapons.append("standard practice staff")
        Main.main_weapon = "staff"
    print("'Now that you got your weapon, continue down the hall and you should find the dorms for you trainees to stay at, just find the one with your name on it and head inside.'")
    #time.sleep(10)
    os.system('clear')
    print("As you reached the dorms you searched through them until you found the one with your name on it.")
    print("Number 31:")
    print(Main.name)
    Dorms()

def Body_Tempering_Arts(weapon_path_selection):
    print("Finally, you go to get your final technique, your body tempering technique which will allow you to physically cultivate your body to grow stronger. The instructor near the breathing techniques section tells you to go to the back of the library to find the body tempering techniques.")
    #time.sleep(18)
    print("From all the techniques, you've managed to narrow it down to a few choices:")
    print("1)Diamond Body Technique")
    print("2)One Mind One Body Technique")
    print("3)5 Elements Perfection Body Technique")
    print("4)Supreme Domineering Body Technique")
    print("5)Undying Warrior Body Technique")
    print("6)Other")
    body_tempering_art_choice = input()
    if body_tempering_art_choice in ["other","Other"]:
        #time.sleep(10)
        print("Really.")
        time.sleep(1)
        print("Why.")
        time.sleep(1)
        print("Are you really going to choose this technique? Like out of all of these techniques, are you going to choose this one?")
        body_confirmation = input()
        if body_confirmation[0] == "y":
            print("You've chosen: Yoga Exercises for Eighty Year Olds to Strengthen Joints and Hip Mobility")
            Main.body_tempering_arts.append("Yoga Exercises for Eighty Year Olds to Strengthen Joints and Hip Mobility")
            First_Weapon(weapon_path_selection)
        if body_confirmation[0] == "n":
            print("1)Diamond Body Technique")
            print("2)One Mind One Body Technique")
            print("3)5 Elements Perfection Body Technique")
            print("4)Supreme Domineering Body Technique")
            print("5)Undying Warrior Body Technique")
            body_tempering_art_choice = input()
            Main.body_tempering_arts.append(body_tempering_art_choice)
            First_Weapon(weapon_path_selection)
    else:
        Main.body_tempering_arts.append(body_tempering_art_choice)
        First_Weapon(weapon_path_selection)

def Breathing_Arts(weapon_path_selection):
    print("As you go up to the instructor near the martial arts section of the library, he tells you that you can now move on to the right section of the library where the interal breathing techniques are which will allow you to cultivate your body spiritually and further strenghten your techniques.")
    #time.sleep(18)
    if weapon_path_selection.lower() == "sword":
        print("He instructed you to go the sword section to find internal breathing arts related to swords to assist you in your cultivation")
        print("1)River of Swords Breathing Technique")
        print("2)10,000 Sword Breathing Technique")
        print("3)One Mind Sword Breathing Technique")
        breathing_technique_choice = input()
        Main.breathing_arts.append(breathing_technique_choice)
    if weapon_path_selection.lower() == "bow":
        print("He instructed you to go the bow section to find internal breathing arts related to bows to assist you in your cultivation")
        print("1)Unending Arrow Breathing Technique")
        print("2)Immortal Hunters Breathing Technique")
        print("3)All Seeing Arrow Breathing Technique")
        breathing_technique_choice = input()
        Main.breathing_arts.append(breathing_technique_choice)
    if weapon_path_selection.lower() == "axe":
        print("He instructed you to go the axe section to find internal breathing arts related to axes to assist you in your cultivation")
        print("1)Living Forests Breath Breathing Technique")
        print("2)Wooden Cycle Breathing Technique")
        print("3)Howls of the Dying World Breathing Technique")
        breathing_technique_choice = input()
        Main.breathing_arts.append(breathing_technique_choice)
    if weapon_path_selection.lower() == "spear":
        print("He instructed you to go the spear section to find internal breathing arts related to spears to assist you in your cultivation")
        print("1)Undying Soldiers Breathing Technique")
        print("2)Point of Origin Breathing Technique")
        print("3)Vital Rush Breathing Technique")
        breathing_technique_choice = input()
        Main.breathing_arts.append(breathing_technique_choice)
    if weapon_path_selection.lower() == "fist":
        print("He instructed you to go the fist section to find internal breathing arts related to fists to assist you in your cultivation")
        print("1)Unmoving Reaction Breathing Technique")
        print("2)Untempted Soul Breathing Technique")
        print("3)Focused Mind Breathing Technique")
        breathing_technique_choice = input()
        Main.breathing_arts.append(breathing_technique_choice)
    if weapon_path_selection.lower() == "staff":
        print("He instructed you to go the staff section to find internal breathing arts related to staffs to assist you in your cultivation")
        print("1)Natural Monkey's Breathing Technique")
        print("2)Influx Breathing Technique")
        print("3)Divine Cycle Breathing Technique")
        breathing_technique_choice = input()
        Main.breathing_arts.append(breathing_technique_choice)
    os.system('clear')
    Body_Tempering_Arts(weapon_path_selection)
    
def Martial_Art(weapon_path_selection):
    os.system('clear')
    print("Choose one of the following martial arts:")
    if weapon_path_selection.lower() == "sword":
        print("1)Death Touch Art")
        print("2)Slashing Sword Art")
        print("3)Universal Severance Technique")
        martial_arts_choice = input()
        Main.martial_arts.append(martial_arts_choice)
    if weapon_path_selection.lower() == "bow":
        print("1)Heavenly Target Technique")
        print("2)Wind Guidance Art")
        print("3)Piercing Arrow Art")
    if weapon_path_selection.lower() == "axe":
        print("1)World Splitting Axe Art")
        print("2)Cleaving Axe Art")
        print("3)Demonic Cleaving Axe Technique")
        martial_arts_choice = input()
        Main.martial_arts.append(martial_arts_choice)
    if weapon_path_selection.lower() == "spear":
        print("1)Stabbing Spear Art")
        print("2)Piercing Dragons Flow Art")
        print("3)Sky Penetrating Art")
        martial_arts_choice = input()
        Main.martial_arts.append(martial_arts_choice)
    if weapon_path_selection.lower() == "fist":
        print("1)Drunken Buddha's Fist Art")
        print("2)Asuras Bloody Claw Art")
        print("3)Punching Fist Art")
        martial_arts_choice = input()
        Main.martial_arts.append(martial_arts_choice)
    if weapon_path_selection.lower() == "staff":
        print("1)Swinging Staff Art")
        print("2)Dharma Wheel Turning Staff Art")
        print("3)Monkey Gods Divine Staff Art")
        martial_arts_choice = input()
        Main.martial_arts.append(martial_arts_choice)
    os.system('clear')
    Breathing_Arts(weapon_path_selection)

def Grand_Archive():
    print("The head instructor lead all of you throughout the facilities until you guys reached 2 giant doors with 2 guards. He gave them a signal and both guards proceeded to open both doors and what you could see when you went inside was a huge library filled with thousands if not hundreds of thousands of books.")
    #time.sleep(18)
    print("'This is the Grand Archives of the cult where we store all the martial arts and manuals of the cult. You all will be given 1 hour to choose a martial arts, breathing technique, and body tempering technqiue to practice. After that, you shall be given a training uniform of the cult and a suitable weapon for your martial arts.'")
    #time.sleep(20)
    print("'Now Go.")
    #time.sleep(1)
    print("As you go to search for your martial arts first, you realize you haven't thought of what weapon you want to use.")
    #time.sleep(8)
    print("Which weapon are you searching for?")
    print("1)Sword\n2)Bow\n3)Axe\n4)Spear\n5)Fist\n6)Staff")
    weapon_path_selection = input()
    Martial_Art(weapon_path_selection)

if __name__ == "__main__":
    while True:
        Main = MainCharacter()
        Enemies = Enemy()
        print("As you awake in a strange stone room, you stand up slowly as you try to think about where you are when you're hit with a strong headache as memories flood into your head.")
        #time.sleep(9)
        print("[Choose from the options below]")
        print("  富      重生      高貴      孤   ")
        print("Wealth  Rebirth  Nobility   Alone")
        identification_choices = input()
        identification(identification_choices)
        print("As you try to absorb your surroundings, you hear a loud sound as a wall infront of you opens up shining a bright light into your dark room.")
        #time.sleep(7)
        print("A man covering his face wtih a hood walks in and drags you by the hand out of the room.")
        #time.sleep(4)
        print("As you follow the man through the hallways, you question how big is this place but you guys soon arrive at a large room where you say many other children standing there.")
        #time.sleep(10)
        print("The man who was dragging you lets go and walks away and as you stand there, questioning what is going on, you suddenly hear a loud sound on the stage as you see the man who was dragging you and many other similar men standing on a stage as an old man with a scar on his left eye walks on infront of them.")
        #time.sleep(18)
        print("The man clears his through and suddenly yells out loud for the children to be quiet, the room filled with whispers and chatter quickly became silent.")
        #time.sleep(7)
        print("'Ahem. You all must be confused as to why you've been brought here. I am the head of this facility and known as the ghost demon, one of the twelve demon generals of the cult. The reason is that you've all been chosen to become the key forces of the cult and assist the cult as spies and assassins to further are goal.'")
        #time.sleep(20)
        print("'Even though there may be many of you, I'll tell you right now, most of you will die. Only those who evolve and become true apex predators among all of you, those who become the best of the best will survive. The rest shall just become a stepping stone for the others rise.'")
        #time.sleep(17)
        print("'But before your instructor comes up to talk to you all, I will ask only once, are there any among you who wish to leave before we start'")
        #time.sleep(7)
        print("As you questioned whether to raise your hand, you saw a hand raise up, and then another, and another, and soon, there where more than 50 hands raised among the sea of children there.")
        #time.sleep(13)
        print("[Do you raise your hand?]")
        hand_raising_choice = input()
        if hand_raising_choice[0] == "y":
            print("'Those who've raised their hands please stand in front of the stage.'") 
            #time.sleep(3)
            print("'Ok great.' The man said as he snapped his fingers")
            #time.sleep(2)
            print("Immediately the men behind him walked off the stage and towards all of us as they pulled their swords.")
            #time.sleep(6)
            print("One second you're looking straight and the next everything seems upside down as you realize you've been decapitated. All the children who raised their hands were killed.")
            #time.sleep(11)
            print("When the men finished cutting you all down, they placed their swords back in their scabbards and walked back onto the stage as men entered from the sides and started removing the corpses.")
            #time.sleep(13)
            print("'That's what happens to those who aren't dedicated to the cause, you trash.'")
            Main.Death()
        if hand_raising_choice[0] == "n":
            print("'Those who've raised their hands please stand in front of the stage.' All the children who raised their hands started walking from the crowd of children to the front of the stage") 
            #time.sleep(3)
            print("'Ok great.' The man said as he snapped his fingers")
            #time.sleep(2)
            print("Immediately the men behind him walked off the stage and towards the children who raised their hands as they pulled their swords and began mercillesly slaughtering the children.")
            #time.sleep(12)
            print("When the men finished cutting all of them down, they placed their swords back in their scabbards and walked back onto the stage as men entered from the sides and started removing the corpses.")
            #time.sleep(13)
            print("'Great, now that we've gotten rid of the waste, your head instructor shall give you a few words before dismissing you. But before I leave, remember, those who aren't dedicated to the cause aren't needed.'")
            #time.sleep(14)
            print("Now that we've gotten done with the entrance ceremony, you all shall be taken to the grand archive to pick out your martial arts that you shall train as long as you are here")
            os.system('clear')
            Grand_Archive()