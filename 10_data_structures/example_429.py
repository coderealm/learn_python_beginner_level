# file name: example_429.py

nested = [[1, 2], [3, 4], [5]]

flat = [x for sub in nested for x in sub]

print(flat)
