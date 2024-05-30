class Student:
    def __init__(self, name, score):
        self.name = name
        self.score =  score
    
    def __repr__(self): # https://docs.python.org/3/library/functions.html#repr
        return f"{self.name}: {self.score}"  # This method allows to print out contents of the objects, not just a message about the objects.

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63)]

# Using if statement
failing_students = []
for student in students:
    if student.score < 0.7:
        failing_students.append(student)
print()
print("**** Using if statement ****")        
print(failing_students)

# Using a filter
filter_list =  list(filter(lambda student: student.score < .7, students))
print()
print("**** Using filter ****")   
print(filter_list)

# Challenge
# Use filter to show only even numbers

numbers = [1, 2, 3, 4, 5]
filter_numbers = list(filter(lambda number: number % 2 == 0 ,numbers))
print()
print("**** Challenge ****")
print(filter_numbers)







