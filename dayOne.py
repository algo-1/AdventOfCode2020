# q1 

years = []
with open("dayOne.txt") as file:
    for line in file:
        line = line.rstrip()
        years.append(int(line))

def two_sum(years):
    low = 0
    high = len(years) - 1 
    years.sort()
    while low < high:
        val = years[low] + years[high]
        if val == 2020:
            return (years[low], years[high], years[low]*years[high])
        if val < 2020:
            low += 1
        else:
            high -= 1
    return -1

print(two_sum(years))

# q2

def three_sum(years):
    years.sort()

    start = 0

    while years[start+ 1] == years[start-1] and start < len(years) - 3:
        start += 1
    
    for i in range(start, len(years) - 2):
        j = i+1 
        k = len(years) - 1
        while j < k:
            val = years[i] + years[j] + years[k]
            if val == 2020:
                return (years[i], years[j], years[k], years[i]*years[j]*years[k])
            elif val < 2020:
                j += 1
            else:
                k -= 1 

    return -1 

print(three_sum(years))
