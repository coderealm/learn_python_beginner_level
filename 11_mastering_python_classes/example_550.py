# file name: example_550.py

class Person:

    __slots__ = ("name", "age")


    def __init__(self, name, age):

        self.name = name
        
        self.age = age

class Employee(Person):

    __slots__ = ("employee_id",)
