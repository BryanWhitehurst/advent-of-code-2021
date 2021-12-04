#find most common bit in each row of numbers
def findGamma(vals):
    gamma = ''
    print(len(vals[0]) - 2)
    for i in range( len(vals[0])):
        one_cnt = 0
        zero_cnt = 0
        for x in vals:
            if x[i] == '1': one_cnt += 1
            else: zero_cnt += 1
        if one_cnt > zero_cnt: gamma = gamma + '1'
        else: gamma = gamma + '0'
    return gamma
    return int(gamma, 2) 

#flip gamma bits
def findEpsilon(gamma): 
    epsilon = ''
    for c in gamma:
        if c == '0': epsilon += '1'
        else: epsilon += '0'
    return epsilon

"""
def findEpsilon(vals):
    epsilon = ''
    for i in range( len(vals[0])):
        one_cnt = 0
        zero_cnt = 0
        for x in vals:
            if x[i] == '1': one_cnt += 1
            else: zero_cnt += 1
        if one_cnt < zero_cnt: epsilon = epsilon + '1'
        else: epsilon = epsilon + '0'
    return int(epsilon, 2)      
"""      
    
f = open("input.txt", "r")
vals = []
for x in f: 
    vals.append(x.strip())

gamma = findGamma(vals)
epsilon = findEpsilon(gamma)

print(int(gamma, 2) * int(epsilon, 2))