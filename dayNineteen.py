from functools import lru_cache
from collections import defaultdict

rules = defaultdict(list)

with open("dayNineteenRules.txt") as f:
    for text in f:
        rule, vals = text.split(" : ")
        if "|" in vals:
            vals = vals.split(" | ")
            for v in vals:
                rules[rule].append(v.split())
        else:
            rules[rule].append(vals.split())

@lru_cache(None)
def match_rules(string, num):
    for pattern in rules[num]:
        if len(pattern) == 2:
            a = pattern[0]
            b = pattern[1]

            for i in range(1, len(string)):
                if match(string[:i], a) and match(string[i:], b):
                    return True

        elif len(pattern) == 3:
            a = pattern[0]
            b = pattern[1]
            c = pattern[2]

            for i in range(1, len(string) - 1):
                for j in range(2, len(string)):
                    if match(string[:i], a) and match(string[i:j], b) and match(string[j:], c):
                        return True
        else:
            a = pattern[0]
            if match(string, a):
                return True  
        
    return False

@lru_cache(None)
def match(string, num):
    if num == "a" or num == "b":
        return string == num
    else:
        return match_rules(string, num)

count = 0
with open("dayNineteen.txt") as file:
    for line in file:
        line = line.strip()
        x = rules["0"][0][0]
        y = rules["0"][0][1]
        for i in range(1, len(line)):
            if match(line[:i], x) and match(line[i:], y):
                count += 1
                break
        
print(f" ans = {count}")

# q2 rules replaced in ...Rules.txt  
# 8 : 42 | 42 8
# 11 : 42 31 | 42 11 31

# q1 rules 
# 8 : 42 
# 11 : 42 31 

# quotes on letters a & b removed from ...Rules.txt as well