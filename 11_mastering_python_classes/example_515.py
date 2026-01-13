# file name: example_515.py

class Person:

    def __init__(self, name, age):

        self.name = name    # instance variable

        self.age = age     # instance variable

    def have_birthday(self):

        self.age += 1   # modifies object state

person = Person("Alice", 25)

# Calling an Instance Method
person.have_birthday() # 

print(person.age)
