# word count

# Use three quotes at beginning and end of large strings

import string

raw_text = """ 
Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
"""

# remove punctuation - must import string to use
text = ""
for char in raw_text:
    if char not in string.punctuation:
        text += char


text_list = text.lower().split() # creates Python list of individual words.

def get_word():
     my_word = input("What word do you want to count? ")
     return my_word


print()
print("*" * 50)
print("Here is the text:")

print(raw_text)
print("*" * 50)
print()

my_word = get_word()

while my_word not in text_list:  # keeps prompting user to enter a valid word
    print("This word is NOT found in the text. Try again.")
    my_word = get_word()

if my_word in text_list:
    
    word_count = {}

    for word in text_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    occurance = word_count[f"{my_word.lower()}"]
            
    print("Here are the results.")
    print()
    print(f"Word: {my_word.lower()}  Occurance: {occurance}")
    print()









    