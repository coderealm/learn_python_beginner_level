# file name: example_529.py

class Number:

    def __init__(self, value):

        self.value = value

    def __add__(self, other):

        return self.value + other.value

n1 = Number(3)

n2 = Number(4)

print(n1 + n2)
