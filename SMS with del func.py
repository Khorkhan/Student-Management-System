class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        return f"Name: {self.name}, Age: {self.age}, Major: {self.major}"

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_all(self):
        if not self.students:
            print("No students in the system.")
            return

        for student in self.students:
            print(student.introduce())

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student.introduce()
        return "Student not found."

    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return f"Student {name} deleted successfully."
        return "Student not found."

# main program
def main():
    manager = StudentManagementSystem()
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Find Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice(1-5): ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            major = input("Major: ")
            manager.add_student(Student(name, age, major))
            print("Student added successfully.")

        elif choice == "2":
            print("\nAll Student: ")
            manager.show_all()

        elif choice == "3":
            name = input("Enter Student to find:")
            print(manager.find_student(name))

        elif choice == "4":
            name = input("Enter Student to delete: ")
            print(manager.delete_student(name))

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

# run the program
main()