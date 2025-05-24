import string
import collections as ct
import sys
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Check valid password
def password_check(password):    
    is_valid_password = False 

    match True:
        case _ if len(password) < 10:
            return
        case _ if not any(char.isupper() for char in password):
            return
        case _ if not (2 <= len([c for c in password if c.isdigit()]) <= 3):
            return
        case _ if sum(v for k, v in ct.Counter(password).items() if k in string.punctuation) != 1:
            return
        case _:
            is_valid_password = True
    return is_valid_password

#Create class of student
class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school

    def __str__(self):
        return f"Student Name: {self.name}, School: {self.school}"

#Collect score
def score_collect(subject,coefficient,name):
    while True:
        try:
            point = float(input (f"Input {name} mark in {subject} on a 100-point scale: "))
            if 0 <= point <= 100:
                subject = point * coefficient
                return subject
            else:
                print("Please enter a value on 100-point scale")
        except ValueError: #Prevent crashing when user input string
            print("Invalid input. Please enter number")
            

    
    
#Create student
def create_student(number_student):
    students = []
    students_data = []
    Engineering = 0
    Business = 0
    Law = 0
    Not_accepted = 0
    
    for i in range(number_student):
        print(f"Enter details for student {i+1}:")
        name = input("Name:")

        #Collect records
        math = score_collect("Math",4,name)
        science = score_collect("Science",5,name)
        language = score_collect("Language",4,name)
        drama = score_collect("Drama",3,name)
        music = score_collect("Music",2,name)
        biology = score_collect("Biology",4,name)

        #Calculate GPA
        GPA = float(math + science + language + drama + music + biology)/22
        school = str

        students_data.append({
            "Name": name,
            "Math": math / 4,       
            "Science": science / 5,
            "Language": language / 4,
            "Drama": drama / 3,
            "Music": music / 2,
            "Biology": biology / 4,
            })



        # Assign school based on GPA
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


    return students, Engineering, Business, Law, Not_accepted, students_data

def main():
    # Print Welcome screen
    print("Welcome in Humber College")

    # Promt the user to input username
    username = input("Please input your Username: ")
    
    # Prompt for 3 if the password is not valid
    valid_password = False
    attempting1 = 0
    while not valid_password and attempting1 < 3:
            valid_password = password_check(password = input("Please input your Password, the password should have:\n- At least 10 characters long\n- At least 1 uppercase\n- 2 or 3 digit\n- 1 special character\nYour password:"))
            attempting1 += 1

    if not valid_password and attempting1 == 3:
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

    students, Engineering, Business, Law, Not_accepted, students_data = create_student(number_student)

    print()
    
    for student in students:
        print(student)

    print()
    print(f"Engineering: {Engineering}")
    print(f"Business: {Business}")
    print(f"Law: {Law}")
    print(f"Not accepted: {Not_accepted}")

    #Convert list of dictionaries to table
    df = pd.DataFrame(students_data)

    #Reshape to long format for Plotly
    df_long = df.melt(id_vars='Name', var_name='Subject', value_name='Score')

    #Create Canvas
    fig = make_subplots(rows=1,cols=2,subplot_titles=('Compares students scores across subjects',"Distribution of students by school"),specs=[[{'type': 'xy'}, {'type': 'domain'}]]) #xy for bar/line, domain for pie
    
    
    
    for student in df_long['Name'].unique():
        df_student = df_long[df_long['Name'] == student]
        fig.add_trace(
            go.Bar(
                x=df_student['Subject'],
                y=df_student['Score'],
                name=student),
                row=1, col=1)

    #Create school table:
    school_data = {
        'School': ['Engineering', 'Business', 'Law', 'Not accepted'],
        'Count': [Engineering, Business, Law, Not_accepted]
    }

    df_school = pd.DataFrame(school_data)
    
    fig.add_trace(
        go.Pie(
            labels=df_school['School'],
            values=df_school['Count'],
            name="School Assignment"),
        row=1, col=2
    )


    fig.show()

    
main()
