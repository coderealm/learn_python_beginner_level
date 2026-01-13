# file name: example_499.py

d = {"a": 1, "b": 2}

print(d.get("a"))            # retrieves value for "a"

print(d.setdefault("c", 3))  # adds "c" if missing and returns its value

print(d.copy())              # returns a shallow copy of the dictionary
