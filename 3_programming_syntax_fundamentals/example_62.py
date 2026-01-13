# file name: example_62.py

def parse_int(s):
    try:
        return int(s)
    except ValueError as e:
        raise ValueError(f"Invalid integer: {s}") from e
    finally:
        # runs no matter what
        pass
