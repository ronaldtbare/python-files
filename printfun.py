# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()
# my_list = [5,4,3]
# my_list[0].remove()
# print(my_list)
limit = int(input("Enter the factorial number: "))

answer = 1
for number in range(limit,0,-1):
    # print(number)
    answer = answer * number
print(f"{limit}! = {answer}")




