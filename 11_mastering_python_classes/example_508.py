# file name: example_508.py

class Person:

    def __init__(self, name, age):

        self._age = age   # protected variable

    def get_age(self):

        return self._age

person = Person("Alice", 25)

# Accessible externally, but discouraged
print(person._age)  
