# file name: example_466.py

a = {1, 2}
b = {1, 2, 3}

print(a <= b)   # True (subset)

print(a.issubset(b))     # True

print(a < b)    # True (proper subset)
