# file name: example_170.py

def greet(name=None):

    if name is None:

        print("Hello, Guest!")

    else:

        print(f"Hello, {name}!")

greet()

greet("Alice")
