from collections import defaultdict

graph = defaultdict(list)

visited = {}
has_shiny_gold = {}

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
                graph[key].append(-1)
            else:
                to_append = bag[2:]
                to_append = to_append.replace(" bags", "")
                to_append = to_append.replace(" bag", "")
                graph[key].append(to_append)
            
            visited[key] = False
            has_shiny_gold[key] = False
             

# q1 

visited[-1] = False
visited["shiny gold"] = True 
has_shiny_gold["shiny gold"] = True
has_shiny_gold[-1] = False 

def dfs(node, graph, visited, has_shiny_gold):
    if node == -1:
        return 
        
    visited[node] = True 

    for child in graph[node]:
        if visited[child] == True:
            if has_shiny_gold[child] == True:
                has_shiny_gold[node] = True 
        else:
            dfs(child, graph, visited, has_shiny_gold)
            if has_shiny_gold[child] == True:
                has_shiny_gold[node] = True 

for node in graph:
    if visited[node] == False:
        dfs(node, graph, visited, has_shiny_gold)

res = 0 
for node in has_shiny_gold:
    if has_shiny_gold[node] == True and node != "shiny gold":
        res += 1 

print(f"The number of bag colors that can eventually contain at least one shiny gold bag is {res}") 

