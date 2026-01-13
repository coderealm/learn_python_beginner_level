# file name: example_513.py
 
class Person:
    def __init__(self, name, age):
        
        self.name = name   # instance variable

        self.age = age    # instance variable

person1 = Person("Alice", 25)

person2 = Person("Bob", 30)

print(person1.age)

print(person2.age)

person1.age = 26

print(person1.age)

print(person2.age)
