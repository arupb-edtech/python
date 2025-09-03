import pprint

dict = {}
j = 0
for i in range(15):
    if i % 2 == 0:
        dict[j] = i
        j = j + 1

# Pretty print with a smaller width for better formatting
pprint.pprint(dict, width=1)

students = {
    1: {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
    2: {"name": "Bob", "age": 22, "grades": [88, 76, 92]},
    3: {"name": "Charlie", "age": 19, "grades": [95, 89, 84]},
    4: {"name": "Diana", "age": 21, "grades": [72, 85, 80]},
    5: {"name": "Ethan", "age": 23, "grades": [90, 91, 89]},
}

pprint.pprint(students, width=1)

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def __str__(self):
        return f"Student {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"Student({self.name!r}, {self.age!r}, {self.grades!r})"

# Creating an object
student = Student("Alice", 20, [85, 90, 78])
print(student)        # Output: Student Alice, Age: 20
print(repr(student))  # Output: Student('Alice', 20, [85, 90, 78])