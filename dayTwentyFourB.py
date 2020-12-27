from copy import deepcopy
dirs = {
    "e":  ( 1, 0),
    "w":  (-1, 0),
    "se": (0.5, -1),
    "sw": (-0.5, -1),
    "ne": (0.5,  1),
    "nw": (-0.5, 1)
}

opp = {
    "black" : "white",
    "white" : "black"
}

tiles = {}
lists = {}
with open("example.txt") as file:
    for line in file:
        pos = [0,0]
        line = line.rstrip()
        vals = line.split()
        for d in vals:
            x = dirs[d][0]
            y = dirs[d][1]

            pos[0] += x
            pos[1] += y 

        tiles[str(pos)] = "white"
        lists[str(pos)] = pos 

curr_tiles = tiles
for i in range(100):
    prev_tiles = deepcopy(curr_tiles)
    for tile, color in prev_tiles.items():
        for d in dirs:
            x = dirs[d][0]
            y = dirs[d][1]
            pos = lists[tile]
            print(pos)
            neigh_x = int(pos[0]) + x
            neigh_y = int(pos[1]) + y 
            value = str([neigh_x, neigh_y])
            if color == "black":
                count1 = 0
                if value in prev_tiles:
                    if prev_tiles[value] == "black":
                        count1 += 1
                else:
                    tiles[value] = "white"
                    lists[value] = [neigh_x, neigh_y]
                if count1 == 0 or count1 > 2:
                    tiles[tile] = "white"
            else:
                count2 = 0
                if value in prev_tiles:
                    if prev_tiles[value] == "black":
                        count2 += 1
                else:
                    tiles[value] = "white"
                    lists[value] = [neigh_x, neigh_y]
                if count2 == 2:
                    tiles[tile] = "black"
            
    curr_tiles = tiles
count = 0
for _,color in tiles.items():
    if color == "black":
        count += 1

print(f"ans = {count}")





# se se nw ne ne ne w se e sw w sw sw w ne ne w se w sw 
# ne e e ne se nw nw w sw ne ne w nw w se w ne nw se sw e sw 
# se sw ne sw sw se nw w nw se 
# nw nw ne se e sw sw ne ne w ne sw w ne w se sw ne se e ne 
# sw w e sw ne sw ne nw se w nw ne ne se e nw 
# e e se nw se sw sw ne nw sw nw nw se w w nw se ne 
# se w ne ne ne ne se nw se w ne nw w w se 
# w e nw w w e se e e w e sw w w nw w e 
# w sw e e se ne ne w nw w nw se ne w se nw w se se se nw ne 
# ne e sw se e nw w sw nw sw sw nw 
# ne nw sw w se w sw ne ne ne w se nw se nw ne se se ne w 
# e ne w nw e w ne sw se w nw sw e nw e sw ne nw se nw sw 
# sw e ne sw ne sw ne ne e nw ne w e ne w w ne sw sw ne se 
# sw w e se ne se w e nw ne sw nw w ne se sw w ne 
# e ne se nw sw w sw ne ne sw se nw ne w sw se e nw se se 
# w nw ne se ne se ne nw w ne nw se w e se w se se se w 
# ne ne w sw nw e w sw ne ne se nw ne se w e sw 
# e ne sw nw sw nw se ne nw nw nw w se e sw ne e w se ne se 
# ne sw nw e w nw nw se e nw se e se w se nw sw e e w e 
# w se w e e e nw ne se nw w w sw ne w 