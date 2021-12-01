#returns number of sums that are larger than the previous sum
#start at 3, add up the three before it
#go to 4, add up the 3 before it, and compare
def numLargerSums(vals):
    count = 0    
    for i in range(3, len(vals)):
        sum1 = vals[i - 3] + vals[i - 2] + vals[i - 1]
        sum2 = vals[i - 2] + vals[i - 1] + vals[i]
        
        if sum2 > sum1: count += 1
        
    return count
        
f = open("input.txt", "r")
vals = []
for x in f: 
    vals.append(int(x))
    
print(numLargerSums(vals))