from collections import defaultdict

valid = set()
ranges = []
keys = defaultdict(list) 

res = 0 
with open("daySixteenA.txt") as file:
    for line in file:
        line = line.rstrip()
        line = line.replace("or", "")
        line = line.split()
        temp = set()
        for val in line:
            values = val.split("-")
            low = values[0]
            high = values[1]
            for i in range(int(low), int(high)+1):
                valid.add(i)
                # q2 
                temp.add(i)
        
        ranges.append(temp)

with open("daySixteenNearbyTickets.txt") as f:
    for line in f:
        line = line.rstrip()
        new_row = []
        for num in line.split(","):
            if int(num) not in valid:
                res += int(num)
            # q2 
            else:
                new_row.append(int(num))

        n = len(new_row)
        for i in range(n):
            keys[i].append(int(new_row[i]))

data = {}
for col in keys:
    fits = set()
    for i in range(len(ranges)):
        count = 0
        for num in keys[col]:
            if num in ranges[i]:
                count += 1 
        if count == len(keys[col]):
            fits.add(i)
    # print(col, fits, len(fits))
    data[col] = fits 

def get_range_index(fit, seen):
    for v in fit:
        if v not in seen:
            return v 

seen = set()
range_to_col = {}
for i in range(1, 20+1):
    for col, fit in data.items():
        if len(fit) == i:
            index = get_range_index(fit, seen)
            seen.add(index)
            range_to_col[index] = col 
            break 

# q1
print(f"q1: {res}")

# q2 
my_ticket = [83,127,131,137,113,73,139,101,67,53,107,103,59,149,109,61,79,71,97,89]

prod = 1
for i in range(6):         # <- top 6 ranges correspond to the departures 
    col = range_to_col[i]
    # print(i, col)
    prod *= my_ticket[col]

print(f"q2: {prod}")


