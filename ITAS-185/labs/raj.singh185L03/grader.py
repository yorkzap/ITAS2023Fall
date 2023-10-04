"""
Course: ITAS 185 - Introduction to Programming
Lab 3: Working with numbers and modules
Description: This program takes a grade and checks it
"""

while True:
    grade = float(input("Enter a grade please: "))
    if grade == 0:
        break
    elif grade < 60 and grade > 0:
        print(f"Your mark of {grade} means the result was poor")
    elif grade == 100:
        print(f"Your mark of {grade} means the result was Perfect")
    elif grade > 60 and grade < 100:
        print(f"Your mark of {grade} means the result was Passed")
    elif grade == 60:
        print(f"Your mark of {grade} means the result was Squeaked by")
    else:
        print(f"Your mark of {grade} means the result was Error")

