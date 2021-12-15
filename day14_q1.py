def matchRules(poly, rules, numSteps):
    for k in range(numSteps):
        j = 0
        newPoly = poly
        for i in range(1, len(poly)):
            rule = poly[i - 1] + poly[i]
            newPoly = newPoly[:i + j] + rules[rule] + newPoly[i + j:] #until and not including index
            j += 1
        poly = newPoly
    return poly

f = open("input.txt", "r")

poly = f.readline().strip()
rules = {}
f.readline()
for x in f: 
    x1, x2 = x.strip().split(" -> ")
    rules[x1] = x2


str = matchRules(poly, rules, 40)
numOccurances = {}
max = 0
min = 1000000000
for c in str: 
    if c not in numOccurances: numOccurances[c] = 1
    else: numOccurances[c] += 1

for c in str:
    if numOccurances[c] > max: max = numOccurances[c]
    if numOccurances[c] < min: min = numOccurances[c] 
print(max - min)

