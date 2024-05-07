#  Python 3:  Fibonoacci sequence up to n.

# This function prints the Fionacci sequence.
def fib(n):
    # a = 0
    # b = 1
    a, b = 0, 1
    while a < n:
        print(a, end=' ') # Prints horizontally
        # a = b
        # b = a + b
        a, b = b, a+b

# This get a number from the user.       
print()
n = int(input("Input the upper limit of the Fibonacci sequence: "))

# This calls the function fib.
fib(n)
