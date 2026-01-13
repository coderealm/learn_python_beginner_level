# file name: example_60.py

command = ("move", 10, 20)

match command:
    case ("move", x, y):
        print("Move to", x, y)
    case ("quit",):
        print("Quit")
    case _:
        print("Unknown command")
