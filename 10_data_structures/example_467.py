# file name: example_467.py

a = {1, 2}

b = {1, 2, 3}

print(b >= a)   # True (superset)

b.issuperset(a)

print(b > a)    # True (proper superset)
