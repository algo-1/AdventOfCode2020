# q1

rows = []
with open("dayThree.txt") as file:
    for line in file:
        row = []
        line = line.rstrip()
        for letter in line:
            row.append(letter)
        rows.append(row)

def traverse(grid, i, j, res):
    
    n = len(grid)
    m = len(grid[0])

    j = j % m 
    if i >= n:
        return
    if grid[i][j] == '#':
        res[0] += 1
    for x,y in [(1,3)]:
        traverse(grid, i+x, j+y, res)

res = [0]

traverse(rows, 0, 0, res)
print(res[0])


# q2

def traverseTwo(grid, i, j, res, a, b):
    
    n = len(grid)
    m = len(grid[0])

    j = j % m 
    if i >= n:
        return
    if grid[i][j] == '#':
        res[0] += 1
    for x,y in [(a,b)]:
        traverseTwo(grid, i+x, j+y, res, a, b)


values = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

prod = 1
for x,y in values:
    result = [0]
    traverseTwo(rows, 0, 0, result, x, y)
    print(result[0])
    prod *= result[0]

print(f"answer is {prod}")