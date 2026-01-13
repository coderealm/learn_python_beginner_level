# file name: example_546.py

class Car:

    class Engine:

        def start(self):

            print("Engine started")

    def __init__(self):

        self.engine = Car.Engine()

car = Car()

car.engine.start()
