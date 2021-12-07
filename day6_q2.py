#more efficient approach: how to get 256
def lanternfish(fish, numD):
    #count of each value
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for f in fish:
        arr[f] += 1
    for d in range(numD):
        #save 0 value, add it to 8's and 6's at the end. 
        temp = arr[0]
        for i in range(1, 9):
            arr[i - 1] = arr[i]
        arr[8] = temp
        arr[6] += temp


    total = 0
    for t in arr:
        total += t
    return total


f = open("input.txt", "r")
inp = map(int, f.read().split(","))

print(lanternfish(inp, 256))
