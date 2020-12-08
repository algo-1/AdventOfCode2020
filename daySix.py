import string
from collections import defaultdict

values = []
with open("daySix.txt") as file:
    for line in file:
        values.append(line.rstrip())

groups = []
temp = []
i = 0
while i < len(values):
    if values[i] != '':
        temp.append(" " + values[i])
    else:
        groups.append("".join(temp))
        temp = []
    i += 1
# append last temp 
groups.append("".join(temp))

# q1 
   
def getYesValue(group, keys):
    yesCount = 0
    for val in set(group):
        if val in keys:
            yesCount += 1
    return yesCount

yesValues = string.ascii_lowercase
res = 0 
for group in groups:
    res += getYesValue(group, yesValues)

print(f"Total number of yesses is {res}")


# q2 

def getCommonYesValue(group, keys):
    yesCount = 0
    for passanger in group.split():
        for val in passanger:
            keys[val] += 1 
    
    for key in keys:
        if keys[key] == len(group.split()):
            yesCount += 1
  
    return yesCount


result = 0

for group in groups:
    keys = defaultdict(int)
    result += getCommonYesValue(group, keys)

print(f"Total number of common yesses is {result}")

