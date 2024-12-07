with open("05_12_demo_input.txt", "r") as f:
    data = f.readlines()

def split_input_file(data):
    page_ordering_rules = []
    pages_to_produce = []

    for item in data:
        if "|" in item:
            page_ordering_rules.append(item.split("\n")[0])
        elif "," in item:
            pages_to_produce.append(item.split("\n")[0])
        else:
            continue
    return page_ordering_rules, pages_to_produce

def individual_pages_and_rules_tuples(ordering_rules):
    individual_pages = []
    rules_tuples = []
    for item in ordering_rules:
        _ = item.split("|")
        rules_tuples.append((int(_[0]), int(_[1])))
        if int(_[0]) in individual_pages:
            continue
        else:
            individual_pages.append(int(_[0]))
        if int(_[1]) in individual_pages:
            continue
        else:
            individual_pages.append(int(_[1]))
    return individual_pages, rules_tuples

# find first and last
def sorting_algo(individual_pages, rules_tuples):
    initial_pages = individual_pages
    from_left = []
    # reverse order at the end
    from_right = []
    while len(individual_pages) > 2:
        left_instructions = []
        right_instructions = []
        _highest = 0
        _lowest = 0
        #print("starting tuples", rules_tuples)
        for item in rules_tuples:
            left, right = item
            left_instructions.append(left)
            right_instructions.append(right)
        # clean instructs
        left_instructions = set(left_instructions)
        right_instructions = set(right_instructions)
        print("left instructs", left_instructions)
        print("right instructs", right_instructions)
        print("do we have a problem now?", left_instructions == right_instructions)
        print(individual_pages)
        print(len(individual_pages), len(left_instructions), len(right_instructions))
        for numb in individual_pages:
            if (numb in left_instructions) & (numb not in right_instructions):
                _highest = numb
            if (numb not in left_instructions) & (numb in right_instructions):
                _lowest = numb
        # add to ordered list
        from_left.append(_highest)
        from_right.append(_lowest)
        # remove from individual pages
        print("this is highest:", _highest)
        print("this is lowest: ", _lowest)
        individual_pages.remove(_highest)
        individual_pages.remove(_lowest)
        # clean tuple
        to_be_removed = []
        for tup in rules_tuples:
            if (_highest in tup) or (_lowest in tup):
                to_be_removed.append(tup)
            else:
                continue
        for item in to_be_removed:
            rules_tuples.remove(item)
        print("###################################")
    print(from_right)
    print(from_left)
    ## putting it together
    res = []
    for item in from_left:
        res.append(item)
    res.append(initial_pages[0])
    for i in range(len(from_right) - 1, -1, -1):
        res.append(from_right[i])
    return res

def is_update_in_order(page_ordering_rules, single_update):
    update_clean = [int(x) for x in single_update.split(",")]
    # filter rule based on update instruction numbers
    _filtered_rule = [x for x in page_ordering_rules if x in update_clean]
    if update_clean == _filtered_rule:
        return update_clean[int(len(update_clean)/2)]
    else:
        return False
    
        

def main():
    with open("input_05_12.txt", "r") as f:
        data = f.readlines()
    ordering_rules, print_instructions = split_input_file(data)
    individual_pages, rules_tuples = individual_pages_and_rules_tuples(ordering_rules)
    print("individual pages:", len(individual_pages))
    print("rules_tuples:", len(rules_tuples))
    print(individual_pages)
    left_instr = []
    right_instr = []
    for tup in rules_tuples:
        left, right = tup
        left_instr.append(left)
        right_instr.append(right)
    print(len(set(left_instr)))
    for page in individual_pages:
        for tup in rules_tuples:
            if page in tup:
                print(page, tup)
    print(len(set(right_instr)))
    """page_ordering_rules = sorting_algo(individual_pages, rules_tuples)
    sum_of_middle_instructions = 0
    for item in print_instructions:
        is_valid = is_update_in_order(page_ordering_rules, item)
        if not is_valid:
            continue
        else:
            sum_of_middle_instructions += is_valid

    print("this is the result:", sum_of_middle_instructions) 
    """


if __name__ == "__main__":
    main()