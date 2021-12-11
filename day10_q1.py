f = open("input.txt", "r")
inp = []
for x in f:
    inp.append(x.strip())

illegals = []
for x in inp:
    stack = []
    for c in x:
        if c == '(' or c == '[' or c == '{' or c == '<':
            stack.append(c)
        else: 
            if c == ')' and stack[-1] == '(': 
                stack.pop()
                continue
            elif c == ')': 
                illegals.append(c)
                break
            if c == ']' and stack[-1] == '[': 
                stack.pop()
                continue
            elif c == ']': 
                illegals.append(c)
                break  
            if c == '}' and stack[-1] == '{': 
                stack.pop()
                continue
            elif c == '}': 
                illegals.append(c)
                break  
            if c == '>' and stack[-1] == '<': 
                stack.pop()
                continue
            elif c == '>': 
                illegals.append(c)
                break  

total = 0
for c in illegals: 
    if c == ')': total += 3
    elif c == ']': total += 57
    elif c == '}': total += 1197
    elif c == '>': total += 25137
print(total)