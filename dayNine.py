from collections import deque
values = []
with open("dayNine.txt") as file:
    for line in file:
        num = line.rstrip()
        values.append(int(num))
preambles = deque(values[:25])

def calculate_sums(preambles):
    sums = set()
    for i in range(len(preambles)):
        for j in range(len(preambles)):
            if i != j:
                sums.add(preambles[i]+preambles[j])
    return sums 
curr_index = 25 
for i in range(25, len(values)):
    sums = calculate_sums(preambles)
    if values[i] not in sums:
        print(values[i])
        break
    preambles.popleft()
    preambles.append(values[curr_index])
    curr_index += 1

# q2 

i = -1
j = 0
tot = 0
while j < len(values):
    tot += values[j]
    while tot > 776203571:
        i += 1
        tot -= values[i]
    if tot == 776203571:
        print(max(values[i+1:j+1]) + min(values[i+1:j+1])) # starts at i+1 to j as i has been removed 
        break 
    j += 1
