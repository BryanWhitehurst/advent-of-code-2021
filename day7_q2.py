#determine cost of each position, then use the one that has the least fuel

def additionalCost(num):
    #5 a change in 5 positions results in cost: 1 + 2 + 3 + 4 + 5
    total = 0
    for i in range (1, num + 1): 
        total += i
    return total
    
def bestPos(inp):
    maxPos = max(inp)
    minPos = min(inp)
    lowestCost = 0

    for i in range(minPos, maxPos + 1):
        curCost = 0
        for val in inp:
            curCost += additionalCost(abs(i - val))
        if i == minPos: lowestCost = curCost
        elif curCost < lowestCost: lowestCost = curCost
    return lowestCost


f = open("input.txt", "r")
inp = map(int, f.read().split(","))

print(bestPos(inp))