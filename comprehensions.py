# Count the number of spaces in a string

# string = "The quick brown fox jumped over the lazy dog."

# space = [s for s in string if s == " "]

# print(len(space))

# word_count = len(space) + 1

# print("The word count is", word_count)

# # create a list of all the consonants in a string

# sentence = "yellow yaks like yelling and yawning and yesterday they yodled while eating yucky yams"

# result = [letter for letter in sentence if letter not in "a,e,i,o,u,''"]

# print(result)

# find the common numbers in the two lists

# list1 = [1,2,3,4]
# list2 = [2,3,4,5]
# common = [ num for num in list1 if num in list2]
# print(common)

# convert a string into a code where a's are b's, b's are c's, and c's are d's, etc

# message = input("Enter your message: ").lower()
# code = []

# for char in message:
#     if char == "a":
#         code.append("b")
#     if char == "b":
#         code.append("c")
#     if char == "c":
#         code.append("d")
#     if char == "d":
#         code.append("e")
#     if char == "e":
#         code.append("f")
#     if char == "f":
#         code.append("g")
#     if char == "g":
#         code.append("h")
#     if char == "h":
#         code.append("i")
#     if char == "i":
#         code.append("j")
#     if char == "j":
#         code.append("k")
#     if char == "k":
#         code.append("l")
#     if char == "l":
#         code.append("m")
#     if char == "m":
#         code.append("n")
#     if char == "n":
#         code.append("o")
#     if char == "o":
#         code.append("p")
#     if char == "p":
#         code.append("q")
#     if char == "q":
#         code.append("r")
#     if char == "r":
#         code.append("s")
#     if char == "s":
#         code.append("t")
#     if char == "t":
#         code.append("u")
#     if char == "u":
#         code.append("v")
#     if char == "v":
#         code.append("w")
#     if char == "w":
#         code.append("x")
#     if char == "x":
#         code.append("y")
#     if char == "y":
#         code.append("z")
#     if char == "z":
#         code.append("a")
#     elif char not in "'!', '.', ' '":
#         code.append(char)
    
# print(code)

# Get only the numbers in a sentence

# sentence = "In 1984 there were 13 instances of a protest with over 1000 people attending."
# words = sentence.split()
# print(sentence)
# print(words)
# result = [number for number in words if number.isnumeric()]
# print(result)

# Find all the words in a string that are less than 4 letters

sentence = "On a summer day Sommer Smith went swimming in the sun and his red skin stung"
words = sentence.split()
print(words)

result = [word for word in words if len(word) < 4]
print(result)