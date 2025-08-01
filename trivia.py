# This is a simple trivia game written in Python. 
import os
import time

questions = [

{
"prompt": "What was the first commercial web browser? ",
"options": ["A. Firefox", "B. Safari", "C. Netscape Navigator", "D. AOL"],
"answer": "C"
},

{
"prompt": "Who starred in the hit movie 'The Matrix'? ",
"options": ["A. Jennifer Lopez", "B. Christopher Walken", "C. Keanu Reeves", "D. Bruce Willis"],
"answer": "C"
},

{
"prompt": "What was Chandler's last name on the show Friends? ",
"options": ["A. Jones", "B. Robinson", "C. Bing", "D. Smith"],
"answer": "C"
},

{
"prompt": "What band had the hit song 'Sandman'? ",
"options": ["A. B-52's", "B. Blind Melon", "C. Nickelback", "D. Metallica"],
"answer": "D"
},

{
"prompt": "Complete this title, '3rd Rock from the _____? ",
"options": ["A. tree", "B. moon", "C. sun", "D. Left"],
"answer": "C"
}
]

# Title
print(" __________________________________________")
print("|                                          |")
print("|            9O's Trivia Game              |")
print("|                                          |")
print(" __________________________________________")
print()
print("Welcome to the 9O's Trivia Game!  Good luck!")
print()

score = 0

for question in questions: # Loops through each dictionary in the list
    os.system('clear')
    # Title
    print(" __________________________________________")
    print("|                                          |")
    print("|         9O's Trivia Game                 |")
    print("|                                          |")
    print(" __________________________________________")
    print()
    print("Welcome to the 9O's Trivia Game!  Good luck!")
    print()
    print(f"Question # {questions.index(question)+1}")
    print(question["prompt"])
    for option in question["options"]:
        print(option)
    answer = input("Enter your answer (A,B,C, or D): ").upper()
    print()
    
    if answer == question["answer"]:
        print("That is correct! \n")
        score += 1
        time.sleep(3)
    else:
        print("Oopsies!  That is wrong.")
        print(f"The correct answer is {question["answer"]} \n")
        time.sleep(3)

print(f"You got {score} out of {len(questions)} questions correct.")
print("Thanks for playing!!!")





