# file name: example_530.py

class User:

    def __str__(self):

        return "User object"

    def __repr__(self):

        return "User()"

u = User()

print(str(u)) # Call __str__

print(repr(u)) # Call __repr__

# Not recommended calling directly
# print(u.__str__())
# print(u.__repr__())
