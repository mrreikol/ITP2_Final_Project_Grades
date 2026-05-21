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


def main():
    manager = GradeManager()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose from 1 to 9.")


if __name__ == "__main__":
    main()
