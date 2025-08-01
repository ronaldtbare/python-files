# write to a file then read it

file = open("example1.txt", "a")

file.write("Hello world!\n")

file.close()

file = open("example1.txt", "r")

print(file.read())

file.close()