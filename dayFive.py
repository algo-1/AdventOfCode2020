# q1
import math 
boarding_passes = []
with open("dayFive.txt") as file:
    for line in file:
        boarding_passes.append(line.strip())

def evalRow(code):
    low = 0
    high = 127 
    curr = 0 
    for char in code:
        if char == "F":
            high = math.floor((low + high) / 2)
            curr = high 
        else:
            low = math.ceil((low + high) / 2)
            curr = low 
    return curr

def evalCol(code):
    low = 0
    high = 7
    curr = 0
    for char in code:
        if char == "L":
            high = math.floor((low + high) / 2)
            curr = high    
        else:
            low = math.ceil((low + high) / 2)
            curr = low  
    return curr 

def getId(code):

    row_val = evalRow(code[:7])   

    col_val = evalCol(code[7:]) 
        
    return (row_val* 8) + col_val

max_id = 0
for code in boarding_passes:
    curr_id = getId(code)
    max_id = max(max_id, curr_id) 

print(f"The highest seat ID is {max_id}")

# q2

sum_ids = 0
for code in boarding_passes:
    current_id = getId(code)
    sum_ids += current_id
# min ID (32) was calculated by slightly altering # q1 solutuion
missing_id = sum([x for x in range(32, 849)]) - sum_ids

print(f"Missing seat ID (my seat ID) is {missing_id}")