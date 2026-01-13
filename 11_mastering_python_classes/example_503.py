# file name: example_503.py

class Person:

    def __init__(self, name, age):

        self.name = name

        self.age = age

    def greet(self):
         
         print(self.name)

person = Person("Alice", 25) # object creation

person.greet() # Python automatically passes self

Person.greet(person) 
