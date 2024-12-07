

def clean_data(data):
    cleaned_data = []
    for item in data:
        cleaned_data.append(item[:-1])
    return cleaned_data




def where_is_waldo(data):
    for i in range(0, len(data[0]) -1):
        for j in range(0, len(data) - 1):
            if data[i][j] == "^":
                return(i,j)
            
def run_waldo(starting_coordinates, data):
    i, j = starting_coordinates
    print(i,j)
    pass

def main():
    with open("06_12_demo_input.txt", "r") as f:
        data = f.readlines()
    cleaned_data = clean_data(data)
    for item in cleaned_data:
        print(item)
    print(len(cleaned_data[0]))
    print(len(cleaned_data))
    i,j = where_is_waldo(data)
    print(i,j)

if __name__ == "__main__":
    main()