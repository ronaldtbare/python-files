

print()
with open("roadnottaken.txt", "r") as file:
    original = file.read()
    
print(original)

line_num = int(input("\nWhat line would you like to print? "))


with open('roadnottaken.txt') as file:
    for i, line in enumerate(file):
        if i == line_num:  # Line numbers are zero-indexed
            print("\nHere is the line you chose: \n")
            print(line)
            break






