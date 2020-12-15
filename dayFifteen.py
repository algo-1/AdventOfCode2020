with open("dayFifteen.txt") as file:
    line = file.read().rstrip()
    start_nums = [int(num) for num in line.split(",")]
pairs = {}
for i in range(len(start_nums)):
    pairs[start_nums[i]] = [i+1, 0]

j = len(start_nums)

while j < 30000000: # 2020 for #q1
    last_num = start_nums[j-1] 
    if pairs[last_num][1] == 0:
        start_nums.append(0)
        if pairs[0][1] == 0:
            pairs[0][1] = j + 1
        else:
            pairs[0][0] = pairs[0][1]
            pairs[0][1] = j +1 

    else:
        diff = pairs[last_num][1] - pairs[last_num][0]
        start_nums.append(diff)
        if diff in pairs:
            if pairs[diff][1] == 0:
                pairs[diff][1] = j + 1
            else:
                pairs[diff][0] = pairs[diff][1]
                pairs[diff][1] = j + 1 
        else:
            pairs[diff] =[j+1, 0]

    j += 1

print(start_nums[30000000 - 1]) # -> [ 2020 - 1 ] for #q1 

