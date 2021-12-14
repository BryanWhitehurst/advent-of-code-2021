f = open("input.txt", "r")
pts = []
instr = []
for x in f: 
    if x.split(" ")[0] == 'fold': 
        instr.append(x.split(" ")[2].strip().split("="))
        instr[-1][1] = int(instr[-1][1])
    elif x == "\n": continue
    else: pts.append([int(i) for i in x.strip().split(",")])

def horizontalFold(points, fold_y):
    length  = len(points)
    i = 0
    for p in range(length):
        if points[i][1] > fold_y: 
            newPoint = [points[i][0], (2 * fold_y) - points[i][1]]
            if newPoint in points:
                if points.index(newPoint) < i:  i -= 1
                points.remove(newPoint) 
            points.append(newPoint)
            points.remove(points[i])

        else: i += 1

def verticalFold(points, fold_x):
    length  = len(points)
    i = 0
    for p in range(length):
        if points[i][0] > fold_x: 
            newPoint = [(2 * fold_x) - points[i][0], points[i][1]]

            if newPoint in points: 
                if points.index(newPoint) < i:  i -= 1
                points.remove(newPoint) 
            points.append(newPoint)
            points.remove(points[i])

        else: i += 1

verticalFold(pts, instr[0][1])
print(len(pts))
