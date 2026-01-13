# file name: example_426.py

names = [" Alice ", "", "Bob", "  "]

clean = [n.strip() for n in names if n.strip()]

print(clean)
