
# Old Bubble sort algorythm

my_list = []
swapped = True

number = int(input("How many elements do you want to sort? "))

for i in range(number):
    val = input("Enter a list element: ")
    my_list.append(val)
print("Unsorted list: ", my_list)

# Nested Loop control
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] # swap list items
        
# print sorted list         
print()
print("Sorted List = ", my_list)
print()



            
    
