
import random # import sthe random number generator

class Animal:
    info = "a living organism that feeds on organic matter"

    def __init__(self, name): # The name variable is passed to Dog
        print("An animal is created!")
        self.name = name


class Dog(Animal):
    info = "Furry four-legged canine"

    def __init__(self, name): # The name variable is passed to Bulldog
        super().__init__(name) # This line calls the method of Animal
        print("A dog is created!")
        self.lucky_number = random.randint(1,10)
        

    def bark(self):
        print(f"Woof! My name is {self.name} and my lucky number is {self.lucky_number}")

class Bulldog(Dog):

    def __init__(self, name):
        super().__init__(name)
        print("A bulldog was created!")


dog1 = Bulldog("Fido")

dog1.bark()

print(dog1.name)


