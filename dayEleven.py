from copy import deepcopy 
space = []
with open("dayEleven.txt") as file:
    for line in file.readlines():
        temp = []
        for ch in line:
            if ch != "\n":
                temp.append(ch)
        space.append(temp)

def free_adjascent(space, i, j):
    axes = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    countA = 0
    countB = 0
    for x,y in axes:
        if i+x < len(space) and i+x >= 0 and j+y < len(space[0]) and j+y >= 0:
            countA += 1
            if space[i+x][j+y] != "#":
                countB += 1
    return countA == countB

def occupied_adjascent(space, i, j):
    axes = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    count = 0
    for x,y in axes:
        if i+x < len(space) and i+x >= 0 and j+y < len(space[0]) and j+y >= 0:
            if space[i+x][j+y] == "#":
                count += 1
    return count >= 4 

for _ in range(100):
    curr_state = deepcopy(space)
    for i in range(len(space)):
        for j in range(len(space[0])):
            if space[i][j] == "#":
                if occupied_adjascent(curr_state, i, j):
                    space[i][j] = "L" 
            elif space[i][j] == "L":
                if free_adjascent(curr_state, i, j):
                    space[i][j] = "#"  

    # print('\n'.join(map(''.join, space)))
    # print()

num_occupied = 0
for i in range(len(space)):
    for j in range(len(space[0])):
        if space[i][j] == "#":
            num_occupied += 1

print(num_occupied)
