from timeit import timeit

my_list = timeit.timeit(stmt='[1,2,3,4,5]', number=1000000)

my_tuple = timeit.timeit(stmt='(1,2,3,4,5)', number=1000000)

print("List: ", my_list)

print("Tuple: ", my_tuple)