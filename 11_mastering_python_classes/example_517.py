# file name: example_517.py

class Person:

    species = "Human"   # class variable

    def __init__(self, name, age):

        self.name = name   # instance variable
        
        self.age = age    # instance variable

person1 = Person("Alice", 25)

person2 = Person("Bob", 30)

print(person1.species)

print(person2.species)
