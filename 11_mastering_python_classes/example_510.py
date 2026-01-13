# file name: example_510.py

class Person:

    def __init__(self, age):

        self.__age = age   # private variable

    def get_age(self):

        return self.__age

    def set_age(self, age):

        if age > 0:

            self.__age = age

person = Person("Alice", 25)

print(person.get_age())  # getter

person.set_age(30)       # setter

print(person.get_age())
