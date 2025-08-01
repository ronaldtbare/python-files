# python classes

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36) # p1 object created
p2 = Person("Mary", 28) # p2 object created
print() 
print(p1.name)
print(p1.age)
print()
print(p2.name)
print(p2.age)
print()

print("-"*30)

class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		
	def horn(self):
		message = f"BEEP! BEEP! I am a {self.make}!"
		return message

car1 = Car("Toyota", "Tacoma", 2012) # car1 object created
car2 = Car("Ford", "Fiesta", 2017) # car2 object created

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.horn())
print()
print(car2.make)
print(car2.model)
print(car2.year)
print(car2.horn())

print("-"*30)

class Robot:
	def __init__(self, name, color, weight):
		self.name = name
		self.color = color
		self.weight = weight
		
	def sayhi(self):
		x = f"Hello, I am the {self.name} robot."
		return x



robot1 = Robot("BB8", "red", 40) # robot1 object created
robot2 = Robot("Plink", "orange", 30) # robot2 object created
robot3 = Robot("JoJo", "blue", 35) # robot3 object created

print(robot1.sayhi())
print("My color is", robot1.color)
print("My weight is", robot1.weight)
print()
print(robot2.sayhi())
print("My color is", robot2.color)
print("My weight is", robot2.weight)
print()
print(robot3.sayhi())
print("My color is", robot3.color)
print("My weight is", robot3.weight)





