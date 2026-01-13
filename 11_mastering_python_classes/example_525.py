# file name: example_525.py

class Person:

    def __init__(self,name):

        self.name = name

class Employee(Person):

    def __init__(self, name, employee_id):

        super().__init__(name)   # call parent constructor

        self.employee_id = employee_id

employee = Employee("Alice", 101)

print(employee.name)

print(employee.employee_id)
