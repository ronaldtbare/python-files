# 90s Trivia Game

# REQUIREMENTS
# must include a function
# must pull random 5 questions from a bank of question for each game
# must communicate effecitvely with users
# data structure is a list of dictionaries - question, options, answer
# keep score
# check for valid user input

import time
import os
import random

# bank of questions - a list of dictionaries
bank = [
    {
        "question": "Which 90s band is known for their hit song 'Smells Like Teen Spirit'?",
        "options": ["1. Pearl Jam", "2. Soundgarden", "3. Nirvana", "4. Alice in Chains"],
        "answer": "3"
    },
    {
        "question": "What was the name of the 90s pop group that had a hit with 'Backstreets Back'?",
        "options": ["1. Spice Girls", "2. Backstreet Boys", "3. N'Sync", "4. Destiny's Child"],
        "answer": "2"
    },
    {
        "question": "Who is the artist behind the 90s hit song 'Waterfalls'?",
        "options": ["1. TLC", "2. Mariah Carey", "3. Whitney Houston", "4. Janet Jackson"],
        "answer": "1"
    },
    {
        "question": "Which 90s rapper is known for his album 'Ready to Die'?",
        "options": ["1. Tupac", "2. Biggie Smalls", "3. Dr. Dre", "4. Nas"],
        "answer": "2"
    },
   
    {
        "question": "Which 90s pop group had a hit with the song 'Wannabe'?",
        "options": ["1. Backstreet Boys", "2. Spice Girls", "3. N'Sync", "4. Destiny's Child"],
        "answer": "2"
    },
    {
        "question": "Who is the artist behind the 90s hit song 'Ironic'?",
        "options": ["1. Alanis Morissette", "2. Sheryl Crow", "3. Fiona Apple", "4. Jewel"],
        "answer": "1"
    },
   
    {
        "question": "Which 90s rapper is known for his album 'The Chronic'?",
        "options": ["1. Tupac", "2. Biggie Smalls", "3. Dr. Dre", "4. Nas"],
        "answer": "3"
    },
    {
        "question": "What was the name of the 90s pop group that had a hit with 'Bye Bye Bye'?",
        "options": ["1. Backstreet Boys", "2. Spice Girls", "3. N'Sync", "4. Destiny's Child"],
        "answer": "3"
    },
    {
        "question": "Which 90s band is known for their hit song 'Wonderwall'?",
        "options": ["1. Oasis", "2. Blur", "3. Radiohead", "4. Nirvana"],
        "answer": "1"
    },
    {
        "question": "What was the name of the 90s R&B group that had a hit with 'End of the Road'?",
        "options": ["1. Boyz II Men", "2. TLC", "3. Blackstreet", "4. En Vogue"],
        "answer": "1"
    },
    {
        "question": "Who is the artist behind the 90s hit song 'Genie in a Bottle'?",
        "options": ["1. Britney Spears", "2. Christina Aguilera", "3. Mariah Carey", "4. Jennifer Lopez"],
        "answer": "2"
    },
    {
        "question": "Which 90s band is known for their hit song 'Glycerine'?",
        "options": ["1. Bush", "2. Stone Temple Pilots", "3. Foo Fighters", "4. Green Day"],
        "answer": "1"
    },
    {
        "question": "Which 90s rapper is known for his album 'Me Against the World'?",
        "options": ["1. Tupac", "2. Biggie Smalls", "3. Dr. Dre", "4. Nas"],
        "answer": "1"
    },
    {
        "question": "Which 90s rapper is known for his album 'Ready to Die'?",
        "options": ["1. Tupac", "2. Biggie Smalls", "3. Dr. Dre", "4. Nas"],
        "answer": "2"
    },
    {
        "question": "What was the name of the 90s grunge band fronted by Eddie Vedder?",
        "options": ["1. Nirvana", "2. Soundgarden", "3. Pearl Jam", "4. Alice in Chains"],
        "answer": "3"
    },
    {
        "question": "Which 90s pop group had a hit with the song 'Wannabe'?",
        "options": ["1. Backstreet Boys", "2. Spice Girls", "3. N'Sync", "4. Destiny's Child"],
        "answer": "2"
    },
    {
        "question": "Who is the artist behind the 90s hit song 'Ironic'?",
        "options": ["1. Alanis Morissette", "2. Sheryl Crow", "3. Fiona Apple", "4. Jewel"],
        "answer": "1"
    },
    {
        "question": "Which 90s band is known for their hit song 'Creep'?",
        "options": ["1. Oasis", "2. Blur", "3. Radiohead", "4. Nirvana"],
        "answer": "3"
    },
    {
        "question": "What was the name of the 90s R&B group that had a hit with 'No Diggity'?",
        "options": ["1. Boyz II Men", "2. TLC", "3. Blackstreet", "4. En Vogue"],
        "answer": "3"
    },
    {
        "question": "What was the name of the 90s pop group that had a hit with 'Bye Bye Bye'?",
        "options": ["1. Backstreet Boys", "2. Spice Girls", "3. N'Sync", "4. Destiny's Child"],
        "answer": "3"
    },
    {
        "question": "Who is the artist behind the 90s hit song 'Torn'?",
        "options": ["1. Alanis Morissette", "2. Sheryl Crow", "3. Natalie Imbruglia", "4. Jewel"],
        "answer": "3"
    },
    {
        "question": "Which 90s band is known for their hit song 'Wonderwall'?",
        "options": ["1. Oasis", "2. Blur", "3. Radiohead", "4. Nirvana"],
        "answer": "1"
    },
    {
        "question": "What was the name of the 90s R&B group that had a hit with 'End of the Road'?",
        "options": ["1. Boyz II Men", "2. TLC", "3. Blackstreet", "4. En Vogue"],
        "answer": "1"
    },
   
    {
        "question": "What was the name of the 90s R&B group that had a hit with 'Bills, Bills, Bills'?",
        "options": ["1. Boyz II Men", "2. TLC", "3. Blackstreet", "4. Destiny's Child"],
        "answer": "4"
    },
    {
        "question": "Who is the artist behind the 90s hit song 'Smooth'?",
        "options": ["1. Santana ft. Rob Thomas", "2. Alanis Morissette", "3. Sheryl Crow", "4. Jewel"],
        "answer": "1"
    },
    {
        "question": "What was the name of the 90s grunge band fronted by Layne Staley?",
        "options": ["1. Pearl Jam", "2. Soundgarden", "3. Alice in Chains", "4. Stone Temple Pilots"],
        "answer": "3"
    },
    {
        "question": "Which 90s rapper is known for his album 'Me Against the World'?",
        "options": ["1. Tupac", "2. Biggie Smalls", "3. Dr. Dre", "4. Nas"],
        "answer": "1"
    },
    {
        "question": "What was the name of the 90s pop group that had a hit with 'Say You'll Be There'?",
        "options": ["1. Spice Girls", "2. Backstreet Boys", "3. N'Sync", "4. Destiny's Child"],
        "answer": "1"
    },
    {
        "question": "Who is the artist behind the 90s hit song 'You Oughta Know'?",
        "options": ["1. Alanis Morissette", "2. Sheryl Crow", "3. Fiona Apple", "4. Jewel"],
        "answer": "1"
    },
    {
        "question": "Which 90s band is known for their hit song 'Black Hole Sun'?",
        "options": ["1. Pearl Jam", "2. Soundgarden", "3. Alice in Chains", "4. Stone Temple Pilots"],
        "answer": "2"
    },
    {
        "question": "What was the name of the 90s R&B group that had a hit with 'No Scrubs'?",
        "options": ["1. Boyz II Men", "2. TLC", "3. Blackstreet", "4. Destiny's Child"],
        "answer": "2"
    },
        {
        "question": "Which 90s band had a hit with the song 'Zombie'?",
        "options": ["1. The Cranberries", "2. Smashing Pumpkins", "3. Hole", "4. Soundgarden"],
        "answer": "1"
    },
        {
        "question": "Which 90s band had a hit with the song 'Don't Speak'?",
        "options": ["1. No Doubt", "2. Bush", "3. Gwen Stefani", "4. Garbage"],
        "answer": "1"
    },
    {
        "question": "Which 90s band had a hit with the song 'Kiss From a Rose'?",
        "options": ["1. Seal", "2. U2", "3. Coldplay", "4. The Script"],
        "answer": "1"
    },
    {
        "question": "Which 90s band had a hit with the song 'Iris'?",
        "options": ["1. Goo Goo Dolls", "2. Foo Fighters", "3. Weezer", "4. Green Day"],
        "answer": "1"
    },
    {
        "question": "Which 90s band had a hit with the song 'Today'?",
        "options": ["1. Smashing Pumpkins", "2. Foo Fighters", "3. Weezer", "4. Green Day"],
        "answer": "1"
    },
    {
        "question": "Who is the artist behind the 90s hit song 'Gangsta's Paradise'?",
        "options": ["1. Coolio", "2. Snoop Dogg", "3. Dr. Dre", "4. Snoop Dogg & Nate Dogg"],
        "answer": "1"
    },
    {
        "question": "Who is the artist behind the 90s hit song 'Jump'?",
        "options": ["1. Kris Kross", "2. NSYNC", "3. Backstreet Boys", "4. Spice Girls"],
        "answer": "1"
    }
]

questions = random.sample(bank,5) # this picks UNIQUE items from bank holds the current game questions
   
# positive and negative feedback lists
feedbackyes = ["Peachy King!", "You got that right!", "Good job1!", "Way to go!", "Aye Aye! Captain!", "Cool Beans!"]
feedbackno = ["Not on my watch!", "UUUGGGGGHH!!!", "Remarkably wrong!", "BAD pilgrim!", "You missed!", "Boooooo!!!", "NADA!"]


def ask_it(question_number):
    os.system("clear")
    
    # print title
    print()
    print(f"""
    ***  𝟡𝟘❜𝕤 𝕄𝕦𝕤𝕚𝕔 𝕋𝕣𝕚𝕧𝕚𝕒  ***
    """)
    # print the question
    print()
    print(f"Question # {question_number + 1}\n")
    print(questions[question_number]["question"])
    print()
    for i in range(0,4):
        print(questions[question_number]["options"][i])
    print()
    return question_number

score = 0
choices = ["1", "2", "3", "4"]


while True: # game loop

    for x in range(len(questions)):
        qn = ask_it(x)

        # check for valid user input
        while True:
            user_input = str(input("Enter your answer(1,2,3,4) : "))
            if user_input in choices:
                break
            else:
                print("Please input 1,2,3, or 4.")
                time.sleep(1) 
        # checks if the answer is correct
        if user_input == questions[qn]["answer"]:
            time.sleep(1)
            print()
            print(random.choice(feedbackyes))
            score += 1
        else:
            time.sleep(1)
            print()
            print(random.choice(feedbackno))
        time.sleep(2)
        
    # print score
    print(f"\nYour score is {score} out of {len(questions)} questions!\n")
    # exit game loop?
    play = input("Play again? (y/n) ")
    if play == "n":
        print()
        
        break
    else: 
        score = 0 # reset score for next game
        questions = random.sample(bank,5)  # reset questions for next game

os.system("clear")
