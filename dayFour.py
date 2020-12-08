# q1

values = []
with open("dayFour.txt") as file:
    for line in file:
        values.append(line.rstrip())

parsed_values = []
temp = []
i = 0
while i < len(values):
    if values[i] != '':
        temp.append(" " + values[i])
    else:
        parsed_values.append("".join(temp))
        temp = []
    i += 1
# append last temp 
parsed_values.append("".join(temp))   


def isValid(value, credentials):
    count = 0
    for credential in credentials:
        if credential in value:
            count += 1
    return count == len(credentials)

res = 0
must_haves = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for value in parsed_values:
    if isValid(value, must_haves):
        res += 1

print(f"result: {res}")


# q2 
import re 

credential_specifications = {
    "byr": [1920, 2002],
    "iyr": [2010, 2020],
    "eyr": [2020, 2030],
    "in" : [59, 76],
    "cm" : [150, 193],
    "ecl": ["amb", "blu", "brn", "gry", "hzl", "oth", "grn"],
}

def checkAPair(cred, val, keymap):
        pattern = (r'#[a-f0-9]{6}') 
        if cred == "hgt":
            if "in" in val:
                num = int(val.replace("in", ""))
                return keymap["in"][0] <= num and keymap["in"][1] >= num
            elif "cm" in val:
                num = int(val.replace("cm", ""))
                return keymap["cm"][0] <= num and keymap["cm"][1] >= num

        elif cred == "hcl":
            if len(val) == 7:
                match = re.search(pattern, val)
                if match:
                    return True 

        elif cred == "ecl":
            return val in keymap["ecl"]

        elif cred == "pid":
            if len(val) == 9:
                count = 0 
                for s in val:
                    n = int(s)
                    if n >= 0 or n <= 9:
                        count += 1
                return len(val) == count 
        else:
            min_value = keymap[cred][0]
            max_value = keymap[cred][1]

            return int(val) >= min_value and int(val) <= max_value 
        return False 

def checkIfValid(keymap, value, credentials):
    value = value.split()
    for i in range(len(value)):
        value[i] = str(value[i]).split(":")
    
    pairs = {x:y for x,y in value}
    
    for cred in credentials:
        val = pairs[cred]
        if not checkAPair(cred, val, keymap):
            return False 

    return True 

valid = 0
for value in parsed_values:
    if isValid(value, must_haves):
        if checkIfValid(credential_specifications, value, must_haves):
            # print(value)
            # print()
            valid += 1

print(f"Number of valid passports are: {valid}")



