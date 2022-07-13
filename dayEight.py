inst = []
with open("dayEight.txt") as file:
    for line in file:
        line = line.rstrip()
        line = line.split()
        inst.append([line[0], int(line[1]), False])
done = False
i = 0
acc = 0 
while not done and i < len(inst):
    if inst[i][2] == True:
        done = True 
    elif inst[i][0] == "nop":
        inst[i][2] = True 
        i += 1 
    elif inst[i][0] == "jmp":
        inst[i][2] = True 
        i += inst[i][1]
    elif inst[i][0] == "acc":
        acc += inst[i][1]
        inst[i][2] = True 
        i+= 1
    

print(acc)


