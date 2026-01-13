# file name: example_524.py

class Person:

    def __init__(self, name):

        self.name = name

    def greet(self):

        print(f"Hello, my name is {self.name}")


class Employee(Person):  # Inherits from Person

    def __init__(self, name, employee_id):

        super().__init__(name)

        self.employee_id = employee_id

    def work(self):

        print("Working...")

    # overrides greet method from Person
    def greet(self):

        print(f"Employee name: {self.name}")

employee = Employee("Bob")

employee.greet()
