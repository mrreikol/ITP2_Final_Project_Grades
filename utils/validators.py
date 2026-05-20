def is_valid_grade(value):
    try:
        grade = float(value)
        return grade >= 0 and grade <= 100
    except ValueError:
        return False


def is_not_empty(value):
    return value.strip() != ""