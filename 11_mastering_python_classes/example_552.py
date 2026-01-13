# file name: example_552.py

class FileLogger:

    def write(self, message):

        print("Writing to file:", message)

class SocketLogger:

    def write(self, message):

        print("Sending over network:", message)

def log(writer):

    writer.write("Hello")

log(FileLogger())

log(SocketLogger())
