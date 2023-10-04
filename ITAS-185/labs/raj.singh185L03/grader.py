"""
Course: ITAS 185 - Introduction to Programming
Lab 3: Conditional Flow in Python
Description: This program takes a grade and gives it a message
"""

result_remarks = {
    (0, 59): "poor",
    (60, 60): "Squeaked by",
    (61, 99): "Passed",
    (100, 100): "Perfect"
}

while True:
    grade = float(input("Enter a grade please (0 to exit): "))
    if grade == 0:
        break
    for (start, end), remark in result_remarks.items():
        if start <= grade <= end:
            print(f"Your mark of {grade} means the result was {remark}")
            break
    else:
        print(f"Your mark of {grade} means the result was Error")
