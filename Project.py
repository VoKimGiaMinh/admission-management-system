import string
import collections as ct
import sys

# Check valid password
def password_check(password):

    # Check password length
    if len(password) < 10:
        return False

    # Check password upper character
    if not any(char.isupper() for char in password):
        return False
    
    # Check Password number
    number = [char for char in password if char.isdigit()]
    if not(2 <= len(number) <= 3):
        return False

    # Check special char
    special_chars = string.punctuation
    total = sum(v for k, v in ct.Counter(password).items() if k in special_chars)
    if total != 1:
        return False
    return True

#Create class of student
class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school

    def __str__(self):
        return f"Student Name: {self.name}, School: {self.school}"
#Create student
def create_student(number_student):
    students = []
    Engineering = 0
    Business = 0
    Law = 0
    Not_accepted = 0
    
    for i in range(number_student):
        print(f"Enter details for student {i+1}:")
        name = input("Name:")
        math = float(input (f"Input {name} mark in Math on a 100-point scale: "))*4
        science = float(input (f"Input {name} mark in Science on a 100-point scale: "))*5
        language = float(input (f"Input {name} your mark in Language on a 100-point scale: "))*4
        drama = float(input (f"Input {name} your mark in Drama on a 100-point scale: "))*3
        music = float(input (f"Input {name} your mark in Music on a 100-point scale: "))*2
        biology = float(input (f"Input {name} your mark in Biology on a 100-point scale: "))*4
        GPA = float(math + science + language + drama + music + biology)/22
        school = str
        if 90 <= GPA  <= 100:
            school = "School of Engineering"
            Engineering += 1
        elif 80 <= GPA  <= 90:
            school = "School of Business"
            Business += 1
        elif 70 <= GPA  <= 80:
            school = "Law School"
            Law += 1
        elif GPA < 70:
            school = "Not accepted"
            Not_accepted += 1

        student = Student(name, school)
        students.append(student)

    return students, Engineering, Business, Law, Not_accepted

def main():
    # Print Welcome screen
    print("Welcome in Humber College")

    # Promt the user to input username
    username = input("Please input your Username: ")
    
    # Prompt for 3 if the password is not valid
    valid_password = bool
    attempting1 = 0
    while valid_password != True and attempting1 < 3:
            valid_password = password_check(password = input("Please input your Password, the password should have:\nat least 10 characters long\nat least 1 uppercase\n2 or 3 digit\n1 special character\nYour password:"))
            attempting1 += 1

    if  valid_password != True and attempting1 == 3:
        print("Too many attempting!")
        sys.exit()     

    # Prompt the user to input number of student 3 times
    number_student = 0
    attempting2 = 0
    while (number_student < 1 or number_student > 50) and attempting2 < 3:
            number_student = int(input("Please input the number of students between 1-50:"))
            attempting2 += 1

    if  (number_student < 1 or number_student > 50) and attempting2 == 3:
        print("Too many attempting!")
        sys.exit()

    students, Engineering, Business, Law, Not_accepted = create_student(number_student)

    print()
    
    for student in students:
        print(student)

    print()
    print(f"Engineering: {Engineering}")
    print(f"Business: {Business}")
    print(f"Law: {Law}")
    print(f"Not accepted: {Not_accepted}")
    
main()
