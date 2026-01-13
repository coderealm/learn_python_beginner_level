# file name: example_523.py

class Person:

    def __init__(self, name):

        self.name = name

    def greet(self):

        print(f"Hello, my name is {self.name}")


class Employee(Person):   # Inherits from Person

    def __init__(self, name, employee_id):

        super().__init__(name)

        self.employee_id = employee_id

    def work(self):

        print("Working...")


employee = Employee("Alice", 101)

employee.greet()

employee.work()
