# file name: example_511.py

class Person:

    def __init__(self, age):

        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):

        if value > 0:

            self.__age = value

person = Person("Alice", 25)

print(person.get_age())  # getter

person.set_age(30)       # setter

print(person.get_age())
