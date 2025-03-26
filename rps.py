# Rock, paper, scissors game

import random

choices = ('r', 'p', 's')
rps = {'r':'Rock', 'p':'Paper', 's':'Scissors'}

print('\n*** Rock, Paper, Scissors Game ***')

while True:
    user_choice = input('\nRock, paper or scissors? (r/p/s) ').lower()
    if user_choice not in choices:
        print("Invalid choice.")
        continue

    computer_choice = random.choice(choices)
    
    print(f"\nYou chose {rps[user_choice]}")
    print(f"Computer chose {rps[computer_choice]}")

    if user_choice == computer_choice:
        print("\nThat is a TIE!!")
        continue

    if  ((user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')):
        print("\nYou win!!!")
    else:
        print("\nComputer wins!!!")
    
    play = input("\nPlay again? (y/n) ").lower()
    if play == 'n':
        break



    