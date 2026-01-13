# file name: example_82.py

def outer():
    x = 10

    def inner():

        x = 20  # Creates a new local variable
        
    inner()

    print(x)  # Output: 10
