from models.student import Student
from models.course import Course
from utils.validators import is_valid_grade, is_not_empty


class GradeManager:

    def __init__(self):
        self.__students = {}
        self.__courses = {}

    def add_student(self, student_id, name):
        if not is_not_empty(str(student_id)) or not is_not_empty(name):
            raise ValueError("Student ID and name cannot be empty.")

        student_id = str(student_id).strip()
        name = name.strip()

        if student_id not in self.__students:
            self.__students[student_id] = Student(student_id, name)

        return self.__students[student_id]

    def add_course(self, course_name):
        course = Course(course_name)
        name = course.get_name()

        if name not in self.__courses:
            self.__courses[name] = course

        return self.__courses[name]

    def student_exists(self, student_id):
        return str(student_id).strip() in self.__students

    def course_exists(self, course_name):
        return course_name.strip() in self.__courses

    def assign_grade_to_existing(self, student_id, course_name, grade):
        student_id = str(student_id).strip()
        course_name = course_name.strip()

        if not self.student_exists(student_id):
            raise ValueError("Student not found. Add the student first.")

        if not self.course_exists(course_name):
            raise ValueError("Course not found. Add the course first.")

        if not is_valid_grade(str(grade)):
            raise ValueError("Grade must be a number from 0 to 100.")

        student = self.__students[student_id]
        course = self.__courses[course_name]

        student.add_grade(course.get_name(), float(grade))

    def assign_grade(self, student_id, name, course_name, grade):
        """Used when importing CSV because CSV contains student name too."""

        if not is_valid_grade(str(grade)):
            raise ValueError("Grade must be a number from 0 to 100.")

        student = self.add_student(student_id, name)
        course = self.add_course(course_name)

        student.add_grade(course.get_name(), float(grade))

    def iter_students(self):
        for student in self.__students.values():
            yield student

    def get_course_names(self):
        course_names = []

        for course in self.__courses.values():
            course_names.append(course.get_name())

        course_names.sort()
        return course_names

    def student_gpa_row(self, student_id):
        student_id = str(student_id).strip()

        if not self.student_exists(student_id):
            raise ValueError("Student not found.")

        student = self.__students[student_id]

        return {
            "student_id": student.get_id(),
            "name": student.get_name(),
            "average_grade": round(student.average_grade(), 2),
            "gpa": round(student.calculate_gpa(), 2)
        }

    def gpa_report_rows(self):
        rows = []

        for student in self.iter_students():
            rows.append({
                "student_id": student.get_id(),
                "name": student.get_name(),
                "average_grade": round(student.average_grade(), 2),
                "gpa": round(student.calculate_gpa(), 2)
            })

        return rows

    def top_students(self, limit=3):
        students = list(self.iter_students())

        students.sort(
            key=lambda student: student.calculate_gpa(),
            reverse=True
        )

        return students[:limit]

    def top_students_rows(self, limit=3):
        rows = []

        for student in self.top_students(limit):
            rows.append({
                "student_id": student.get_id(),
                "name": student.get_name(),
                "gpa": round(student.calculate_gpa(), 2),
                "average_grade": round(student.average_grade(), 2)
            })

        return rows

    def students_above_gpa(self, minimum_gpa):
        return list(
            filter(
                lambda student: student.calculate_gpa() >= minimum_gpa,
                self.iter_students()
            )
        )
