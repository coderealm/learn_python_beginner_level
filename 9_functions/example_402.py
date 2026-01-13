# file name: example_402.py

def greet(name, age):

    print(name, age)

data = {"name": "Bob", "age": 25}

greet(**data)
