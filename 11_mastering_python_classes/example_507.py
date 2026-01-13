# file name: example_507.py

class Person:

    def __init__(self, name, age=0):

        self.name = name
        
        self.age = age

person = Person("Bob")

print(person.age)
