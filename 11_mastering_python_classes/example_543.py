# file name: example_543.py

class Engine:

    def start(self):

        print("Engine started")

class Car:

    def __init__(self):

        self.engine = Engine()   # Car has an Engine

car = Car()

car.engine.start()
