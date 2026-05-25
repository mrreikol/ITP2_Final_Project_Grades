# Student Grade Management System

This is our final project for Introduction to Programming 2.
It is a console application written in Python that helps manage students, courses, and grades.

---

## What the program does

- Add students and courses
- Assign grades to students
- Calculate GPA for each student
- Show all students with their ID, name, GPA, and courses
- Generate reports (top students, GPA report)
- Import student data from CSV file
- Save data to JSON file

---

## How to run

1. Clone the repository:
```
git clone https://github.com/mrreikol/ITP2_Final_Project_Grades.git
cd ITP2_Final_Project_Grades
```

2. Run the program:
```
python main.py
```

3. Run the tests:
```
python -m unittest tests/test_project.py
```

---

## Project structure

```
ITP2_Final_Project_Grades/
|
|-- main.py
|-- README.md
|-- .gitignore
|
|-- data/
|   |-- students.csv
|
|-- models/
|   |-- person.py
|   |-- student.py
|   |-- course.py
|
|-- services/
|   |-- grade_manager.py
|
|-- utils/
|   |-- file_handler.py
|   |-- logger.py
|   |-- validators.py
|
|-- tests/
|   |-- test_project.py
|
|-- reports/
```

---

## Input and output format

CSV input (`data/students.csv`):
```
student_id,name,course,grade
1,Aidos,Math,88
1,Aidos,Physics,91
2,Aigerim,Math,95
2,Aigerim,Physics,89
...
```

JSON output (saved to `reports/students_data.json`):
```
{
  "students": [
    {
      "student_id": "1",
      "name": "Aidos",
      "grades": {"Math": 88.0, "Physics": 91.0},
      "average_grade": 89.5,
      "gpa": 3.67
    }
  ],
  "courses": ["Math", "Physics"]
}
```

---

## Data structures we used

**dict** — we used it to store students and courses by ID or name. It is faster than searching through a list.

**dict (for grades)** — inside each Student object, grades are stored as a dictionary where the key is the course name and the value is the grade. Easy to update and look up by course name.

**list** — we used it to collect rows, report data, and sorted student lists. Easy to loop through.

**set** — we used it in `all_student_ids()` to return unique student IDs without duplicates.

---

## OOP

We have a base class `Person` and a child class `Student` that inherits from it.
`Course` is a separate class.

We used:
- inheritance — Student inherits `person_id` and `name` from Person
- encapsulation — attributes are private (`_name`, `__grades`), accessed through methods
- polymorphism — `Student` overrides the `short_info()` method from `Person`

---

## Advanced Python features

- **Generator** — `iter_students()` in `grade_manager.py` uses `yield` to go through students one by one
- **Decorator** — `log_action` in `logger.py` is used to log every file operation automatically
- **Lambda and filter** — used in `top_students()` and `students_above_gpa()` to sort and filter students by GPA

---

## Testing

We wrote unit tests in `tests/test_project.py` using `unittest`.

We tested:
- GPA calculation with real grade values
- invalid grade raises ValueError
- loading rows from CSV data
- filtering students above a minimum GPA
- showing all students with their courses

---

## Team members

**Mustafa** — created `Person`, `Student`, and `Course` classes with inheritance, encapsulation, and polymorphism.

**Islam** — created `GradeManager` with all the main logic: grades, GPA, reports, generator, and lambda/filter.

**Abylkair** — implemented file handling for CSV and JSON, input validation, logging decorator, and wrote unit tests.

**Ismail** — built the main menu, generated sample CSV data, and wrote all documentation.
