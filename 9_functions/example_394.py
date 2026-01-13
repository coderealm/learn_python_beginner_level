# file name: example_394.py

def show_info(*args, **kwargs):

    print("Positional arguments:", args)
    
    print("Keyword arguments:", kwargs)

show_info(1, 2, 3, name="Bob", age=30)
