temp = int(input("What is the temperature outside? "))

if temp <= 32:
    print("It is freezing outside!")
elif temp > 32 and temp < 55:
    print("It is cool, grab a jacket.")
elif temp > 55 and temp < 88:
    print("It is fairly nice outside.")
elif temp > 88:
    print("It is hot outside!")


