# This program demonstrates how to work with files

# Open file for writing and create it if it does not exit "+""
#myfile = open("textfile.txt", "w+")

# append data to a file.
# myfile = open("textfile.txt", "a+")

# # write some lines of data to file.
# for i in range(5):
#     myfile.write("This is some more random text\n")

# # close file when done.
# myfile.close()

# Open the file back up and read the contents
myfile = open("textfile.txt", "r")
if myfile.mode == "r":  # ensures that file is set for read mode
    # contents = myfile.read() # reads entire file
    # print(contents)
    fileline = myfile.readlines()
    for i in fileline:
        print(i)









