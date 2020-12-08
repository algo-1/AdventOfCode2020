# q1 

values = []
with open("dayTwo.txt") as file:
    for line in file:
        line = line.rstrip()
        line = line.replace(":", "")
        line = line.replace("-", " ")
        values.append(line)

def isValid(password, low, high, specified_letter):
    count = 0
    for i in range(len(password)):
        if password[i] == specified_letter:
            count += 1
        if count > high:
            return False 
        
    if count < low:
        return False 
    
    return True 

count = 0 
for val in values:
    val = val.split()
    # print(val)
    low = int(val[0])
    high = int(val[1])
    specified_letter = val[2]
    password = val[3] 

    if isValid(password, low, high, specified_letter):
        count += 1

print(count)


# q2 

def isValidModified(password, low, high, specified_letter):
    if password[low - 1] == specified_letter and password[high-1] == specified_letter:
        return False
    elif password[low - 1] == specified_letter or password[high-1] == specified_letter:
        return True 
    
    return False 


counter = 0 
for val in values:
    val = val.split()
    # print(val)
    low = int(val[0])
    high = int(val[1])
    specified_letter = val[2]
    password = val[3] 

    if isValidModified(password, low, high, specified_letter):
        counter += 1

print(counter)
