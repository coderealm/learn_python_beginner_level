# file name: example_8.py

with open("numbers.txt", "w") as f:
    print(1, 2, 3, sep=", ", file=f)
