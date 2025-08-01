# best practice for file handling

with open("example1.txt", "a") as file:
    file.write("Dude, Wheres my car!\n")

# Do more stuff down here

with open("example1.txt", "r") as file:
    print(file.read())

# do some more stuff

with open("animals.txt", "a+") as file:
    file.write("Cow\n")
    file.write("Horse\n")