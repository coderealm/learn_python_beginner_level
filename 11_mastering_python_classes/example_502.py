# file name: example_502.py


class Person:

    def __init__(self, name):

        self.name = name

    def greet(self):
        
        print(self.name)

person = Person("Alice")

person.greet()
