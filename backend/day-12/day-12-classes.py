class Student:
    def __init__(self, name, age, is_enrolled, classes, offenses):
        self.name = name
        self.age = age
        self.is_enrolled = is_enrolled
        self.classes = classes
        self.offenses = offenses
        
    # add a new class to the student
    def add_class(self, new_class):
        self.classes.append(new_class)
        
student1 = Student("Juan Dela Cruz", 20, True, [], [])
student1.add_class("Math")
student1.add_class("Science")

print("Student:", student1.name)
print("Age:", student1.age)
print("Enrolled:", student1.is_enrolled)
print("Classes:", student1.classes)
print("Offenses:", student1.offenses)
