# file name: example_80.py

count = 0

def increment():
    global count
    count += 1

increment()

print(count)  # Output: 1
