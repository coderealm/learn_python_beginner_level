# file name: example_540.py

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    def greet(self):
        print(f"Hi, I'm {self.name}")
