# file name: example_58.py


nums = [2, 4, 6, 9]

for n in nums:
    if n % 2 == 1:
        print("Found odd:", n)
        break
else:
    print("No odd numbers found")
