# file name: example_541.py

from dataclasses import dataclass

@dataclass(frozen=True)
class Point:

    x: int

    y: int

point = Point(1, 2)
point.x = 3  # Results in an Error
