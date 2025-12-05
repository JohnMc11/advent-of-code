import re


pattern = r"""(\d+)-(\d+),?"""
regex = re.compile(pattern, re.VERBOSE)

file = open('input')
try:
    product_ids = file.read()
finally:
    file.close()

ranges = regex.findall(product_ids)

pattern = r"""^(0\d*)?$|^(.+?)\2{1}$"""
regex = re.compile(pattern, re.VERBOSE)

total: int = 0
for r in ranges:
    low, high = map(int, r)
    for i in range(low, high + 1):
        matches = regex.findall(str(i))
        if len(matches) > 0:
            print(i)
            total += i

print("Total", total)