import copy

def matchRules(poly, rules, numSteps):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counts = {}
    for l in alphabet: 
        counts[l] = 0
    for s in poly: 
        counts[s] += 1

    for i in range(1, len(poly)):
        s = poly[i - 1] + poly[i]
        rules[s][1] += 1
    for k in range(numSteps):
        rules2 = copy.deepcopy(rules)
        for key in rules: 
            num = rules[key][1]
            produces = rules[key][2]
            for p in produces: 
                print(p)
                print(p in rules)
                if p in rules: rules2[p][1] += num
            rules2[key][1] -= num
            counts[rules[key][0]] += num
        rules = copy.deepcopy(rules2)
    print(rules)
    print(counts)

    return counts



"""def matchRules(poly, rules, numSteps):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counts = {}
    for l in alphabet: 
        counts[l] = 0
    futurePairs = []
    for i in range(1, len(poly)):
            futurePairs.append(poly[i - 1] + poly[i])
    for s in poly: 
        counts[s] += 1

    for k in range(numSteps):
        print(k)
        curPairs = copy.deepcopy(futurePairs)
        futurePairs = []
        for p in curPairs: 
            counts[rules[p]] += 1
            s1 = p[:1] + rules[p]
            s2 = rules[p] + p[1:]
            if s1 in rules: futurePairs.append(s1)
            if s2 in rules: futurePairs.append(s2)


    return counts"""

f = open("input.txt", "r")

poly = f.readline().strip()
rules = {}
f.readline()
for x in f: 
    x1, x2 = x.strip().split(" -> ")
    rules[x1] = [x2, 0, [x1[:1] + x2, x2 + x1[1:]]]
#print(rules)

dict = matchRules(poly, rules, 40)
min = dict[poly[0]]
max = dict['B']
for key in dict:
    if dict[key] == 0: continue
    if dict[key] < min: min = dict[key]
    if dict[key] > max: max = dict[key]

print(max - min)
