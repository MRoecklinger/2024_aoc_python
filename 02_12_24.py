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
        if line[i + 1] > line[i]:
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
    else:
        return False
    
def increasing_with_damper(line):
    _index_of_anomalies = []
    for i in range(0, len(line) - 1):
        print(line[i+1], line[i])
        if line[i+1] > line[i]:
            continue
        else:
            print("ARE YOU EVEN APPENDING", i)
            _index_of_anomalies.append(i)
    print("this is list of anomalies:", _index_of_anomalies, len(_index_of_anomalies))
    if len(_index_of_anomalies) == 1:
        line.pop(_index_of_anomalies[0])
        return line
    else:
        return False
    
def decreasing_with_damper(line):
    _index_of_anomalies = []
    for i in range(0, len(line) -1):
        if line[i] > line[i+1]:
            continue
        else:
            _index_of_anomalies.append(i+1)
    if len(_index_of_anomalies) == 1:
        line.pop(_index_of_anomalies[0])
        return line
    else:
        return False
    
def is_increasing(line):
    """compares first and last item to check if it is increasing"""
    if line[0] > line[-1]:
        return False
    elif line[0] < line[-1]:
        return True
    else:
        print("THEY ARE THE SAME PICTURE, ANOMALY DETECTED")

    


def main_1():
    with open("input_02_12.txt", "r") as f:
        data = f.readlines()
    print(len(data))
    number_of_safe_rows = 0
    for line in data:
        line_clean = clean_line(line)
        if is_safe_without_dampener(line_clean):
            number_of_safe_rows += 1
    print("we have", number_of_safe_rows, "safe rows without dampener")


## meta algo
# go through line by line
# check if it matches increasing or decreasing sorted list
## 
def main_2():
    with open("02_12_demo_input.txt", "r") as f:
        data = f.readlines()
    number_of_safe_rows = 0
    for line in data:
        line_cleaned = clean_line(line)
        print(line_cleaned)
        if is_safe_without_dampener(line_cleaned):
            number_of_safe_rows += 1
        elif not decreasing_with_damper(line_cleaned):
            line_popped = increasing_with_damper(line_cleaned)
            print("this is line_popped", line_popped)
            if line_popped == sorted(line_popped):
                number_of_safe_rows += 1
            else:
                continue
        elif not increasing_with_damper(line_cleaned):
            line_popped = decreasing_with_damper(line_cleaned)
            if line_popped == sorted(line_popped, reverse=True):
                number_of_safe_rows += 1
            else:
                continue
        else:
            print("SOMETHIN SLIPPED THROUGH")

    print("we have following number of accepted rows:", number_of_safe_rows)
    


def main_3():
    with open("input_02_12.txt", "r") as f:
        data = f.readlines()
    number_of_safe_rows = 0
    for line in data:
        line_cleaned = clean_line(line)
        if is_increasing(line_cleaned):
            print(line_cleaned, increasing_with_damper(line_cleaned))
            ### can be already fine instruction
            if (line_cleaned == sorted(line_cleaned)) & check_for_limits_increasing(line_cleaned):
                number_of_safe_rows += 1
            elif (line_cleaned == sorted(line_cleaned)) and not check_for_limits_increasing(line_cleaned):
                continue
            elif not increasing_with_damper(line_cleaned):
                print("not going in here?")
                continue
            else:
                reduced_line = increasing_with_damper(line_cleaned)
                print("THIS IS THE LINE" ,reduced_line)
                if check_for_limits_increasing(reduced_line):
                    number_of_safe_rows += 1
                else:
                    continue
        if not is_increasing(line_cleaned):
            print(line_cleaned, decreasing_with_damper(line_cleaned))
            if (line_cleaned == sorted(line_cleaned, reverse=True)) & check_for_limits_decreasing(line_cleaned):
                number_of_safe_rows += 1
            elif (line_cleaned == sorted(line_cleaned, reverse=True)) and not check_for_limits_decreasing(line_cleaned):
                continue
            elif not decreasing_with_damper(line_cleaned):
                continue
            else:
                reduced_line = decreasing_with_damper(line_cleaned)
                if check_for_limits_decreasing(reduced_line):
                    number_of_safe_rows += 1
                else:
                    continue
    print("we have following number of safe rows:", number_of_safe_rows)
                


if __name__ == "__main__":
    main_3()
