class Student:
    def __init__(self, name, score):
        self.name = name
        self.score =  score

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63)]

student_results = []

for student in students:
    # if student.score >= 0.7:
    #     student_results.append(f"{student.name} Passed")
    # else:
    #     student_results.append(f"{student.name} Failed")
    
    # The following code does the same as above just on one line
    student_results.append(f"{student.name} Passed") if student.score >= 0.7 else student_results.append(f"{student.name} Failed")
    
print(student_results)


# This map function does the exact same as the above code.  Lambda is a special mini function inside the statement. The second argument, students, is what the map statement cycles through.
map_results = list(map(lambda student: f"{student.name} Passed" if student.score >= 0.7 else f"{student.name} Failed", students))
print()
print("**** Using map ****")
print(map_results)

# Challenge:  return a list of all these numbers multiplied by 2 using map.

numbers = [1, 2, 3, 4, 5]

map_numbers = list(map(lambda number: number * 2, numbers))
print()
print("**** Challenge ****")
print(map_numbers)