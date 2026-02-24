# os gives us access to the command line, time is used as a delay
import os, time

# this function prints text delayed like older video games
def slowText(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  

# introduces the player, sets the playerName variable
def start():
    global playerName   # establishes playerName as a global variable
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("Welcome to the game! Please enter your name: ")
    playerName = input()
    slowText("Hello, {}! You find yourself in the living room of a mysterious house.".format(playerName))
    slowText("From here, you can go to the kitchen, the bedroom, or the garden.")
    # Further game logic would go here
    time.sleep(1)
    livingRoom()

# continuation of the start, allows for the player to go to the living room
def livingRoom():
    global backpack
    os.system('cls' if os.name == 'nt' else 'clear')
    print("backpack: {}".format(backpack))
    slowText("You are in the living room. There are doors to the kitchen, bedroom, and garden. You can also look for items.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "kitchen":
        kitchen()
    elif choice == "bedroom":
        bedroom()
    elif choice == "garden":
        garden()
    elif choice == "look for items":
        if searchBackpack(backpack, "oreos"):
            slowText("You decided to scan the room. You find nothing.")
        else:
            slowText("You decided to scan the room. You find a half-eaten pack of oreos. Do you want to pick them up?")
            choice = input().strip().lower()
            if choice == "yes":
                backpack.append("oreos")
        time.sleep(2)
        livingRoom()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(3)
        livingRoom()

def kitchen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("backpack: {}".format(backpack))
    slowText("You are in the kitchen. There is a door to the living room and a window outside, which you can try to escape through. You can also look for items.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "living room":
        livingRoom()
    elif choice == "open window":
        openWindow()
    elif choice == "look for items":
        if searchBackpack(backpack, "paper clip"):
            slowText("You decided to scan the room. You find nothing.")
            time.sleep(2)
            kitchen()
        else:
            slowText("You decided to scan the room. You open up a junk drawer and find a paperclip. Do you want to pick it up?")
            choice = input().strip().lower()
            if choice == "yes":
                backpack.append("paper clip")
        time.sleep(2)
        kitchen()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(3)
        kitchen()

def garden():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("backpack: {}".format(backpack))
    slowText("You are in the garden. There is a door to the living room. You can also look for items.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "living room":
        livingRoom()
    elif choice == "look for items":
        if searchBackpack(backpack, "shovel"):
            slowText("You decided to scan the room. You find nothing.")
            time.sleep(2)
            garden()
        else:
            slowText("You decided to scan the room. You find a shovel on the floor. Do you want to pick it up?")
            choice = input().strip().lower()
            if choice == "yes":
                backpack.append("shovel")
            time.sleep(2)
            garden()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(3)
        garden()

def bedroom():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("backpack: {}".format(backpack))
    slowText("You are in the bedroom. There is a door to the living room. You can also look for items.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "living room":
        livingRoom()
    elif choice == "look for items":
        if searchBackpack(backpack, "pillow"):
            slowText("You decided to scan the room. You find nothing.")
            time.sleep(2)
            bedroom()
        else:
            slowText("You decided to scan the room. You find a pillow on the bed. Do you want to pick it up?")
            choice = input().strip().lower()
            if choice == "yes":
                backpack.append("pillow")
                time.sleep(2)
                bedroom()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(3)
        bedroom()

def searchBackpack(pack, item):
    #this function should return true if item is inside the list named 'pack'
    found = False
    for i in range(len(pack)):
        if pack[i] == item:
            found = True
    return found

def openWindow():
    slowText("You decided to try to open the window.")
    if searchBackpack(backpack, "paper clip") == True:
        slowText("You use the paperclip to unlock the window, but it still won't budge open. You need to try to break the window with something strong to get out.")
        if searchBackpack(backpack, "shovel") == False:
                slowText("You have nothing to break the window with.")
                time.sleep(2)
                kitchen()
        choice = input().strip().lower()
        if choice == "use shovel":
            if searchBackpack(backpack, "shovel") == True:
                slowText("You use the shovel to break the window open, but there is a man outside holding a pillow. In order to escape, you must have a pillow fight.")
        elif choice == "pillow fight":
            if searchBackpack(backpack, "pillow") == True:
                slowText("You have a pillow fight with the man and win, you escape!")
                time.sleep(3)
                start()
            elif searchBackpack(backpack, "pillow") == False:
                slowText("You have no pillow to fight with and you cannot escape.")
                time.sleep(2)
                kitchen()
    else:
        slowText("Unfortunately, you can't open the window.")
        time.sleep(2)
        kitchen()
playerName = ""
backpack = []
start()