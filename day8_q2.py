#[ [[unique vals], [output]]  ]
f = open("input.txt", "r")
inp = []
for x in f: 
    a = x.strip().split("|")
    inp.append([a[0].strip().split(" "), a[1].strip().split(" ")])

def findVals(uniques, output): 
    #contains sorted string of each number
    arr = ["", "", "", "", "", "", "", "", "", ""]

    for i in range(len(uniques)):
        if len(uniques[i]) == 2 or len(uniques[i]) == 4 or len(uniques[i]) == 3 or len(uniques[i]) == 7:
            newStr = sorted(uniques[i])
            newStr = "".join(newStr)
            #newStr = uniques[i]
            index = 0 
            if len(uniques[i]) == 2: index = 1
            elif len(uniques[i]) == 4: index = 4
            elif len(uniques[i]) == 3: index = 7
            elif len(uniques[i]) == 7: index = 8
            arr[index] = newStr

    for i in range(len(uniques)):
        newStr = sorted(uniques[i])
        newStr = "".join(newStr)
        #newStr = uniques[i]
        if len(uniques[i]) == 5: 
            #way to check if has characters in common
            if arr[1][0] in newStr and arr[1][1] in newStr: arr[3] = newStr 
            elif numInCommon(arr[4], newStr) == 2: arr[2] = newStr
            else: arr[5] = newStr

        if len(newStr) == 6: 
            if numInCommon(newStr, arr[7]) == 2: arr[6] = newStr
            elif numInCommon(newStr, arr[4]) == 4: arr[9] = newStr
            else: arr[0] = newStr

    result = ""
    for s in output: 
        s_sorted = sorted(s)
        s_sorted = "".join(s_sorted)
        ind = arr.index(s_sorted)
        result += str(ind)
    
    return int(result)
def numInCommon(str1, str2):
    total = 0
    for i in str1:
        for j in str2: 
            if i == j: total += 1
    return total


sum = 0 
for entry in inp: 
    sum += findVals(entry[0], entry[1])

print(sum)