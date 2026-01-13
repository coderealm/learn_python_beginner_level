# file name: example_512.py

class Person:

    def __init__(self, name, age):

        self.name = name   # instance variable

        self.age = age    # instance variable

person1 = Person("Alice", 25)

person2 = Person("Bob", 30)

print(person1.name, person1.age)

print(person2.name, person2.age)
