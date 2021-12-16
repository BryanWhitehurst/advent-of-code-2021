import sys
import copy
f = open("input.txt", "r")
risks  = []
for x in f: 
    risks.append([int(i) for i in x.strip()])

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
    return table[-1][-1] - 2
            
print(shortest(risks))