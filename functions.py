
# print()

# string.split()

# name.lower()

# def howdy():  # define the function
#     print("Hello, world!")
#     print("My name is Bob.")


# howdy() # call the function

# def greet(first_name, last_name): # there are 2 parameters
#     print(f"Greetings {first_name} {last_name}!")


# greet("Jon", "Tyler") # this call has 2 arguments
# greet("Travis", "Bare")

# dice roller - function

import random

def rollit(sides): # has 1 parameter
    roll = random.randint(1, sides)
    print(f"Using a {sides} sided die, you rolled a {roll}.")


die_sides = int(input("Enter amount of sides: "))

rollit(die_sides)

