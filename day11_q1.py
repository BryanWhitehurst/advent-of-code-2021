grid  = []

f = open("input.txt", "r")
for x in f:
    grid.append([int(i) for i in x.strip()])

def recurse(grid):
    #increase energy level of each by 1
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] += 1
    
    #check for flashes and keep track of each element that flashes
    flashed = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] > 9 and (i, j) not in flashed: 
                flashed.append((i, j))

    for e in flashed:
        increaseAdjacent(grid, e, flashed)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 9: grid[i][j] = 0
    return len(flashed)

def increaseAdjacent(grid, point, flashed):
    i = point[0]
    j = point[1]
    #need to see if diagonals are 
    check = [True, True, True, True]
    if i == 0: check[0] = False
    elif i == (len(grid) - 1): check[1] = False

    if j == 0: check[2] = False
    elif j == len(grid[0]) - 1: check[3] = False

    if check[0]:
        grid[i - 1][j] += 1
        if grid[i - 1][j] > 9 and (i - 1, j) not in flashed: flashed.append((i - 1, j))
    if check[1]: 
        grid[i + 1][j] += 1
        if grid[i + 1][j] > 9 and (i + 1, j) not in flashed: flashed.append((i + 1, j))
    if check[2]: 
        grid[i][j - 1] += 1 
        if grid[i][j - 1] > 9 and (i, j - 1) not in flashed: flashed.append((i, j - 1))
    if check[3]: 
        grid[i][j + 1] += 1
        if grid[i][j + 1] > 9 and (i, j + 1) not in flashed: flashed.append((i, j + 1))
    if check[0] and check[2]: 
        grid[i - 1][j - 1] += 1
        if grid[i - 1][j - 1] > 9 and (i - 1, j - 1) not in flashed: flashed.append((i - 1, j - 1))
    if check[0] and check[3]: 
        grid[i - 1][j + 1] += 1
        if grid[i - 1][j + 1] > 9 and (i - 1, j + 1) not in flashed: flashed.append((i - 1, j + 1))
    if check[1] and check[2]: 
        grid[i + 1][j - 1] += 1
        if grid[i + 1][j - 1] > 9 and (i + 1, j - 1) not in flashed: flashed.append((i + 1, j - 1))
    if check[1] and check[3]: 
        grid[i + 1][j + 1] += 1
        if grid[i + 1][j + 1] > 9 and (i + 1, j + 1) not in flashed: flashed.append((i + 1, j + 1))


total = 0 
for i in range(100):
    total += recurse(grid)

print(total)