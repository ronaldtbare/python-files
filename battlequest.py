# Battle Quest
# randomly pick a monster
# - name, health, damage
# create character
# - name, health, damage
# function to roll dice
# turn based
# stats function

import random
import os
import time
import sys

def roll_it(sides):
    roll = random.randint(1, sides)
    return roll


def my_monster_stat(my_monster):
    print(f"\nMonster: {my_monster['name']}") 
    print(f"Health: {my_monster['health']}") 
   
   
def player_stat(player):
    print(f"\nPlayer: {player['name']}")
    print(f"Health: {player['health']}") 
   

def damage(damage_range):
    damage = random.randint(1, damage_range)
    return damage


def monster_dead():
    if my_monster["health"] < 1:
        my_monster_stat(my_monster)
        player_stat(player)
        print("\nYou WIN!")
        print(f"You have defeated the {my_monster['name']}!\n")
        # sys.exit()
        return "no"


def pick_monster():
    # a list of dictionaries
    monsters = [
    { "name" : "Ogre" , "health" : 9, "damage" : 4},

    { "name" : "Kobold" , "health" : 8, "damage" : 3},

    { "name" : "Troll" , "health" : 7, "damage" : 4},

    { "name" : "Grue" , "health" : 8, "damage" : 5},
    ]
    chosen_monster = random.choice(monsters)
    return chosen_monster


def player_dead():
    if player["health"] < 1:
        os.system('clear')
        my_monster_stat(my_monster)
        player_stat(player)
        print("\nGame Over!!")
        print(f"You have been defeated by the {my_monster['name']}!\n")
        # sys.exit()
        return "no"


def playbattle():
    os.system('clear')

    print(f"\nYou have encountered a {my_monster['name']} and must defend yourself!")

    while True: # battle loop
        
        my_monster_stat(my_monster)
        player_stat(player)

        choice = input("\nEnter 'a' to attack and press <Enter> : ").lower()

        if choice == "a":
            time.sleep(1)
            print("\nYou attack!")
            to_hit = roll_it(20)
            if to_hit >= 7:
                time.sleep(.5)
                print(f"\nYou hit the {my_monster['name']}!!!")
                player_damage = damage(player["damage"])
                time.sleep(1)
                print(f"You did {player_damage} damage.")
                my_monster["health"] -= player_damage
                
            elif to_hit <= 6:
                time.sleep(.5)
                print(f"\nYou swing and miss the {my_monster['name']}!!!!")
        else:
            print("Try again.")
            time.sleep(1)
            os.system('clear')
            continue

        monster_alive = monster_dead()
        player_alive = player_dead()

        if monster_alive == "no" or player_alive == "no":    
            return "check"

        print("\n**********************")
        print(f"\n{my_monster['name']}'s turn:")
        time.sleep(.5)
        print(f"{my_monster['name']} attacks!")

        to_hit = roll_it(20)
        if to_hit >= 7:
            time.sleep(.5)
            print(f"\nThe {my_monster['name']} has hit you!!!")
            monster_damage = damage(my_monster["damage"])
            time.sleep(1)
            print(f"Monster did {monster_damage} damage.")
            player["health"] -= monster_damage
                
        elif to_hit <= 6:
            time.sleep(.5)
            print(f"\n{my_monster['name']} swings and misses you!!!!")

        monster_alive = monster_dead()
        player_alive = player_dead()

        if monster_alive == "no" or player_alive == "no":    
            return "check"
        time.sleep(2)
        os.system('clear')


# Print title
os.system('clear')
print('''
 ____        _   _   _         ___                  _   
| __ )  __ _| |_| |_| | ___   / _ \ _   _  ___  ___| |_ 
|  _ \ / _` | __| __| |/ _ \ | | | | | | |/ _ \/ __| __|
| |_) | (_| | |_| |_| |  __/ | |_| | |_| |  __/\__ \ |_ 
|____/ \__,_|\__|\__|_|\___|  \__\_\\__,_|\___||___/\__|

''')

global my_monster
my_monster = pick_monster()

global player
player = {"name": "player", "health": 8, "damage": 4}

time.sleep(1)
player['name'] = input("What is thy name? ")

while True:

    check = playbattle()
    if check == "check":
        play = input("Play again? (y/n) ")
        if play == "n":
            print()
            break
        else:
            my_monster = pick_monster()
            player['health'] = 8
            continue

