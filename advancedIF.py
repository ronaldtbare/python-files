# Advanced IF statements

age = 7
height = 140

# and
if age >= 8 and height >= 135:
   print("you can ride the ride")

# or
if age >= 17 or height >= 160:
    print("You can ride the super ride.")

# elif (else if)
if height < 120:
    print("You can't ride any rides.")
elif height < 135:
    print("You cn ride level-1 rides.")
elif height < 200:
    print("You can ride any ride.")
else:
    print("Too tall to ride any ride.")

# You can combine and and or
if height > 5 and height < 100 or height > 150:
    print("Have fun and ride the ride.")