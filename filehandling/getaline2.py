import linecache
print()
with open("roadnottaken.txt", "r") as file:
    original = file.read()
    
print(original)

line_num = int(input("\nWhat line would you like to print? "))

print()
print(linecache.getline('roadnottaken.txt', line_num))