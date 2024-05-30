# The "r" says to write over the file if it exists or create it.
# This code reads the entire file at once.
file = open("myfile.txt", "r")
# file_text = file.read()
# print(file_text)

# This codes reads line by line.
# if the file has been read before, the read marker is at the
# end of the file and doesn't read anything else.  The list will be empty.

# lines = file.readlines()
# print(lines)

# Reading using a for loop.
# for line in file:
#     print(line)


# file.close() # Always close a file after opening or it will get corrupted by other opens.

# Challenge
# Create a file numbers.txt that has a few lines of numbers. 
# Multiply all the numbers together and print the result.

file = open("numbers.txt", "r")

for line in file:
    print(line)

file.close()