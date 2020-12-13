import math
data = []
with open("dayThirteen.txt") as file:
    for line in file.readlines():
        line = line.rstrip()
        data.append(line)

data[1] = data[1].split(",")

# # q1 
cap = int(data[0])
vals = []
i = []
for v in data[1]:
    try:
        v = int(v)
        vals.append(math.ceil(cap/v)*v)
        i.append(v)
    except :
        pass
    
print((min(vals)-cap)*i[vals.index(min(vals))]) 


# q2 
values = data[1]
for i in range(len(values)):
    if values[i] != "x":
        print(i, values[i])

# use chinese remainder theorem

# x is congruent to 0 mod values[0]
# x is congruent to -index mod values[i] (1 -> last index)

# I spotted the Chinese remainder theorem could be used while going through the example 
# especially with how values[i] were all coprime
# However, I did not write code for this. I simply made use of an online calculator 😅