f = open("input.txt", "r")
inp = []
for x in f: 
    a = x.strip().split("|")
    inp.append(a[1].strip().split(" "))

total = 0
for segment in inp: 
    for str in segment: 
        if len(str) == 2 or len(str) == 4 or len(str) == 3 or len(str) == 7:
            total+= 1
print(total)