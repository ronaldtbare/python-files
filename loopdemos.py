# print the Fibonacci sequence up to the 15th term

# a, b = 0, 1
# count = 0
# while count < 15:
#     print(a, end=" ")
#     a, b = b, a + b
#     count += 1
###############################################

# Find all the prime numbers between 1 and 50 using nested for and if 

# for x in range(1, 51):
#     for y in range(2, x):
#         if x % y == 0:
#             break
#     else:
#         print(x, sep=" ")
       
#######################################################################

# Print numbers from 1 to 5 except 3 using a for loop and continue statement

for num in range(1, 6):
    if num == 3:
        continue
    print(num)