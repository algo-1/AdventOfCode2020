from collections import defaultdict

graph = defaultdict(int)
labels = [3, 1, 5, 6, 7, 9, 8, 2, 4]

for i in range(10, 1000001):
    labels.append(i)

for i in range(len(labels) - 1):
    graph[labels[i]] += labels[i+1]
graph[labels[-1]] += labels[0]

sorted_labels = sorted(labels)

curr_node = 3
j = 0 

while j < 10000000:
# rearrange graph 
    node1 = graph[curr_node]
    node2 = graph[node1]
    node3 = graph[node2]
    next_three_cups = [node1, node2, node3]
    node_set = set(next_three_cups)
    i = curr_node - 1
    
    while i in node_set:
        i -= 1
    k = 0 
    m = -1 
    while sorted_labels[k] in node_set:
        k += 1
    while sorted_labels[m] in node_set:
        m -= 1
      
    if i < sorted_labels[k]:
            destination_cup = sorted_labels[m]
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
second_node = graph[node]

print(f"ans = {node * second_node}")
