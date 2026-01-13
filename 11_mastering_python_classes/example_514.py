# file name: example_514.py

class Person:
    def __init__(self, name, age):

        self.name = name

        self.age = age

    def greet(self):

        print(f"Hello, my name is {self.name}")

person = Person("Alice", 25)

person.greet()
