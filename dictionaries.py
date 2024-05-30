# Demos of Dictionaries in Python
# use curly braces {key:value, key:value}

student_grades = {"Sarah":95, "Tom":90, "Larry":76, "Mary":89}

print(student_grades)

print(student_grades["Tom"])

print(student_grades["Larry"])

student_grades["Joe"] = 84 # adds Joe to the dictionary

print(student_grades)

print(student_grades["Joe"])

del(student_grades["Tom"]) # deletes Tom

print(student_grades)

print(len(student_grades)) # len shows how many entries are in dictionary

for name in student_grades: # prints the keys
    print(name)

for grade in student_grades:  # prints the values
    print(student_grades[grade])



