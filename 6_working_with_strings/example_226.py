# file name: example_226.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Bob", 30)

print(f"{person.name} is {person.age} years old.")
