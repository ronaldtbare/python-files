# Import module
import tkinter as tk
from PIL import ImageTk, Image 
import random
import os


# create root window
root = tk.Tk()

# root window title and dimensions
root.title("TkWordGuess")
# Set geometry(width x height)
root.geometry('350x350')


# adding image to program
image1 = Image.open("title.gif")
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(root, image=test)
label1.grid(padx=0,pady=0, column=0,row=0)





words = ["human", "chimpanzee", "orangutan", "gorilla", "bonobo", "gibbon"]

chosen_word = random.choice(words)
# print(chosen_word)
word_display = ["_" for _ in chosen_word]
missed_letters = []
attempts = 6
print(f"You have {attempts} attempts to guess the letters.")

while attempts > 0 and "_" in word_display:
    os.system('clear')
    print("\n***** Word Guesser Game ******")
    print("\nYou have to guess this word.")
    print(f"Missed letter guesses: {attempts}")
    print(f"Missed letter list: {missed_letters}")
    print("\n" + " ".join(word_display))
    
    guess = input("Guess a word = ["human", "chimpanzee", "orangutan", "gorilla", "bonobo", "gibbon"]

chosen_word = random.choice(words)
# print(chosen_word)
word_display = ["_" for _ in chosen_word]
missed_letters = []
attempts = 6
print(f"You have {attempts} attempts to guess the letters.")

while attempts > 0 and "_" in word_display:
    os.system('clear')
    print("\n***** Word Guesser Game ******")
    print("\nYou have to guess this word.")
    print(f"Missed letter guesses: {attempts}")
    print(f"Missed letter list: {missed_letters}")
    print("\n" + " ".join(word_display))
    
    guess = input("Guess a letter: ").lower()
    
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess # reveals the letter
    else:
        print("That letter is not in the word.")
        attempts -= 1
        missed_letters.append(guess)
    

# Game conclusion
os.system('clear')
if "_" not in word_display:
    print("\nYou guessed the word!")
    print("".join(word_display))
    print("You win!\n")
else:
    print(f"\nYou ran out of guesses. The word was {chosen_word}.")
    print("You lose!\n")tter: ").lower()
    
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess # reveals the letter
    else:
        print("That letter is not in the word.")
        attempts -= 1
        missed_letters.append(guess)
    

# Game conclusion
os.system('clear')
if "_" not in word_display:
    print("\nYou guessed the word!")
    print("".join(word_display))
    print("You win!\n")
else:
    print(f"\nYou ran out of guesses. The word was {chosen_word}.")
    print("You lose!\n")





# Execute Tkinter (run it)
root.mainloop()