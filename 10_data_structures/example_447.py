# file name: example_447.py

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

p = Point(3, 4)

result = p.x   # 3

print(result)
