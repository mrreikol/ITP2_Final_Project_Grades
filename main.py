from services.grade_manager import GradeManager
from utils.file_handler import read_csv_rows, write_csv, write_json

DATA_FILE = "data/students.csv"
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

def calculate_gpa_menu(manager):
    student_id = input("Enter student ID, or press Enter to show all students: ")

    if student_id.strip() == "":
        rows = manager.gpa_report_rows()
        if len(rows) == 0:
            print("No students found.")
            return

        print("\nGPA per student")
        for row in rows:
            print(row["student_id"], row["name"], "Average:", row["average_grade"], "GPA:", row["gpa"])
    else:
        try:
            row = manager.student_gpa_row(student_id)
            print("\nStudent:", row["name"])
            print("Average grade:", row["average_grade"])
            print("GPA:", row["gpa"])
        except ValueError as error:
            print("Error:", error)

def generate_reports(manager):
    gpa_rows = manager.gpa_report_rows()
    top_rows = manager.top_students_rows(3)

    if len(gpa_rows) == 0:
        print("No data. Add students and grades first.")
        return

    write_csv(GPA_REPORT_FILE, ["student_id", "name", "average_grade", "gpa"], gpa_rows)
    write_json(TOP_REPORT_FILE, top_rows)

    print("\nReports generated successfully.")
    print("GPA report:", GPA_REPORT_FILE)
    print("Top students report:", TOP_REPORT_FILE)

    print("\nTop-performing students")
    for row in top_rows:
        print(row["student_id"], row["name"], "GPA:", row["gpa"])

def import_csv_menu(manager):
    file_path = input("CSV file path, or press Enter for data/grades.csv: ")
    if file_path.strip() == "":
        file_path = DATA_FILE

    rows = read_csv_rows(file_path)
    errors = manager.load_from_rows(rows)

    print("Loaded rows:", len(rows))
    if len(errors) > 0:
        print("Some rows had errors:")
        for error in errors:
            print("-", error)
    else:
        print("CSV imported successfully.")

def save_data_to_json(manager):
    data = manager.to_json_data()
    write_json(DATA_JSON_FILE, data)
    print("Data saved to", DATA_JSON_FILE)

def show_all_students_menu(manager):
    rows = manager.all_students_with_courses_rows()

    if len(rows) == 0:
        print("No students found.")
        return

    print("\n--- All Students ---")
    print("ID | Name | GPA | Courses")
    print("-" * 45)

    for row in rows:
        print(row["student_id"], "|", row["name"], "|", row["gpa"], "|", row["courses"])

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
        elif choice == "4":
            calculate_gpa_menu(manager)
        elif choice == "5":
            generate_reports(manager)
        elif choice == "6":
            import_csv_menu(manager)
        elif choice == "7":
            save_data_to_json(manager)
        elif choice == "8":
            show_all_students_menu(manager)
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose from 1 to 9.")

if __name__ == "__main__":
    main()
