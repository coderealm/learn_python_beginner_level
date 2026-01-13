# file name: example_318.py

from decimal import Decimal, ROUND_HALF_UP

value = Decimal("2.675")

result = value.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)

print(result)
