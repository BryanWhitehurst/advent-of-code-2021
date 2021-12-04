import copy
def ogr(vals):
    while(len(vals) != 1): 
        for i in range(len(vals[0])):
            cur = []
            one_cnt = 0
            zero_cnt = 0
            for x in vals: 
                if x[i] == '1': one_cnt += 1
                else: zero_cnt += 1
            if one_cnt >= zero_cnt: 
                for x in vals: 
                    if x[i] == '1': cur.append(x)
            else: 
                for x in vals: 
                    if x[i] == '0': cur.append(x)
            vals = cur
            if(len(vals) == 1): return int(vals[0], 2)

#CO2 scrubber rating
def csr(vals):
    while(len(vals) != 1): 
        for i in range(len(vals[0])):
            cur = []
            one_cnt = 0
            zero_cnt = 0
            for x in vals: 
                if x[i] == '1': one_cnt += 1
                else: zero_cnt += 1
            if one_cnt >= zero_cnt: 
                #remove everything with 0 in current position
                for x in vals: 
                    if x[i] == '0': cur.append(x)
            else: 
                #remove everything with 1 in current position
                for x in vals: 
                    if x[i] == '1': cur.append(x)
            vals = cur
            if(len(vals) == 1): return int(vals[0], 2)

f = open("input.txt", "r")
vals = []
for x in f: 
    vals.append(x.strip())

v1 = ogr(copy.copy(vals))
v2 = csr(vals)
print(v1 * v2)