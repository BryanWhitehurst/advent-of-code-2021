def fillDiagram(lines, diagram):
    for line in lines: 
        if line[0][0] != line[1][0] and line[0][1] != line[1][1]: continue

        #horizontal line
        if line[0][1] == line[1][1]:
            y = line[0][1]
            for i in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
                diagram[y][i] += 1
        
        #vertical line
        if line[0][0] == line[1][0]:
            y = line[0][0]
            for i in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
                diagram[i][y] += 1

def countOverlap(diagram):
    count = 0
    for i in range(len(diagram)):
        for j in range(len(diagram[0])):
            if diagram[i][j] > 1: count += 1
    return count


lines = []

f = open("input.txt", "r")


#split based off "->"
maxX = 0 
maxY  =0
for x in f: 
    points  = x.strip().split(" -> ")
    line = []
    for p in points:
        test = map(int, p.split(","))
        curX = test[0]
        curY = test[1]
        maxX = max(curX, maxX)
        maxY = max(curY, maxY)
        line.append(test)
    lines.append(line)


diagram = [[0 for i in range(maxX + 1)] for j in range(maxY + 1)]
fillDiagram(lines, diagram)
print(countOverlap(diagram))
