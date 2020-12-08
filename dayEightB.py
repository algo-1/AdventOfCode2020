from copy import deepcopy
inst = []
with open("dayEight.txt") as file:
    for line in file:
        line = line.rstrip()
        line = line.split()
        inst.append([line[0], int(line[1]), False])

pairs = {
    "jmp" : "nop",
    "nop" : "jmp"
}

def check_if_terminates(inst, acc):
    i = 0
    while i < len(inst):
        if inst[i][2] == True:
            return False 
        elif inst[i][0] == "nop":
            inst[i][2] = True 
            i += 1 
        elif inst[i][0] == "jmp":
            inst[i][2] = True 
            i += inst[i][1]
        elif inst[i][0] == "acc":
            acc[0] += inst[i][1]
            inst[i][2] = True 
            i+= 1
    return True 
for i in range(len(inst)):
    if inst[i][0] in pairs:
        acc_val = [0] 
        faux_inst = deepcopy(inst)
        faux_inst[i][0] = pairs[inst[i][0]]
        if check_if_terminates(faux_inst, acc_val):
            break

print(acc_val[0])