import copy

f = open("input.txt", "r")
inp = {}
for x in f:
    n1, n2 = x.strip().split("-")
    if not inp.has_key(n1): inp[n1] = [n2]
    else: inp[n1].append(n2)
    if not inp.has_key(n2): inp[n2] = [n1]
    else: inp[n2].append(n1)

paths = []
def countDistinct(graph, start, end, visited = [], real = [], smallCaves = [], visitedTwice = False):
    if start == 'start' or start == 'end':  visited.append(start)
    elif start.islower() and visitedTwice and start not in visited:
        visited.append(start)
    elif start.islower() and not visitedTwice and start in smallCaves: 
        visited.append(start)
        visitedTwice = True
    elif start.islower() and not visitedTwice: smallCaves.append(start)

    real.append(start)


    if start == end: 
        #print(visitedOnce)
        #print(real)
        paths.append(real)
    else: 
        for node in graph[start]: 
            #print(start)
            #print("Graph Start ", graph[start])
            if visitedTwice and node in smallCaves: continue
            if node not in visited: countDistinct(graph, node, end, copy.deepcopy(visited), copy.deepcopy(real), copy.deepcopy(smallCaves), visitedTwice)

countDistinct(inp, 'start', 'end')
print(len(paths))

