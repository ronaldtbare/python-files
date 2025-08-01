

word = input("Enter an adjective: ")


with open("stuff.txt", "r") as file:
    original = file.read()
    
print(original)

changed = original.replace("random", word)

print(changed)


with open("stuff.txt", "w") as file:
    file.write(changed)