# file name: example_549.py

class Person:

    __slots__ = ("name", "age")

    def __init__(self, name, age):

        self.name = name

        self.age = age

person = Person("Alice", 25)
person.city = "NY"   #  AttributeError
