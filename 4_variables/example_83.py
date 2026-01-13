# file name: example_83.py

def outer():

    x = 10

    def inner():

        nonlocal x

        x = 20
        
    inner()

    print(x)  # Output: 20
