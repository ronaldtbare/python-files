# Read

# file = open("myfile.txt","r")
# lines = file.readlines()
# file.close()


# Edit

# lines = ["Hello\n", "My name is Weezer."]

# lines.insert(0,"I like cheese.\n") # 0 is the position, at the beginning.

# lines[1] = "Hello friend!\n"

# lines[-1] = lines[-1] + "\n" # gets last line in file and appends "newline" to it
# lines.append("Goodbye!")


# Write

# file = open("myfile.txt", "w")
# file.writelines(lines)
# file.close()

# Challenge - make all numbers in numbers.txt be multipied by 2

file = open("numbers.txt", "r")
lines = file.readlines()
file.close()


for x in range(0,len(lines)):
    new_num = int(lines[x]) * 2
    lines[x] = f"{new_num}\n"
   

file = open("new_numbers.txt", "w")
file.writelines(lines)
file.close()

