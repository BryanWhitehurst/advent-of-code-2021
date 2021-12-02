def finalPosition(inp):
    horizontal = 0
    depth = 0
    aim = 0
    for item in inp:
        if item[0] == 'forward': 
            horizontal += item[1]
            depth += aim * item[1]
        elif item[0] == 'down':
            aim += item[1]
        else: 
            aim -= item[1]
    return horizontal * depth


f = open("input.txt", "r")
inp = []
for line in f:
    a = line.split()
    inp.append([a[0], int(a[1])])
    
print(finalPosition(inp))