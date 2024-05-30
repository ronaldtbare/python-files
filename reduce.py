class Student:
    def __init__(self, name, score):
        self.name = name
        self.score =  score
    
    def __repr__(self): # https://docs.python.org/3/library/functions.html#repr
        return f"{self.name}: {self.score}"  # This method allows to print out 
                                             # contents of the objects, not
                                             #  just a message about the
                                             #  objects.

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63)]

score_total = 0

for student in students:
    score_total += student.score

print(score_total / len(students))

from functools import reduce # Reduce function must be imorted

# Reduce function just uses all the list items and returns a single value.
#  First argument is lambda function, second argument is the list, 3rd 
# argument is starting value.
reduce_total = reduce(lambda total, student: student.score + total, students, 0)

print("Average is: ", round(reduce_total / len(students), 2)) # round to 2 decimal places

# Challenge
# Use reduce to multiply all numbers in this list

numbers = [1, 2, 3, 4, 5]
big_number = reduce(lambda total, number: number * total, numbers, 1)
print()
print("All these numbers multiplied together is ",big_number)