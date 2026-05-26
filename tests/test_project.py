import unittest
import sys
import os
 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
from services.grade_manager import GradeManager
from models.student import Student
 
class TestStudentGrades(unittest.TestCase):
 
    def test_gpa_calculation(self):
        student = Student("1", "John")
        student.add_grade("Math", 90)
        student.add_grade("Physics", 80)
        self.assertEqual(round(student.calculate_gpa(), 2), 3.33)
 
    def test_invalid_grade(self):
        student = Student("1", "John")
        with self.assertRaises(ValueError):
            student.add_grade("Math", 120)
 
    def test_duplicate_student_id(self):
        manager = GradeManager()
        manager.add_student("1", "John")
        with self.assertRaises(ValueError):
            manager.add_student("1", "Another Person")
 
    def test_negative_student_id(self):
        manager = GradeManager()
        with self.assertRaises(ValueError):
            manager.add_student("-1", "John")
 
    def test_manager_load_rows(self):
        rows = [
            {"student_id": "1", "name": "John", "course": "Math", "grade": "85"},
            {"student_id": "1", "name": "John", "course": "Physics", "grade": "90"},
            {"student_id": "2", "name": "Alice", "course": "Math", "grade": "95"}
        ]
        manager = GradeManager()
        errors = manager.load_from_rows(rows)
        self.assertEqual(len(errors), 0)
        self.assertEqual(len(manager.gpa_report_rows()), 2)
 
    def test_students_above_gpa(self):
        manager = GradeManager()
        manager.assign_grade("1", "John", "Math", 50)
        manager.assign_grade("2", "Alice", "Math", 95)
        result = manager.students_above_gpa(3.5)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_name(), "Alice")
 
    def test_all_students_with_courses(self):
        manager = GradeManager()
        manager.assign_grade("1", "John", "Math", 85)
        manager.assign_grade("1", "John", "Physics", 90)
        rows = manager.all_students_with_courses_rows()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["student_id"], "1")
        self.assertEqual(rows[0]["name"], "John")
        self.assertEqual(rows[0]["courses"], "Math, Physics")
 
if __name__ == "__main__":
    unittest.main()
