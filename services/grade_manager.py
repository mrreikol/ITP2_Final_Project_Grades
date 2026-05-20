from models.student import Student
from models.course import Course
from utils.validators import is_not_empty


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

    def iter_students(self):
        for student in self.__students.values():
            yield student

    def get_course_names(self):
        course_names = []

        for course in self.__courses.values():
            course_names.append(course.get_name())

        course_names.sort()
        return course_names
