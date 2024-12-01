## import file and create two lists
## sort those lists
list_1 = []
list_2 = []

with open("input_01_12.txt", "r") as f:
    for line in f:
        _line_split = line[:-1].split(" ")
        for item in _line_split:
            if (len(item) > 0) & (len(list_1) == len(list_2)):
                list_1.append(int(item))
            elif len(item) > 0 & (len(list_1) > len(list_2)):
                list_2.append(int(item))
            else:
                continue

## sort the lists in place
list_1.sort()
list_2.sort()

## part 1
distance = 0
for i in range(len(list_2)):
    distance += abs(list_1[i] - list_2[i])
    
print("Task 1: find the distance between the sorted lists: ", distance)

## part 2
similarity_score = 0
for i in range(len(list_1)):
    similarity_score += list_2.count(list_1[i]) * list_1[i]

print("Task 2: find the similarity score: ", similarity_score)