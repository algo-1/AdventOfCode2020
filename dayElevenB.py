from copy import deepcopy 
space = []
with open("dayEleven.txt") as file:
    for line in file.readlines():
        temp = []
        for ch in line:
            if ch != "\n":
                temp.append(ch)
        space.append(temp)

def no_occupied_seat(a, b, grid, x, y):
    if a < 0 or a >= len(grid) or b < 0 or b >= len(grid[0]):
        return True
    if grid[a][b] == "L":
        return True 
    if grid[a][b] == "#":
        return False 
    
    return no_occupied_seat(a+x, b +y, grid, x, y)

def is_occupied_seat(a, b, grid, x, y):
    if a < 0 or a >= len(grid) or b < 0 or b >= len(grid[0]):
        return False
    if grid[a][b] == "L":
        return False 
    if grid[a][b] == "#":
        return True  
    
    return is_occupied_seat(a+x, b+y, grid, x, y)

def free_adjascent(grid, i, j):
    axes = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 0
    for x,y in axes:
        if no_occupied_seat(i+x, j+y, grid, x, y):
                count += 1
    return count == 8

def occupied_adjascent(grid, i, j):
    axes = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 0
    for x,y in axes:
        if is_occupied_seat(i+x, j+y, grid, x, y):
                count += 1
    return count >= 5 

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
