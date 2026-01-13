# file name: example_527.py

class Person:

    def __init__(self, name):

        self.name = name

    def __str__(self):
       return f"Person(name={self.name})"

person = Person("Alice")
print(person)
