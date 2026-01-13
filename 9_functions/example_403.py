# file name: example_403.py

def show(a, b, c, d):
    
    print(a, b, c, d)

values = (1, 2)

info = {"c": 3, "d": 4}

show(*values, **info)
