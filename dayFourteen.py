def convertToMaskedDecimal(mask, dec):
    binStr = '{:036b}'.format(dec)
    binList = list(binStr)
    for i in range(36):
        if binStr[i] != mask[i] and mask[i] != "X":
            binList[i] = mask[i]
    
    binStr = "".join(binList)
    
    return int(binStr, 2)
    
def maskedMemory(mem, mask):
    binStr = '{:036b}'.format(mem)
    binList = list(binStr)

    numX = mask.count("X")
    combos = []
    for i in range(2**numX):
        binstr = '{:0{}b}'.format(i, numX)
        combos.append(binstr)

    ans = []
    toChange = []
    for i in range(36):
        if mask[i] == "1":
            binList[i] = "1"
        elif mask[i] == "X":
            binList[i] = "X"
            toChange.append(i)
   
    for pair in combos:
        for j in range(numX):
            binList[toChange[j]] = pair[j]

        ans.append(int("".join(binList), 2))
    
    return ans 

mask = ""
mem = {}
mem2 = {}
with open("dayFourteen.txt") as file:
    for line in file:
        line = line.rstrip()
        if line[:4] == "mask":
            mask = line[7:]
        else:
            line = line.replace("mem", "")
            line = line.replace("[", "")
            line = line.replace("]", "")
            line = line.replace("=", "")
            val = line.split()

            mem[val[0]] = convertToMaskedDecimal(mask, int(val[1]))
            for memory in maskedMemory(int(val[0]), mask):
                mem2[memory] = int(val[1])

res = 0
for key in mem:
    res += mem[key]

print("q1 ->", res)


ans = 0
for v in mem2:
    ans += mem2[v]

print("q2 ->", ans)
