#returns number of vals that are larger than the previous
def numLargerVals(vals):
    count = 0    
    for i in range(1, len(vals)):
        if(vals[i] > vals[i - 1]): count += 1
    return count
        
f = open("input.txt", "r")
vals = []
for x in f: 
    vals.append(int(x))
    
print(numLargerVals(vals))