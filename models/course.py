import re

class Course:
    
    def __init__(self, name):
        name = name.strip()
        if not self.is_valid_name(name):
            raise ValueError("Course name can contain only letters, numbers, and spaces.")
        self._name = name

    def get_name(self):
        return self._name

    def is_valid_name(self, name):
        return re.match(r"^[A-Za-z0-9 ]+$", name) is not None

    def __str__(self):
        return self._name