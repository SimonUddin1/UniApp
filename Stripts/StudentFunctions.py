import re
import random



def check_registration_email_suffix(email):
    return bool(re.match(r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$', email))



def validate_password_complexity(password):
    return bool(re.match(r'^[A-Z][a-zA-Z]{4,}[0-9]{3,}$', password))



def create_student_id():
    student_id = random.randint(1, 999999)
    return str(student_id).zfill(6)



def generate_course_id():
    course_id = random.randint(1, 999)
    return str(course_id).zfill(3)



def assign_random_mark():
    mark = random.randint(25, 100)
    return str(mark)



def calculate_grade(mark):
    if mark >= 85 and mark <= 100:
        return "HD"
    elif mark >= 75 and mark <= 84:
        return " D"
    elif mark >= 65 and mark <= 74:
        return " C"
    elif mark >= 50 and mark <= 64:
        return " P"
    elif mark >= 0 and mark <= 49:
        return " Z"
    else:
        return "Invalid Mark"




