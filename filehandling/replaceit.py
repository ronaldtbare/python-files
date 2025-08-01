# open the file
# display to file to user
# ask user for the word to change
# Display changed file
# write new file


with open("gettysburg.txt", "r") as file:
    original = file.read()
    
print(original)

word = input("What word would you like to change? ")
replaced_word = input("What replacement word would you like to use? ")

changed = original.replace(word, replaced_word)

print("\nThis is the changed file: ")
print(changed)

with open("gettyburg2.txt", "w+") as file:
    file.write(changed)





