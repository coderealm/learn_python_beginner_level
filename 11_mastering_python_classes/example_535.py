# file name: example_535.py

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("This is a shape")
