# file name: example_81.py

def outer():
    msg = "Outer message"

    def inner():

        print(msg)


    inner() # Outer message"

outer()
