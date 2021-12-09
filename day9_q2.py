def getBasinSize(inp, curPoint, visited):
    if curPoint in visited or inp[curPoint[0]][curPoint[1]] == 9: return 0
    visited.append(curPoint)
    i = curPoint[0]
    j = curPoint[1]

    check = [True, True, True, True]
    if i == 0: check[0] = False
    elif i == (len(inp) - 1): check[1] = False

    if j == 0: check[2] = False
    elif j == len(inp[0]) - 1: check[3] = False

    s = 0
    if check[0] and inp[i][j] < inp[i - 1][j]: s += getBasinSize(inp, (i - 1, j), visited)
    if check[1] and inp[i][j] < inp[i + 1][j]: s += getBasinSize(inp, (i + 1, j), visited) 
    if check[2] and inp[i][j] < inp[i][j - 1]: s += getBasinSize(inp, (i, j - 1), visited)
    if check[3] and inp[i][j] < inp[i][j + 1]: s += getBasinSize(inp, (i, j + 1), visited)

    return 1 + s

f = open("input.txt", "r")
inp = []
for x in f:
    inp.append([int(i) for i in x.strip()])

lowPoints = [] 
for i in range(len(inp)):
    for j in range(len(inp[0])):
        check = [True, True, True, True]
        if i == 0: check[0] = False
        elif i == (len(inp) - 1): check[1] = False

        if j == 0: check[2] = False
        elif j == len(inp[0]) - 1: check[3] = False


        isLower = True
        if check[0] and inp[i][j] >= inp[i - 1][j]: isLower = False
        if isLower and check[1] and inp[i][j] >= inp[i + 1][j]: isLower = False 
        if isLower and check[2] and inp[i][j] >= inp[i][j - 1]: isLower = False
        if isLower and check[3] and inp[i][j] >= inp[i][j + 1]: isLower = False

        if isLower: 
            lowPoints.append((i, j))

p = lowPoints[0]
sizes = []
for p in lowPoints: 
    visited = []
    sze = getBasinSize(inp, p, visited)
    sizes.append(sze)

#find three largest
sizes.sort()
length = len(sizes)
print(sizes[length - 1] * sizes[length - 2] * sizes[length - 3])
    

