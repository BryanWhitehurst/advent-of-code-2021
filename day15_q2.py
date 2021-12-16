import sys
import copy

def makeCopy(arr):
    newMatrix = []
    for row in arr: 
        newRow  = [0 for i in range(5 * len(row))]
        for i in range(len(row)):
            newRow[i] = row[i]
        k = len(arr[0])
        for i in range(4 * len(arr[0])):
                val = 1  + newRow[k - len(arr[0])]
                if val == 10: val = 1
                newRow[k] = val
                k += 1
        newMatrix.append(newRow)
    
    #every row extended, now increase length of matrix
    length = len(newMatrix)
    for i in range(4 * length):
        newRow  = [0 for z in range(len(newMatrix[0]))]
        length2 = len(newMatrix[0])
        for j in range(length2):
            val = newMatrix[i][j] + 1
            if val == 10: val = 1
            newRow[j] = val
        newMatrix.append(newRow)

    return newMatrix

def shortest(grid):
    shortest = []
    shortest.append([(0, 0), 0])
    table = [[sys.maxsize for i in range(len(grid))] for j in range(len(grid))]
    table[0][0] = grid[0][0]

    dx = [-1, 0 , 1, 0]
    dy = [0, 1, 0, -1]
    while(len(shortest) > 0): 
        #get cell with minimum distance and delete it from the set
        m = shortest[0] 
        for x in shortest:
            if x[1] < m[1]: m = x
        t = copy.deepcopy(m)
        shortest.remove(m)
        
        for i in range(4):
            x = t[0][0] + dx[i]
            y = t[0][1] + dy[i]

            if not (x >= 0 and x < len(grid) and y >= 0 and y < len(grid)): continue

            if (table[x][y] > table[t[0][0]][t[0][1]] + grid[x][y]):
                
                if table[x][y] < sys.maxsize: shortest.remove([(x, y), table[x][y]])

                table[x][y] = table[t[0][0]][t[0][1]] + grid[x][y]
                shortest.append([(x, y), table[x][y]])
    return table[-1][-1] - 1

f = open("input.txt", "r")
risks  = []
for x in f: 
    risks.append([int(i) for i in x.strip()])

matrix = makeCopy(risks)       
print(shortest(matrix))