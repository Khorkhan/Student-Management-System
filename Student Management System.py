class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        return f"Name: {self.name}, Age: {self.age}, Major: {self.major}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_all(self):
        for student in self.students:
            print(student.introduce())

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student.introduce()
        return "Student not found"

# use test
manager = StudentManager()

# add student
manager.add_student(Student("Khan", 28, "Computer Science"))
manager.add_student(Student("Gun", 25, "Mathematics"))

# show all student
manager.show_all()

#find student
print("\nfind student: ")
print(manager.find_student("Khan"))
print(manager.find_student("Eiei"))