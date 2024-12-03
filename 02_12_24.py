## read in the input


def clean_line(line_raw):
    line_str = line_raw[:-1].split(" ")
    line_int = [int(x) for x in line_str]
    return line_int


def check_for_limits_increasing(line):
    safe = False
    for i in range(0, len(line) - 1):
        _dif = line[i + 1] - line[i]
        if (_dif > 0) & (_dif < 4):
            continue
        else:
            return safe
    safe = True
    return safe


def check_for_limits_decreasing(line):
    safe = False
    for i in range(0, len(line) - 1):
        _dif = line[i] - line[i + 1]
        if (_dif > 0) & (_dif < 4):
            continue
        else:
            return safe
    safe = True
    return safe

def is_increasing_in_order(line):
    exceptions = 0
    index_to_pop = 0
    print("WE ARE HERE")
    for i in range(0, len(line) - 1):
        if exceptions > 1:
            return False
        if line[i+1] > line[i]:
            continue
        else:
            index_to_pop = i + 1
            print("WE FOUND THE MOLE")
            exceptions += 1
    if exceptions == 0:
        print("everything is in order, sir")
        return line
    elif exceptions == 1:
        print(exceptions, "how many exceptions")
        return line.pop(index_to_pop)
    
    



def security_dampener_increasing(line):
    dampener_used = 0
    filtered_list = []
    for i in range(0, len(line) - 1):
        if dampener_used > 1:
            return False
        if line[i + 1] > line[i]:
            filtered_list.append(line[i])
        else:
            dampener_used += 1
    return filtered_list


def security_dampener_decreasing(line):
    dampener_used = 0
    filtered_list = []
    for i in range(0, len(line) - 1):
        if dampener_used > 1:
            return False
        if line[i] > line[i + 1]:
            filtered_list.append(line[i])
        else:
            dampener_used += 1
    return filtered_list


def is_safe_without_dampener(line):
    _line_increasing = sorted(line)
    _line_decreasing = sorted(line, reverse=True)
    if line == _line_increasing:
        return check_for_limits_increasing(line)
    elif line == _line_decreasing:
        return check_for_limits_decreasing(line)


def is_safe_with_dampener(line):
    if (security_dampener_increasing(line) is False) & (
        security_dampener_decreasing(line) is False
    ):
        return False
    elif (isinstance(security_dampener_increasing(line), list)) & (
        security_dampener_decreasing(line) is False
    ):
        return check_for_limits_increasing(line)
    elif (security_dampener_increasing(line) is False) & (
        isinstance(security_dampener_decreasing(line), list)
    ):
        return check_for_limits_decreasing(line)
    else:
        print("WTF")


def main():
    with open("02_12_demo_input.txt", "r") as f:
        data = f.readlines()
    print(len(data))
    number_of_safe_rows = 0
    number_of_safe_rows_with_dampener = 0
    for line in data:
        line_clean = clean_line(line)
        if is_safe_without_dampener(line_clean):
            number_of_safe_rows += 1
        print(line)
        if is_safe_with_dampener(line_clean):
            number_of_safe_rows_with_dampener += 1
        print(is_increasing_in_order(line))
    print("we have", number_of_safe_rows, "safe rows without dampener")
    print("we have", number_of_safe_rows_with_dampener, "safe rows with dampener")


if __name__ == "__main__":
    main()
