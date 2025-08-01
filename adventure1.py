import os

os.system('clear')

rooms = {
    "dining room" : {
                "south" : "garden",
                "west" : "hall",
                "item" : "potion"
                },
    "garden" : {
                "north" : "dining room",
                "item" : "axe"
                },
    "hall" : {
                "south" : "kitchen",
                "east" : "dining room",
                "item" : "key"
                },
                         
    "kitchen": {
                "north" : "hall",
                "item"  : "monster"
                },


        }

def showInstructions():
    print('''
Simple RPG Haunted Mansion Game
================================
Commands:
go [north, south, east, west]
get [item]

To win: collect key and potion to leave through garden gate or
        defeat monster with the axe.  
    ''')


def status():
    print(f'''
-------------
You are in the {currentRoom}.
Inventory: {inventory}
-------------  
    ''')
    if "item" in rooms[currentRoom] and rooms[currentRoom]["item"]:
        roomItem = rooms[currentRoom]["item"]
        print(f"You see a {roomItem}!\n")


inventory = []

currentRoom = "hall"

showInstructions()

while True:  # Game loop
    status()
    
    move = input("> ")
    move = move.split(" ", 1)
    os.system('clear')
    if move[0] == "get":
        if move[1] == rooms[currentRoom]["item"]:
            print(f"You got a {move[1]}!")
            inventory.append(move[1])
            rooms[currentRoom]["item"] = ""
            # print(inventory)
        else:
            print(f"You already got the {move[1]}!")

    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            # print(f"You are now in the {currentRoom}.")
        else:
            print(f"You cant go {move[1]}.")

    # win scenario 1
    if "key" in inventory and "potion" in inventory and currentRoom == "garden":
        status()
        print("You have poured the potion on the gate lock and used the key to escape the Haunted Mansion!!")
        print("\nYou win!!!")
        break
    if rooms[currentRoom]["item"] == "monster" and "axe" in inventory:
        status()
        print("You have defeated the monster with the axe!")
        print("\nYou win!!!\n")
        break
    # loss scenario
    if "item" in rooms[currentRoom] and rooms[currentRoom]["item"] == "monster":
        status()
        print("\nYou have been eaten by the monster!")
        print("\nGAME OVER!\n")
        break


