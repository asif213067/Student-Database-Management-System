class StudentDatabase:
    __student_list = []

    @classmethod
    def add_student(cls, student):
        cls.__student_list.append(student)

    @classmethod
    def get_students(cls):
        return cls.__student_list

    @classmethod
    def find_student(cls, student_id):
        for student in cls.__student_list:
            if student.get_id() == student_id:
                return student
        return None

class Student:
    def __init__(self, student_id, name, deparment):
        self.__student_id = student_id
        self.__name = name
        self.__deparment = deparment
        self.__is_enrolled = False

        StudentDatabase.add_student(self)

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_deparment(self):
        return self.__deparment

    def get_enrollment_status(self):
        return self.__is_enrolled

    def enroll_student(self):
        if self.__is_enrolled:
            raise Exception(f"'{self.__name}' is already enrolled!")
        self.__is_enrolled = True
        print(f"'{self.__name}' has been successfully enrolled.")

    def drop_student(self):
        if not self.__is_enrolled:
            raise Exception(f"'{self.__name}' is not currently enrolled!")
        self.__is_enrolled = False
        print(f"'{self.__name}' has been dropped successfully.")

    def view_student_info(self):
        if self.__is_enrolled == True:
            status = "True"
        else:
            status = "False"

        print(f"ID: {self.__student_id}, Name: {self.__name}, Deparment: {self.__deparment}, Enrolled: {status}")


s1 = Student("S101", "Rakib", "Computer Science")
s2 = Student("S102", "Asif",     "Mathematics")
s3 = Student("S103", "Moinul",   "Physics")
s4 = Student("S104", "Sakib",   "Chemistry")
s5 = Student("S105", "Bablu",     "Computer Science")


def view_all_students():
    students = StudentDatabase.get_students()
    if not students:
        print("No students found in the database.")
        return
    print("\nAll Students:")
    for student in students:
        student.view_student_info()

def enroll_student_menu():
    try:
        sid = input("Enter Student ID to enroll: ")
        student = StudentDatabase.find_student(sid)
        if student is None:
            print(f"No student found with ID {sid}.")
        else:
            student.enroll_student()
    except Exception as e:
        print(f"Error: {e}")

def drop_student_menu():
    try:
        sid     = input("Enter Student ID to drop: ")
        student = StudentDatabase.find_student(sid)
        if student is None:
            print(f"No student found with ID {sid}.")
        else:
            student.drop_student()
    except Exception as e:
        print(f"Error: {e}")


def main():
    print("---Student Management Menu---")

    while True:
        print("\n1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            view_all_students()

        elif choice == "2":
            enroll_student_menu()

        elif choice == "3":
            drop_student_menu()

        elif choice == "4":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


main()