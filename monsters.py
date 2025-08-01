# This program randomly selects monsters and places them into the rooms.

import random

def pick_monster():
    monsters = [
    { "name" : "ogre" , "health" : 5},

    { "name" : "kobold" , "health" : 4},

    { "name" : "troll" , "health" : 8},

    ]

    chosen_monster = random.choice(monsters)

    return chosen_monster


rooms = {

"Passage1" : {
                "north": "Great Hall",
                "monster" : pick_monster()         
                },

"Great Hall" : {
                "south": "Passage1",
                "monster" : pick_monster()         
                },
}

print()
print(f"The Passage1 has a {rooms['Passage1']['monster']['name']}")
print(f"The Great Hall has a {rooms['Great Hall']['monster']['name']}\n")