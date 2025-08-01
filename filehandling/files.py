# Basic file handling practice

# open file and put contents in a variable and print to terminal

file = open('stuff.txt', 'r')

contents = file.read()

print(contents)

file.close()

#opens file and prints the file

file = open('stuff.txt', 'r')

print(file.read())

# opens file and appends a line of text

file.close()

file = open('more.txt', 'a')

file.write("Have a happy day!")


file.close()