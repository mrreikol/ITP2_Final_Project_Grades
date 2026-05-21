from services.grade_manager import GradeManager
from utils.file_handler import read_csv_rows, write_csv, write_json

DATA_FILE = "data/grades.csv"
GPA_REPORT_FILE = "reports/gpa_report.csv"
TOP_REPORT_FILE = "reports/top_students.json"
DATA_JSON_FILE = "reports/students_data.json"


def print_menu():
    print("\n--- Student Grade Management System ---")
    print("1. Add student")
    print("2. Add course")
    print("3. Assign grade")
    print("4. Calculate GPA")
    print("5. Generate reports")
    print("6. Import data from CSV")
    print("7. Save data to JSON")
    print("8. Show all students")
    print("9. Exit")

def add_student_menu(manager):
    try:
        student_id = input("Student ID: ")
        name = input("Student name: ")
        manager.add_student(student_id, name)
        print("Student added successfully.")
    except ValueError as error:
        print("Error:", error)

def add_course_menu(manager):
    try:
        course_name = input("Course name: ")
        manager.add_course(course_name)
        print("Course added successfully.")
    except ValueError as error:
        print("Error:", error)

def assign_grade_menu(manager):
    try:
        student_id = input("Student ID: ")
        course_name = input("Course name: ")
        grade = input("Grade 0-100: ")
        manager.assign_grade_to_existing(student_id, course_name, grade)
        print("Grade assigned successfully.")
    except ValueError as error:
        print("Error:", error)

def main():
    manager = GradeManager()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_student_menu(manager)
        elif choice == "2":
            add_course_menu(manager)
        elif choice == "3":
            assign_grade_menu(manager)
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose from 1 to 9.")

if __name__ == "__main__":
    main()
