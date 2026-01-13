# file name: example_538.py

from dataclasses import dataclass

@dataclass
class Person:

    name: str

    age: int = 0

person = Person("Bob")

print(person)
