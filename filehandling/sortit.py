# read a random set of names from a file
# put in a list using readline()
# sort the names
# write them to a new file called sortednames.txt

#opens the file for reading
with open("names.txt", "r") as file:
    name_list = file.readlines()

print("This is the original file: \n")    
print(name_list)

print()

# sorts the list
name_list.sort()

print("This is the sorted file: \n") 

print(name_list)    
   
# writes a new file containing the sorted list
with open("sortednames.txt", "w+") as file:
    for name in name_list:
        file.write(name)

print("\n*** sortednames.txt file created. ***\n")