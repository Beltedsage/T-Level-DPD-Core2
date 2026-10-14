import time
import random

# Quick time sleep function
def ts(t):
    time.sleep(t)

# Chippy quest baloney
chippy_count = 0 # How many times the chippy has been visited (used for Chippy lady dialogues)
cq = 0 # Might be when the quest if completed
lookedforpotatoes = 0 # Dont know if this works
cqc2 = 0 # Has the Co-op been visited after going into the warehouse
chippy_quest_chippy_1 = 0 # Has the chippy quest begun

# dictionaries
locations = {}
inventory = []
health = 100
coophealth = 100

player = {
    "location": 0
}

# Village
locations[0] = {
  "title": "- The Village",
  "desc": "You enter the main village.",
  "exits": {
    "Chippy": 1,
    "The Highway": 2,
    "Co-op": 3,
    "Home" : 4,
  }
}

# Chippy
locations[1] = {
    "title": "- The Codfather",
    "desc": "Best chippy around",
    "exits": {
        "Village": 0,
        "Basement": 5
    },
    "chats": {
        "Chippy lady": 0
    }
}

# The Co-op
locations[2] = {
    "title": "- The Co-op",
    "desc": "£1 for a card, proper deal",
    "exits": {
        "Village": 0,
    },
    "chats": {
        "Co-op bloke": 0
    }
}

locations[3] = {
  "title": "- The Highway",
  "desc": "Haven't done this yet",
  "exits": {
    "Village": 0,
  }
}

# Home
locations[4] = {
    "title": "- Home",
    "desc": "Home is where the heart is \nNothing here yet, future quest",
    "exits": {
        "Village": 0
    }
}

# Chippy basement, nothing here yet
locations[5] = {
    "title": "- The Codfather basement",
    "desc": "Bit spooky in here",
    "exits": {
        "Chippy": 1
    }
}

# Co-op warehouse
locations[6] = {
    "title": "- The Warehouse",
    "desc": "Probably shouldn't be here",
    "exits": {
        "Backdoor": 0
    },
    "items": {
        "Warehouse key": 0
    }
}

# Co-op super secret basement
locations[7] = {
    "title": "- The Super secret basement",
    "desc": "Could be where the spuds are",
    "exits": {
        "Sewers (ends up in the village)": 0
    },
    "items": {
        "The bag of spuds": 0
    }
}

#Quests

# Starting the chippy quest
def chippy_quest():
    ts(0.5), print("-The Chippy Quest-")
    ts(0.5), print("I lost my last sack of potatoes for the chippies. Can you get on it please? Cheers pard.")
    ts(2), print("They never got here, if you go ask at the shop they might know about it.")
    ts(1.5)

# Visiting the co-op for the first time
def chippy_quest_coop_1():
    while True:
        ts(0.5), print("\n\nWelcome to Co-op, do you want to buy something?")
        ts(1), print("1. Yes please, can I have a meal deal.")
        ts(0.5), print("2. Have you seen a sack of potatos anywhere?")
        ts(0.5)
        choice = input("> ")
        if choice == "1":
            ts(0.5), print("\nOf course, £4.10 please")
            ts(1), print("1. (Scan card)")
            ts(0.5), print("2. £4.10? Are you silly pard?")
            ts(0.5), print("3. Have you seen a sack of potatos anywhere?")
            ts(0.5)
            choice = input("> ")
            if choice == "1":
                player["location"] = 0
                ts(1), print("\nLoading... Maybe you shouldn't get distracted?\n"), ts(2)
            elif choice == "2":
                ts(2), print("\nZip it twerp")
                player["location"] = 6
                ts(1), print("\nLoading..."), ts(2)
                break
            elif choice == "3":
                ts(2), print("\nZip it twerp")
                player["location"] = 6
                ts(1), print("\nLoading..."), ts(2)
                break
        elif choice == "2":
            ts(2), print("\nZip it twerp")
            player["location"] = 6
            ts(1), print("\nLoading..."), ts(2)
            break
        else:
            ts(0.5), print("- I think you made a mistake.")

# Revisiting the co-op after going to the basement
def chippy_quest_coop_2():
    coop2 = True
    while coop2 == True:
        ts(0.5), print("\n\nWhat are you doing you silly boy")
        ts(1), print("1. Where are the potatoes pard (the pacifist route)")
        ts(0.5), print("2. Flip you (start a fight)")
        ts(1)
        choice = input("> ")
        if choice == "1":
            ts(0.5), print("\nThey aren't here. Have some")
            ts(0.5), print("(You get decked and are never seen again)")
        elif choice == "2":
            ts(0.5), print("\nYou're bleddy asking for it now pard")
            coop_boss_fight()
            player["location"] = 6
            ts(1), print("\nLoading..."), ts(2)
            coop2 = False
        else:
            ts(0.5), print("You walk away, taking the pacifist route. Try again")

# Fighting the Co-op bloke
def coop_boss_fight():
    coophealth = 100
    health = 100
    ts(0.5), print("\nLoading...")
    ts(1)
    fightactive = True
    while fightactive ==  True:
        if coophealth <= 0:
            ts(1), print("\nYou have beaten the Co-op man")
            ts(0.5), print("You may now go to the warehouse to investigate the spud incident")
            fightactive = False
            break
        elif health <= 0:
            ts(1), print("\nYou have died. Try again")
            ts(1), print("\nLoading...")
            health = 100
            coophealth = 100
        ts(1), print("\n\nYour health -", health)
        ts(0.5), print("Co-op man health -", coophealth)
        ts(0.5), print("\nWhat do you do")
        ts(1), print("1. Swing a haymaker")
        ts(0.5), print("2. Spinning backheel")
        ts(0.5), print("3. Surrender")
        ts(1)
        choice = input("> ")
        print()
        if choice == "1":
            dmg = random.randint(1, 50)
            ts(0.5), print("You swing one at him for", dmg, "damage.")
            coophealth -= dmg
        elif choice == "2":
            spinner = random.randint(1, 2)
            if spinner == 1:
                dmg = random.randint(50, 75)
                ts(0.5), print("You hit a crazy shot and deal", dmg, "damage")
                coophealth -= dmg
            else:
                ts(0.5), print("You missed and did no damage")
        elif choice == "3":
            ts(0.5), print("You surrender. Pretty stupid idea, try again")
            ts(1), print("\nLoading...")
            ts(1)
        else:
            ts(0.5), print("You missed and did no damage")
        if choice == "3":
            continue
        else:
            coopdmg = random.randint(1, 25)
            ts(0.5), print("Co-op bloke hits you for", coopdmg, "damage")
            health -= coopdmg


# The quest ending
def cq_complete():
    ts(2), print("\n\nCheers pard. You have saved the day")
    ts(2), print("As a token of my thanks, you can have a free bag of chips")
    ts(2), print("£2.50 please")
    ts(1), print("---")
    ts(1), print("And they all lived happily ever after")
    ts(2), print("Chippy quest completed")
    player["location"] = 0
    ts(1), print("\nLoading...")

#---------------------------------------------------------------

#Introduction to area & exits
ts(0.5), print("= Chippy Quest 1 =")
ts(0.5), print("Controls are go, talk, take - such as 'go Village', 'talk Chippy lady'")
ts(0.5), print("By the way, you're in the mood for some chips")

# Main game itself
keeprunning = True
while keeprunning == True:
    print("\n\n")
    current_location = player["location"]
    ts(2), print(locations[current_location]["title"])
    ts(0.5), print(locations[current_location]["desc"]) 

    # Prints locations
    ts(0.5), print("\nYou can go to:")
    ts(0.5)
    for r in locations[current_location]["exits"]:
        ts(0.25), print(r)
        if player["location"] == 6 and cqc2 == 1:
            ts(0.25), [print("Super secret basement")]

    # Prints talkable people
    if "chats" in locations[current_location]:
        ts(0.5), print("\nYou can talk to:")
        for r in locations[current_location]["chats"]:
            ts(0.5), print(r)
            
    # Prints items
    if "items" in locations[current_location]:
        ts(0.5), print("\nYou can take:")
        for r in locations[current_location]["items"]:
            ts(0.5), print(r)
    ts(0.5)

    action = input("\nWhat do you want to do: ")

# Talk
    # Chippy lady
    if action == "talk Chippy lady" and player["location"] == 1:
        ts(0.5), print("\n\nHello")
        if chippy_count > 1:
            # Has the chippy quest been completed
            ts(1)
            if cq == 1:
                ts(0.5), print("Thanks for finding my taters pard")
            else:
                done_cq = input("Have you done my chippy quest yet? ").lower()
                if done_cq == "yes" and "The bag of spuds" in inventory:
                    cq = 1
                    ts(0.5), cq_complete()
                elif done_cq == "yes" and not "The bag of spuds" in inventory:
                    ts(0.5), print("You bleddy liar. Bugger off and get cracking")
                else:
                    ts(0.5), print("Get back to it then pard")
            player["location"] = 1

    # Co-op bloke
    elif action == "talk Co-op bloke" and "Warehouse key" in inventory:
        chippy_quest_coop_2()

        cqc2 = 1
    elif action == "talk Co-op bloke" and chippy_quest_chippy_1 == 1 and not "Warehouse key" in inventory:
        chippy_quest_coop_1()
    elif action == "talk Co-op bloke":
        print(chippy_quest_chippy_1)
        print("Go away m8")

# Take
    elif action == "take Warehouse key":
        ts(0.5), inventory.append("Warehouse key")
        print("You took the Warehouse key")

    elif action == "take The bag of spuds":
        ts(0.5), print("\nYou have found the bag of spuds")
        ts(0.5), print("Please return the the Chippy lady")
        inventory.append("The bag of spuds")

# Go
    elif action == "go Village":
        player["location"] = 0
        ts(0.5), print("\nLoading...")

    elif action == "go Chippy" and player["location"] == 0:
        # Keeps track of how many times chippy has been visited / the chippy quest
        chippy_count += 1
        if cq == 1:
            ts(1)
            print()
        elif chippy_count == 1:
            # Begins the Chippy Quest
            ts(1)
            print()
            chippy_quest()
            chippy_quest_chippy_1 = 1    
        player["location"] = 1
        ts(0.5), print("\nLoading...")
    
    elif action == "go Co-op" and player["location"] == 0:
        player["location"] = 2
        ts(0.5), print("Loading...")

    elif action == "go Home" and player["location"] == 0:
        player["location"] = 4
        ts(0.5), print("\nLoading...")

    elif action == "go Basement" and player["location"] == 1:
        player["location"] = 5
        ts(0.5), print("\nLoading...")

    elif action == "go Highway" and player["location"] == 0:
        player["location"] = 3
        ts(0.5), print("\nLoading...")

    elif action == "go Backdoor" and "Warehouse key" in inventory:
        player["location"] = 0
        ts(0.5), print("\nLoading... Probably try go back and reason with Mr Co-op guy")
    
    elif action == "go Backdoor" and not "Warehouse key" in inventory:
        ts(0.5), print("Haven't got a key pard")
    
    elif action == "go Super secret basement" and cqc2 == 1:
        player["location"] = 7
        ts(0.5), print("\nLoading...")

    elif action == "go Sewers"  and player["location"] == 7:
        player["location"] = 0
        ts(0.5), print("\nLoading...")
    
    else:
        ts(0.5), print("\nEither you need to go somewhere else first or you misinputted")
        ts(1.5), print("Example - 'go Village'")
        ts(1)