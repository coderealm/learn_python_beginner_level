# file name: example_520.py

class Person:

    species = "Human"   # class variable

    def __init__(self, name):

        self.name = name

    @classmethod
    def get_species(cls):

        return cls.species
    
print(Person.get_species())
