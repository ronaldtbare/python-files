# Battlecraft monster fighting
# create monster
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


def goblin_stat(goblin):
    print(f"\nMonster: {goblin["name"]}") # print("\nMonster: ", (goblin["name"]))
    print(f"Health: {goblin["health"]}") # print("\nHealth: ", (goblin["health"]))
   
   
def player_stat(player):
    print(f"\nPlayer: {player["name"]}")
    print(f"Health: {player["health"]}") 
   

def damage(damage_range):
    damage = random.randint(1, damage_range)
    return damage


def monster_dead():
    if goblin["health"] < 1:
        # goblin_stat(goblin)
        # player_stat(player)
        print("\nYou have defeated your foe!!!\n")
        sys.exit()


def player_dead():
    if player["health"] < 1:
        # goblin_stat(goblin)
        # player_stat(player)
        print("\nYou have died!!\n")
        sys.exit()
        
valid_choice = ("a", "q")

goblin = {"name": "goblin", "health": 8, "damage": 4}

player = {"name": "player", "health": 12, "damage": 5}

os.system('clear')

print("\nYou have encountered a goblin and must defend yourself!")

while True: # game loop
    
    goblin_stat(goblin)
    player_stat(player)

    choice = input("\nChoose (a)ttack or (q)uit : ").lower()
    if choice not in valid_choice:
        print("Invalid choice. Try again.")
        time.sleep(1)
        os.system('clear')
        continue
    if choice == "q":
        break

    if choice == "a":
        time.sleep(1)
        print("\nYou attack!")
        to_hit = roll_it(20)
        if to_hit > 7:
            time.sleep(.5)
            print("\nYou hit the monster!!!")
            player_damage = damage(player["damage"])
            time.sleep(1)
            print(f"You did {player_damage} damage.")
            goblin["health"] -= player_damage
            
        elif to_hit <= 6:
            time.sleep(.5)
            print("\nYou missed!!!!")

    monster_dead()
    player_dead()

    print("\n**********************")
    print("\nMonster's turn:")
    time.sleep(.5)
    print("Monster attacks!")

    to_hit = roll_it(20)
    if to_hit > 7:
        time.sleep(.5)
        print("\nMonster has hit you!!!")
        monster_damage = damage(goblin["damage"])
        time.sleep(1)
        print(f"Monster did {monster_damage} damage.")
        player["health"] -= monster_damage
            
    elif to_hit <= 6:
        time.sleep(.5)
        print("\nMonster missed!!!!")

    monster_dead()
    player_dead()

    time.sleep(2.5)
    os.system('clear')
