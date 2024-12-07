import itertools


def clean_data(data):
    _remove_linebreak = [x[:-1] for x in data]
    calibrations = {}
    for item in _remove_linebreak:
        _split_for_column = item.split(":")
        _key = int(_split_for_column[0])
        _numbers = [int(x) for x in _split_for_column[1].split(" ") if x != ""]
        calibrations[_key] = _numbers
    return calibrations


def check_calculations(numbers):
    _possible_res = []
    all_combs = itertools.product("tp", repeat=int(len(numbers)) - 1)
    for item in all_combs:
        _tmp_res = []
        for i in range(0, len(item)):
            _tmp_res.append(numbers[i])
            _tmp_res.append(item[i])
        _tmp_res.append(numbers[-1])
        _possible_res.append(_tmp_res)
    return _possible_res


def check_calculations_extended(numbers):
    _all_permutations = []
    all_combs = itertools.product("tp|", repeat=int(len(numbers)) - 1)
    for item in all_combs:
        _tmp_res = []
        for i in range(0, len(item)):
            _tmp_res.append(numbers[i])
            _tmp_res.append(item[i])
        _tmp_res.append(numbers[-1])
        _all_permutations.append(_tmp_res)
    return _all_permutations


def main_1():
    with open("07_12_demo_input.txt", "r") as f:
        data = f.readlines()

    cleaned_data = clean_data(data)
    extended_data = {}
    sum_of_valid_keys = 0
    for key in cleaned_data.keys():
        extended_data[key] = check_calculations(cleaned_data[key])
    res = {}
    for key in extended_data.keys():
        _results = []
        for inst in extended_data[key]:
            _tmp = 0
            if inst[1] == "p":
                _tmp = inst[0] + inst[2]
            elif inst[1] == "t":
                _tmp = inst[0] * inst[2]
            else:
                print("WTF ARE YOU", inst[1])
            for i in range(3, len(inst), 2):
                if inst[i] == "p":
                    _tmp += inst[i + 1]
                elif inst[i] == "t":
                    _tmp *= inst[i + 1]
                else:
                    print("WHAT ARE YOU!!")
            _results.append(_tmp)
        res[key] = _results
    sum_of_valid_keys = 0
    for key in res.keys():
        if key in res[key]:
            sum_of_valid_keys += key
    print(sum_of_valid_keys)


def main_2():
    with open("07_12_demo_input.txt", "r") as f:
        data = f.readlines()
    cleaned_data = clean_data(data)
    extended_data = {}
    for key in cleaned_data:
        extended_data[key] = check_calculations_extended(cleaned_data[key])
    res = {}
    for key in extended_data.keys():
        _results = []
        for inst in extended_data[key]:
            _tmp = 0
            if inst[1] == "|":
                _tmp = int(str(inst[0]) + str(inst[2]))
            elif inst[1] == "p":
                _tmp = inst[0] + inst[2]
            elif inst[1] == "t":
                _tmp = inst[0] * inst[2]
            else:
                print("WTF ARE YOU", inst[1])
            for i in range(3, len(inst), 2):
                if inst[i] == "|":
                    _tmp = int(str(_tmp) + str(inst[i + 1]))
                elif inst[i] == "p":
                    _tmp += inst[i + 1]
                elif inst[i] == "t":
                    _tmp *= inst[i + 1]
                else:
                    print("WHAT ARE YOU!!")
            _results.append(_tmp)
        res[key] = _results
    sum_of_valid_keys = 0
    for key in res.keys():
        if key in res[key]:
            sum_of_valid_keys += key
    print(sum_of_valid_keys)
    return


if __name__ == "__main__":
    main_1()
