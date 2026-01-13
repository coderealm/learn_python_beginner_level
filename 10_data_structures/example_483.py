# file name: example_483.py

data = {"a": 1, "b": 2, "c": 3}

result1 = data.pop("b")

del data["a"]

result2 = data.popitem()

result3 = data.clear()

print(result1)

print(result2)

print(result3)