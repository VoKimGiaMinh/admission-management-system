# Admission Management System

## 📘 Description

🎓 Student Admission & Performance Visualization System
This Python-based application simulates a student admission system that evaluates applicants based on their academic performance. It combines user authentication, GPA calculation, school assignment, and           interactive data visualization using Plotly.

## 🔐 Key Features:
- Password Validation: Enforces strong password rules (length, uppercase, digits, special characters).
- Dynamic Student Input: Collects multiple students’ names and subject scores.
- GPA Calculation.
- School Assignment Logic:
    GPA ≥ 90 → School of Engineering
    GPA ≥ 80 → School of Business
    GPA ≥ 70 → Law School
    GPA < 70 → Not Accepted
- Data Visualization with Plotly:
    📊 Bar Chart: Compares students' scores across subjects.
    🥧 Pie Chart: Displays the distribution of students by school.

## 🧰 Technologies Used:
- Python (core logic & calculations)
- Pandas (data manipulation)
- Plotly (interactive graphs)
- Collections & String Modules (validation & counting)

## 🧾 How to use (Step-by-Step):
- Step 1: Input the username

    Example: MinhVo

- Step 2: Enter the password, make sure your password have:
    - At least 10 characters long
    - At least 1 uppercase
    - 2 or 3 digit
    - 1 special character

    Example: @Minhvo123

- Step 3: Enter the number of student (You can have up to 50 students):

    Example: 2 (If you have two students)

- Step 4: Enter the names of the students and their score
- Step 5: See the result!

## 🛠️ Installation

Make sure you have Python installed

```bash
git clone https://github.com/VoKimGiaMinh/admission-management-system.git
pip install -r requirements.txt
