f = open("input.txt", "r")
inp = []
for x in f:
    inp.append([x.strip(), []])

for x in inp:
    for c in x[0]:
        if c == '(' or c == '[' or c == '{' or c == '<':
            x[1].append(c)
        else: 
            if c == ')' and x[1][-1] == '(': 
                x[1].pop()
                continue
            elif c == ')': 
                x[1] = -1
                break
            if c == ']' and x[1][-1] == '[': 
                x[1].pop()
                continue
            elif c == ']': 
                x[1] = -1
                break  
            if c == '}' and x[1][-1] == '{': 
                x[1].pop()
                continue
            elif c == '}': 
                x[1] = -1
                break  
            if c == '>' and x[1][-1] == '<': 
                x[1].pop()
                continue
            elif c == '>': 
                x[1] = -1
                break  


inp = [i for i in inp if i[1] != -1]

completes = []
for e in inp:
    complete = ''
    e[1].reverse()
    for c in e[1]:
        if  c == '{': complete += '}'
        elif c == '(': complete += ')'
        elif c == '[': complete += ']'
        elif c == '<': complete += '>'
    completes.append(complete)

totals = []
for e in completes: 
    total = 0
    for c in e: 
        total *= 5
        if c == ')': total += 1
        elif c == ']': total += 2
        elif c == '}': total += 3
        elif c == '>': total += 4
    totals.append(total)

totals.sort()        

med = len(totals) / 2
print(totals[med])