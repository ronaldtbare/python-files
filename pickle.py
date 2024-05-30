import pickle

age =  33

file = open("text.txt", "wb") # b is for binary
pickle.dump(age, file)
file.close()

file = open("text.txt", "rb") # b is for binary
new_age = pickle.load(file)
file.close()

print(new_age)