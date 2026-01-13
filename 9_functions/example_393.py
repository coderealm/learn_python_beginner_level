# file name: example_393.py

def print_details(**kwargs):

    for key, value in kwargs.items():

        print(key, ":", value)

print_details(name="Alice", age=25, city="Paris")
