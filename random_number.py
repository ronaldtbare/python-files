import random

def random_num():
    global num
    num = random.randint(1, 3)
    return num

random_num()
print("*" * 30)
print("      Magic Eight Ball  ")
print("*" * 30)

if num == 1:
    print("yes")
elif num == 2:
    print("no")
else:
    print("maybe")

# print(random.randint(1, 20))

# print(random.random()) # chooses a float from 0 to 1






