# file name: example_319.py

def calculate_price(value):

    tax = value * 0.07

    total = value + tax
    
    return round(total, 2)

result = calculate_price(10)

print(result)
