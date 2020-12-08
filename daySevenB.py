from collections import defaultdict

graph = defaultdict(list)

with open("daySeven.txt") as file:
    for line in file:
        line = line.strip()
        line = line.replace(".", "")
        line = line.split(" contain ")

        for bag in line[1].split(", "):
            key = line[0]
            key = key.replace(" bags", "")
            key = key.replace(" bag", "")

            if "no" in line[1]:
                graph[key].append((-1, 0))
            else:
                to_append = bag[2:]
                num = int(bag[:1])
                to_append = to_append.replace(" bags", "")
                to_append = to_append.replace(" bag", "")
                graph[key].append((to_append, num))
            

def getTotalBags(node, graph):
    if node == -1:
        return 0 
    res = 0
    for child in graph[node]:
        temp = child[1] + child[1]*getTotalBags(child[0], graph) 
        res += temp 

    return res  

totalBags = getTotalBags("shiny gold", graph)

print(f"A single shiny gold bag must contain {totalBags} other bags")