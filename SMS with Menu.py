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
        if not self.students:
            print("No student in System")
        else:
            for student in self.students:
                print(student.introduce())

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student.introduce()
        return "Student not found"

# Main Program
def main():
    manager = StudentManager()

    while True:
        print("\n---Student Management System---")
        print("1. Add Student")
        print("2. Show All Student")
        print("3. Find Student")
        print("4. Exit")

        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age:"))
            major = input("Major:")
            manager.add_student(Student(name, age, major))
            print("Student added successfully")

        elif choice == "2":
            print("\nAll Student: ")
            manager.show_all()

        elif choice == "3":
            name = input("Enter student name to find: ")
            print(manager.find_student(name))

        elif choice == "4":
            print("Exit System")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the Program
main()