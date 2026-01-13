# file name: example_91.py

def add(a, b):
    return a + b

print(add(2, 3))     # sum 2, 5 and output 5

print(add("a", "b")) # concatenate a, b and output "ab"

print(add(2, "b"))   # TypeError at runtime
