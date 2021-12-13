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
def find_path(graph, start, end, path=[], real = []):
    if start.islower(): path.append(start)
    real.append(start)
    if start == end: paths.append(real)
    for node in graph[start]: 
            
        if node not in path:
            newpath = find_path(graph, node, end, copy.deepcopy(path), copy.deepcopy(real))
            if newpath: paths.append(real) #if newpath not empty

find_path(inp, 'start', 'end')
print(len(paths))
