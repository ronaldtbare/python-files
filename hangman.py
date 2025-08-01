# Python Hangman Game by Travis Bare

import random


def printGallows(number):
  hangman_pics = ['''
    +---+
    |   |
        |
        |
        |
   ------
  ''', '''
    +---+
    |   |
    O   |
        |
        |
   ------
  ''', '''
    +---+
    |   |
    O   |
    |   |
        |
   ------
  ''', '''
    +---+
    |   |
    O   |
   /|   |
        |
   ------
  ''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
   ------
  ''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
   ------
  ''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
   ------
  ''']
  print(hangman_pics[number])
  return


def printBlanks():
  for x in range(0, len(blanks_holder)):
    print(blanks_holder[x], end=" ")
  return


def youLose():
  print()
  print("*" * 40)
  print((" " * 17) +"HANGMAN")
  print("*" * 40)
  print()
  print(f"Total guesses: {guesses_counter}    Wrong guesses: {wrong_guesses}")
  print("Your guessed letters:",' '.join(guessed_letters))
  printGallows(6)
  print()
  printBlanks()
  print("<- Guess this word.")
  print()
  print("The word was", secret_word)
  print()
  print("******************")
  print("*** You Lose!! ***")
  print("******************")
  print()
  return
  

def youWin():
  print()
  print("*" * 40)
  print((" " * 17) +"HANGMAN")
  print("*" * 40)
  print()
  print(f"Total guesses: {guesses_counter}    Wrong guesses: {wrong_guesses}")
  
  print("Your guessed letters:",' '.join(guessed_letters))
  print()
  print("The word was", secret_word)
  print()
  print("******************")
  print("*** You Win!! ****")
  print("******************")
  print()
  return

 
def getGuess():
    guess = input("Enter your letter guess: ").lower().strip()
    return guess

words = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose gopher groundhog hamster horse kangaroo lion lizard monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".split()

# variables

secret_word = words[random.randint(0, len(words))]
# print(secret_word)
letter_list = list(secret_word)
flag = False
guessed_letters = []
blanks_holder = []
guesses_counter = 0
wrong_guesses = 0
play = True

for letter in letter_list:
  blanks_holder.append("_")


def playGame():

  while letter_list != blanks_holder:
    
    if wrong_guesses != 6:
      print()
      print("*" * 40)
      print((" " * 17) +"HANGMAN")
      print("*" * 40)
      print()
      print(f"Total guesses: {guesses_counter}    Wrong guesses: {wrong_guesses}")
      
      print("Your guessed letters:",' '.join(guessed_letters))
      printGallows(wrong_guesses)
      printBlanks()
      print("<- Guess this word.")
      print("\n")
      # print(blanks_holder)
      
      guess = getGuess()
      guesses_counter += 1
      guessed_letters.append(guess)

      # test if guess is in the word and increment wrong_guesses
      if guess in letter_list:
        print(f"{guess} is in the word.")
      else:
        wrong_guesses +=1
        print(f"{guess} is NOT in the word.")

      flag = False
      
      for x in range(0, len(letter_list)):
        # print(x)
        if guess == letter_list[x]:
          # print(guess, letter_list[x])
          blanks_holder[x] = guess
        elif guess != letter_list[x]:
          flag = True

    if wrong_guesses == 6:
      youLose()
      return
    
    if letter_list == blanks_holder:
      youWin()
      return

again = str(input("Play again? (y/n) : ")).lower()
print(again)
if again == "n" or again == "no":
  play = False
    

