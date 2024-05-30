import random

# class Dog:
#     info = "Furry four-legged canine"

#     def __init__(self):
#         print("I'm alive!")
#         self.lucky_number = random.randint(1,10)

# dog1 = Dog()
# dog2 = Dog()
# print(dog1.lucky_number)
# print(dog2.lucky_number)

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Buick", "LeSabre")
car2 = Car("Ford", "Crown Victoria")

print("Car 1 info: ", car1.make, car1.model)
print("Car 2 info: ", car2.make, car2.model)


