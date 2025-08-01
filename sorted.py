my_list = [8, 10, 6, 2, 4]
my_list3 = ["dog", "cat", "bird", "fish", "zebra", "wombat", "platypus"]
my_list3 = []

num = int(input("How many items do you want to sort? "))

for i in range(num):
    value = input(f"Enter list item {i+1}: ")    
    my_list3.append(value)

swapped = True

# Nested Loop control
while swapped:
    swapped = False
    for i in range(len(my_list3) - 1):
        if my_list3[i] > my_list3[i + 1]:
            swapped = True
            my_list3[i], my_list3[i + 1] = my_list3[i + 1], my_list3[i] # swap list items
        
# print sorted list         
print()
print("Sorted List = ", my_list3)
print()