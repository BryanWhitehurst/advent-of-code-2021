f = open("input.txt", "r")
inp = []
for x in f:
    inp.append([int(i) for i in x.strip()])

riskLevel = 0
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
            riskLevel += inp[i][j] + 1

print(riskLevel)