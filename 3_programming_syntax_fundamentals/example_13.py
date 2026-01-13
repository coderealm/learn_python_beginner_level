# file name: example_13.py

import sys

file = open("output.txt", "w")

print("Hello", "World", sep="-", end="!", file=file, flush=True)
