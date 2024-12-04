import re

REGEX_MULTIPLICATION = r"mul\((?P<first>\d{,3}),(?P<second>\d{,3})\)"
REGEX_FIND = r"mul\(\d{,3}\,\d{,3}\)"


def clean_and_multiply(item):
    res = re.match(REGEX_MULTIPLICATION, item)
    mult = int(res.group("first")) * int(res.group("second"))
    return mult


def main_1():
    with open("input_03_12.txt", "r") as f:
        data = f.readline()
    _ = re.findall(REGEX_FIND, data)
    sum_of_mult = 0
    for item in _:
        sum_of_mult += clean_and_multiply(item)
    print("we have a sum of:", sum_of_mult)


def main_2():
    with open("input_03_12.txt", "r") as f:
        data = f.readline()
    data_split = data.split("don't()")
    print("we have following number of split items:", len(data_split))
    # because we start with enabled
    sum_of_activated_mult = 0
    first_part = data_split[0]
    match_in_first_part = re.findall(REGEX_FIND, first_part)
    for item in match_in_first_part:
        sum_of_activated_mult += clean_and_multiply(item)
    for line in data_split[1:]:
        # split for activation
        line_split = line.split("do()")
        # double de-activation
        if len(line_split) == 1:
            print("no double activation")
            continue
        ## we need another loop to include all dos
        # [0] is don't() --> [1:]
        for _do in line_split[1:]:
            match_activated = re.findall(REGEX_FIND, _do)
            for item in match_activated:
                sum_of_activated_mult += clean_and_multiply(item)
    print("we have following sum of activated instructions:", sum_of_activated_mult)


if __name__ == "__main__":
    main_2()
