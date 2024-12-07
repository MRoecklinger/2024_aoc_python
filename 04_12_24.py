def clean_data(data):
    res = []
    for item in data:
        res.append(item.split("\n")[0])
    return res

def print_matrix(data):
    for item in data:
        print(item)
    
    return


def create_horizontal_str(data):
    horizontal_str = []
    # assuming all have equal length
    # maybe put a consistency check here
    for i in range(0, len(data[0])):
        array_per_column = []
        for item in data:
            array_per_column.append(item[i])
        # print(array_per_column)
        column_st = ""
        column_str = column_st.join(array_per_column)
        horizontal_str.append(column_str)
    return horizontal_str


def create_diagonal_str_decreasing(data):
    diagonal_decreasing_str = []
    for i in range(len(data[0]) -1, -1, -1):
        #print(data[i])
        array_per_diagonal = []
        for j in range(len(data) -1, -1, -1):
            array_per_diagonal.append(data[i][j])
            #print(data[i][j])
        diag_st = ""
        diag_str = diag_st.join(array_per_diagonal)
        diagonal_decreasing_str.append(diag_str)

    return diagonal_decreasing_str


def create_diagonal_str_increasing(data):
    diagonal_increasing_str = []
    for i in range(0, len(data[0])):
        array_per_diagonal =[]
        for j in range(0, len(data)):
            array_per_diagonal.append(data[i][j])

        diag_st = ""
        diag_str = diag_st.join(array_per_diagonal)
        diagonal_increasing_str.append(diag_str)
    return diagonal_increasing_str



def main():
    with open("04_12_demo_input.txt", "r") as f:
        data = f.readlines()

    data_clean = clean_data(data)
    for item in data_clean:
        print(item)
    print("--------")
    for item in create_diagonal_str_decreasing(data_clean):
        print(item)
    # create one list
    """
    list_of_all_str = []
    for item in data_clean:
        list_of_all_str.append(item)
    for item in create_horizontal_str(data_clean):
        list_of_all_str.append(item)
    for item in create_diagonal_str_decreasing(data_clean):
        list_of_all_str.append(item)
    for item in create_diagonal_str_increasing(data_clean):
        list_of_all_str.append(item)
    number_of_xmas = 0
    for item in list_of_all_str:
        if "XMAS" in item:
            number_of_xmas += 1
        elif "XMAS" in item[::-1]:
            number_of_xmas += 1
        else:
            continue
    print(number_of_xmas)
    """


    

if __name__ == "__main__":
    main()
