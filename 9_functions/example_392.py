# file name: example_392.py

def add_numbers(*args):

    total = 0

    for num in args:

        total += num

    print(total)

add_numbers(1, 2)

add_numbers(1, 2, 3, 4)
