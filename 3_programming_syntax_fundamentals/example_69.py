# file name: example_69.py

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner
