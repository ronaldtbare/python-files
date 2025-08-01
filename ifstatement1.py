print(f"""

You have been walking in the cave \nfor quite a distance.  You
have come to a fork and must choose \nthe left passage or the 
right passage.

""")

choice = input("Which do you choose?  \n1. right   or   \n2. left\n: ")

if choice == "1":
    print("""
    
    Ok, so you chose to walk down the \n   right pathway.  Unfortunately,
    you run into a giant spider.  
    
    """)

    choice2 = input("You must make a choice.  \n1. fight or  \n2. Try to escape  \n:")

    if choice2 == "1":
        print("\nThe spider lunges at you! \nYou dodge the attack and a big rock falls on the spider. \n You survived!")
    else:
        print("\nYou run back the other way, and manage to escape!")


else:
    print("""

    As you slowly walk down the left \n   pathway,  you see a faint light ahead
    and some low murmuring. 
    
    """)

    choice3 = input("You must make a choice.  \n1. run into the room or \n2. sneak past the room  \n: ")
 
    if choice3 == "1":
        print("\nMany ogres in the room are alarmed and attack you! \nYou try but fail!")
    else:
        print("\nYou manage to sneak passed the room to safety! Yay!")




