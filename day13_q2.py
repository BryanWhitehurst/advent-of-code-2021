f = open("input.txt", "r")
pts = []
instr = []
for x in f: 
    if x.split(" ")[0] == 'fold': 
        instr.append(x.split(" ")[2].strip().split("="))
        instr[-1][1] = int(instr[-1][1])
    elif x == "\n": continue
    else: pts.append([int(i) for i in x.strip().split(",")])

def fold(points, fold_c, type):
    length  = len(points)
    i = 0
    point = 0
    for p in range(length):
        if type == 'vertical': point = points[i][0]
        else: point = points[i][1]
        print(point)
        if point > fold_c: 
            newPoint = 0
            if type == 'vertical': newPoint = [(2 * fold_c) - points[i][0], points[i][1]]
            else: newPoint = [points[i][0], (2 * fold_c) - points[i][1]]

            if newPoint in points: 
                if points.index(newPoint) < i:  i -= 1
                points.remove(newPoint) 
            points.append(newPoint)
            points.remove(points[i])

        else: i += 1

for i in instr:
    if i[0] == 'x': fold(pts, i[1], 'vertical')
    else: fold(pts, i[1], 'horizontal')

maxX = 0
maxY = 0
for p in pts:
    maxX = max(maxX, p[0])
    maxY = max(maxY, p[1])

grid = [[' ' for i in range(maxX + 1)] for j in range(maxY + 1)]

for p in pts:
    grid[p[1]][p[0]] = '%'

for row in grid:
    for e in row:
        print(e, end='')
    print("")