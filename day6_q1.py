def lanternfish(inp, numDays):
    for j in range(numDays):
        i = len(inp)
        for fish in range(i) :
            if inp[fish] == 0: 
                inp.append(8)
                inp[fish] = 6
            else: 
                inp[fish] -= 1
    return len(inp)
f = open("input.txt", "r")
inp = map(int, f.read().split(","))

print(lanternfish(inp, 256))
