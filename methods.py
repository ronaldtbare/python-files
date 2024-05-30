
import random

class Dog:
    info = "Furry four-legged canine"

    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1,10)
        self.name = name

    def bark(self):
        print(f"Woof! My name is {self.name} and my lucky number is {self.lucky_number}")

dog1 = Dog("Fido")
dog2 = Dog("Spot")

dog1.bark()
dog2.bark()