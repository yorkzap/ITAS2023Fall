"""
Course: ITAS 185 - Introduction to Programming
Lab06: Importing Classes
Description:
    This program imports the Employee class and creates three Employee objects to hold data:
"""

import Employee as emp

emp1 = emp.Employee()
emp1.emp_name = "Kay Oss"
emp1.emp_id = 47899
emp1.department = "Accounting"
emp1.position = "Vice President"


emp2 = emp.Employee()
emp2.emp_name = "Ben Dover"
emp2.id_number = 39119
emp2.department = "IT"
emp2.position = "Programmer"

emp3 = emp.Employee()
emp3.emp_name = "Al E. Gator"
emp3.id_number = 81774
emp3.department = "Manufacturing"
emp3.position = "Engineer"

print(emp1.get_info())
print(emp2.get_info())
print(emp3.get_info())