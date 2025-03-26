# Guessing game!

import random
import time

def you_win():
    print()
    print("**********************")
    print("**** You Win!!! ******")
    print("**********************")
    print()
    print(f"The correct number is {correct_number}.")
    print(f"It took you {guess_count} guesses.\n")

def you_lose():
    print()
    print(f"The correct number is {correct_number}.")
    print()
    print("**********************")
    print("**** You Lose!! ******")
    print("**********************")
    print()
    print("Too many guesses!\n")
    
#################################################################

print()
print("*" * 50)
print("********** Number Guessing Game ******************")
print("*" * 50)
print()
print("Guess a number between 1 and 100. You only get 7 guesses.\n")
time.sleep(2)
print("I am picking a number.....\n")
time.sleep(1)

guess_count = 1

guess = int(input(f"Guess #{guess_count}. What is your guess? "))

correct_number = random.randint(1,10)


while guess != correct_number:

    

    if guess < correct_number:
        time.sleep(.5)
        print("That's too LOW. Try again.\n")
    if guess > correct_number:
        time.sleep(.5)
        print("That's too HIGH. Try again.\n")
    if guess_count == 7:
        you_lose()
        break

    guess_count += 1

    guess = int(input(f"Guess #{guess_count}. What is your guess? "))
   
    

if guess == correct_number:
        you_win()




