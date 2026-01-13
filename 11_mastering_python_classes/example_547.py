# file name: example_547.py


# Nested class → organizational
class NestedOuter:

    class Inner:

        pass

# Composition → relationship
class CompositionOuter:

    def __init__(self):
        
        self.inner = NestedOuter.Inner()

# The nested class is accessed through the outer class name.


