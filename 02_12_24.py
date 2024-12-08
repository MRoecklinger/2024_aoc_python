def is_safe(numbers):
    is_increasing = numbers[0] < numbers[1]
    if is_increasing:
        for i in range(1, len(numbers)):
            diff = numbers[i] - numbers[i - 1]
            if not 0 < diff < 4:
                return False
        return True
    else:
        for i in range(1, len(numbers)):
            diff = numbers[i] - numbers[i - 1]
            if not -4 < diff < 0:
                return False
        return True


def safety_with_dampener(numbers):
    if is_safe(numbers):
        return True
    for i in range(len(numbers)):
        if is_safe(numbers[:i] + numbers[i + 1 :]):
            return True
    return False


def main_1():
    with open("input_02_12.txt", "r") as f:
        data = f.read().strip().split("\n")
    valid_instr = 0
    for line in data:
        numbers = [int(x) for x in line.split()]
        valid_instr += safety_with_dampener(numbers)
    print("number of valid instr", valid_instr)


if __name__ == "__main__":
    main_1()
