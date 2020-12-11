values = [0]
with open("dayTen.txt") as file:
    for line in file:
        num = line.rstrip()
        values.append(int(num))

jolt1 = 0
jolt3 = 0

values.sort()
print(values)
i = 1
while i < len(values):
    val = values[i]
    min_val = values[i-1]
    
    if val - min_val == 1:
        jolt1 += 1
    elif val - min_val == 3:
        jolt3 += 1

    i += 1

print(jolt1 *(jolt3+1))

# q2 optimal dp solution 
lookup = [1]*(len(values))
for curr in range(1, len(values)):
    temp = 0
    i = curr - 1 
    while values[curr] - values[i]  <= 3 and i >= 0:
        temp += lookup[i]
        i -= 1
    lookup[curr] = temp     

print(lookup[-1])

# q2  (brute force)
# from itertools import combinations 

# res = 1 # default case where we remove no value 
# removable = set()
# def get_removable(values, removable):
#     for j in range(len(values)):
#         if j != 0 and j != len(values) - 1:
#             if (values[j] - values[j-1] ) + (values[j+1] - values[j]) <= 3:
#                 removable.add(values[j]) 
     
# def rule_holds(pair, values):
#     nums = values.copy()
#     for v in pair:
#         nums.remove(v)
#     for j in range(len(nums)):
#         if j != 0 and j != len(nums) - 1:
#             if (nums[j] - nums[j-1] ) > 3 or (nums[j+1] - nums[j]) > 3:
#                 return False 
#         elif j == 0:
#             if (nums[0] - 0) > 3 or (nums[1] - nums[0]) > 3:
#                 return False 
#     return True 

# get_removable(values, removable)

# res += len(removable) # ways to remove only one of the removables  
# for i in range(2,len(removable) + 1):
#     vals = combinations(removable, i)
#     for pair in vals:
#         if rule_holds(pair, values):
#             res += 1 
# print(values)
# print(res)



