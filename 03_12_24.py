import re

REGEX_MULTIPLICATION = r"mul\((?P<first>\d{,3}),(?P<second>\d{,3})\)"

with open("input_03_12.txt", "r") as f:
    data = f.readline()


def clean_and_multiply(item):
    res = re.match(REGEX_MULTIPLICATION, item)
    mult = int(res.group("first")) * int(res.group("second"))
    return mult


_ = re.findall(r"mul\(\d{,3}\,\d{,3}\)", data)
print(_)
sum_of_mult = 0
for item in _:
    sum_of_mult += clean_and_multiply(item)

print("we have a sum of:", sum_of_mult)
