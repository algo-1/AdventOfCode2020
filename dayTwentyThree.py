from collections import defaultdict

graph = defaultdict(int)
labels = [3, 1, 5, 6, 7, 9, 8, 2, 4]#[3,8,9,1,2,5,4,6,7]
# save = [3, 1, 5, 6, 7, 9, 8, 2, 4]
label_set = set(labels)

for i in range(len(labels) - 1):
    graph[labels[i]] += labels[i+1]
graph[labels[-1]] += labels[0]

curr_node = 3
j = 0 

while j < 100:
# rearrange graph 
    node1 = graph[curr_node]
    node2 = graph[node1]
    node3 = graph[node2]
    next_three_cups = [node1, node2, node3]
    node_set = set(next_three_cups)
    i = curr_node - 1
    
    while i in node_set:
        i -= 1
        
    if i < min(label_set - node_set):
            destination_cup = max(label_set - node_set)
    else:
        destination_cup = i
    
    graph[curr_node] = graph[node3]
    after_node3 = graph[destination_cup]
    graph[destination_cup] = node1
    graph[node3] = after_node3 

    next_node = graph[curr_node]
    curr_node = next_node

    j += 1
    
node = graph[1]
print(node, end="")
while node != 1:
    node = graph[node]
    if node != 1:
        print(node, end = "")

