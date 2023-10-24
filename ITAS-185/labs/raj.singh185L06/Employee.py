"""
Course: ITAS 185 - Introduction to Programming
Lab06: Employee Class
Description:
    The Employee class defines attributes and a method for managing employee information.
"""

class Employee:
    emp_name = ""
    id_number = 0
    department = ""
    position = ""

    def get_info(self):
        return f"Name: {self.emp_name}\tID: {self.id_number}\tDepartment: {self.department}\tPosition: {self.position}"
    