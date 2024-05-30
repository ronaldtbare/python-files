
# The second argument "x" says to only open if the file does not exist.
# file = open("myfile.txt", "x")

# file.write("This is some random text in the file.")

# file.close()


# The "w" says to write over the file if it exists or create it.
# file = open("myfile.txt", "w")

# file.write("Mary had a little lamb.")

# file.close()


# The "a" will append to an existing file
file = open("myfile.txt", "a")

file.write("Yo ho! A pirate's life for me.")

file.close()

