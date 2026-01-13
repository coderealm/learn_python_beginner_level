# file name: example_521.py

class Person:

    def __init__(self, name, age):

        self.name = name

        self.age = age

    @staticmethod # static method
    def is_adult(age):
        
        return age >= 18
