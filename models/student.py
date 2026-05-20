from models.person import Person

class Student(Person):

    def __init__(self, student_id, name):
        super().__init__(student_id, name)
        self.__grades = {}
        
    def add_grade(self, course_name, grade):
        grade = float(grade)
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        self.__grades[course_name] = grade

    def get_grades(self):
        return self.__grades.copy()

    def get_course_names(self):
        course_names = list(self.__grades.keys())
        course_names.sort()
        return course_names

    def average_grade(self):
        if len(self.__grades) == 0:
            return 0
        total = 0
        for grade in self.__grades.values():
            total = total + grade
        return total / len(self.__grades)

    def grade_to_points(self, grade):
        if grade >= 95:
            return 4.0
        elif grade >= 90:
            return 3.67
        elif grade >= 85:
            return 3.33
        elif grade >= 80:
            return 3.0
        elif grade >= 75:
            return 2.67
        elif grade >= 70:
            return 2.33
        elif grade >= 65:
            return 2.0
        elif grade >= 60:
            return 1.67
        elif grade >= 55:
            return 1.33
        elif grade >= 50:
            return 1.0
        else:
            return 0.0

    def calculate_gpa(self):
        if len(self.__grades) == 0:
            return 0
        total_points = 0
        for grade in self.__grades.values():
            total_points = total_points + self.grade_to_points(grade)
        return total_points / len(self.__grades)

    def short_info(self):
        return "Student " + self.get_id() + " - " + self.get_name()