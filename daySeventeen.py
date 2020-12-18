from collections import deque
from copy import deepcopy

gridddd = deque()

with open("daySeventeen.txt") as file:
    for line in file:
        line = line.rstrip()
        temp = deque(char for char in line)
        gridddd.append(temp)

zmap = {0: gridddd}
hyperspace = {0: {0: deepcopy(gridddd)}}  # <- important lesson here using the same grid without deepcopy would cause errors as part 1 modifies it first

def pad_zmap(ZMAP, n):
    # pad top down left right with inactive cubes 
    for _, grid in ZMAP.items():
        grid.appendleft(deque("." for _ in range(n)))
        grid.append(deque("." for _ in range(n)))
        for row in grid:
            row.appendleft(".")
            row.append(".")

def hyper_pad(hyperspace):
    for _,z_mapp in hyperspace.items():
        pad_zmap(z_mapp, len(hyperspace[0][0]))

def create_grid(n):
    return deque(deque("." for _ in range(n)) for _ in range(n))

def create_3d(negg, poss, hyperspace):
    hyperspace[negg] = deepcopy(hyperspace[0])
    for _,g in hyperspace[negg].items():
        for i in range(len(g)):
            for j in range(len(g[i])):
                if g[i][j] == "#":
                    g[i][j] = "."
    hyperspace[poss] = deepcopy(hyperspace[0])
    for _,g in hyperspace[poss].items():
        for i in range(len(g)):
            for j in range(len(g[i])):
                if g[i][j] == "#":
                    g[i][j] = "."

    for _,z_map in hyperspace.items():
        z_map[poss] = create_grid(len(hyperspace[0][0][0]))
        z_map[negg] = create_grid(len(hyperspace[0][0][0]))


def check(zmap, zmap_clone, x, y, z, active = True):
    pairs = [(0,0), (0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]
    z_dir = [z-1, z, z +1]
    count = 0
    for a,b in pairs:
        if a+x < 0 or b+y <0 or a+x >= len(zmap_clone[z]) or b+y >= len(zmap_clone[z]):
            continue
        if a ==0 and b == 0:
            for Z in z_dir:
                if z != Z:
                    if Z in zmap_clone:
                        grid = zmap_clone[Z]
                        if grid[a+x][b+y] == "#":
                            count += 1
                            if count > 3:
                                zmap[z][x][y] = "."
                                return 
        else:
            for Z in z_dir:
                if Z in zmap_clone:
                    grid = zmap_clone[Z]
                    if grid[a+x][b+y] == "#":
                        count += 1
                        if count > 3:
                            zmap[z][x][y] = "."
                            return 
    if active:
        if count == 2 or count == 3:
            zmap[z][x][y] = "#"
        else:
            zmap[z][x][y] = "."
    else:
        if count == 3:
            zmap[z][x][y] = "#"
    
def hypercheck(hyperspace, hyperspace_clone, x, y, z, w, active=True):
    pairs = [(0,0,0), (0, 1, 0), (1, 0, 0), (1, 1, 0), (0, -1, 0), (-1, 0, 0), (-1, -1, 0), (1, -1, 0), (-1, 1, 0), 
    (0,0,-1), (0, 1, -1), (1, 0, -1), (1, 1, -1), (0, -1, -1), (-1, 0, -1), (-1, -1, -1), (1, -1, -1), (-1, 1, -1),
    (0,0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 1), (0, -1, 1), (-1, 0, 1), (-1, -1, 1), (1, -1, 1), (-1, 1, 1)
    ]

    w_dir = [w-1, w, w+1]
    count = 0
    for a,b,c in pairs:
        if a+x < 0 or b+y <0 or a+x >= len(hyperspace[0][0]) or b+y >= len(hyperspace[0][0]):
            continue
        if a ==0 and b == 0 and c == 0:
            for W in w_dir:
                if w != W:
                    if W in hyperspace_clone and z+c in hyperspace_clone[W]:
                        a_grid = hyperspace_clone[W][z+c]
                        if a_grid[a+x][b+y] == "#":
                            count += 1
                            if count > 3:
                                hyperspace[w][z][x][y] = "."
                                return 
        else:
            for W in w_dir:
                if W in hyperspace_clone and z+c in hyperspace_clone[W]:
                    a_grid = hyperspace_clone[W][z+c]
                    if a_grid[a+x][b+y] == "#":
                        count += 1
                        if count > 3:
                            hyperspace[w][z][x][y] = "."
                            return 
    if active:
        if count == 2 or count == 3:
            hyperspace[w][z][x][y] = "#"
        else:
            try:
                hyperspace[w][z][x][y] = "."
            except:
                print(w,z,x,y)
                
    else:
        if count == 3:
            hyperspace[w][z][x][y] = "#"

for i in range(1, 7):
    neg = -1 * i 
    pos = i 
    n = len(zmap[0])
    zmap[neg] = create_grid(n)
    zmap[pos] = create_grid(n)
    pad_zmap(zmap, n)
    zmap_clone = deepcopy(zmap)
 
    for z,grid in zmap_clone.items():
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "#":
                    check(zmap, zmap_clone, i, j, z)
                else:
                    check(zmap, zmap_clone, i, j, z, active=False)

    # for _,g in zmap.items():
    #     print('\n'.join(map(' '.join, g)))

count = 0 

for z in zmap:
    count += sum(row.count("#") for row in zmap[z])

print(f"Number of active Conway cubes = {count}")


for l in range(1,7):
    negg = -l
    poss = l
    create_3d(negg, poss, hyperspace)
    hyper_pad(hyperspace)
    hyperspace_clone = deepcopy(hyperspace)
    for w, z_map in hyperspace_clone.items():
        for Z, gridd in z_map.items():
            for x in range(len(gridd)):
                for y in range(len(gridd[x])):
                    if gridd[x][y] == "#":
                        hypercheck(hyperspace, hyperspace_clone, x, y, Z, w)
                    else:
                        hypercheck(hyperspace, hyperspace_clone, x, y, Z, w, active=False)
    # for q, zmapsss in hyperspace.items():
    #     for v,g in zmapsss.items():
    #         print(q,v, '\n'.join(map(''.join, g)))
    # print()
    # print()

# print(hyperspace.keys())
# for k in hyperspace:
#     print(k, hyperspace[k].keys())

hyper_count = 0

for _,zmap in hyperspace.items():
    for _,grid in zmap.items():
        hyper_count += sum(row.count("#") for row in grid)

print(f"Number of active hypercubes = {hyper_count}")


# p.s the funny names like gridddd are because I was debugging and thought scope was the issue
# so I just added more letters instead of thinking of new names 😅 


    