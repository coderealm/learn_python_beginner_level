# file name: example_534.py

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

# The abstract method is not implemented on Cat
# even though Cat inherits Animal
# This results in TypeError
class Cat(Animal):
    pass

cat = Cat()   # TypeError

print(cat.speak())
