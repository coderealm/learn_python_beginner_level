# file name: example_509.py

class Person:

    def __init__(self, name, age):

        self.__age = age   # private variable

    def get_age(self):
        
        return self.__age

person = Person("Alice", 25)

print(person.get_age())  # Correct access
