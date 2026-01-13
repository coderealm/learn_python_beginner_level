# file name: example_79.py

count = 0

def increment():

    count = count + 1 

    print(count)  # UnboundLocalError: local variable 'count' referenced before assignment
