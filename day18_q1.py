import copy
import math
#if any number greater than 10, 
def split(l):
    for i in range(2): 
        if isinstance(l[i], list): 
            b = split(l[i])
            if b == True: return b
        #not list
        elif l[i] >= 10: 
            newList = []
            newList.append(math.floor(l[i] / 2))
            newList.append(math.ceil(l[i] / 2))
            j = l.index(l[i])
            l[j] = newList
            return True
    return False



#explode: for each element in your list, check to see if it is a list
#if it is a list, check to see if depth is 4
#if depth is 4 that means that means we need to add the left element to the left and the right element to the right
#if it is a list and depth is not 4, recurse
def explode(l, depth, indexTracker, originalList):
    for i in range(2): 
        if len(indexTracker) < depth: 
            indexTracker.append(i)
        else: indexTracker[depth - 1] = i
        
        if isinstance(l[i], list) and depth >= 4: 
                newL = []
                if isinstance(l[0], list): newL = l[0]
                else: newL = l[1]
                addLeft(originalList, indexTracker, newL[0])
                addRight(originalList, indexTracker, newL[1])
                l[i] = 0
                return True


        elif isinstance(l[i], list): 
            b = explode(l[i], depth + 1, indexTracker, originalList)
            if b: return b

        

    return False #nothing to explode


def recurseDown(l, indexTracker):
    if len(indexTracker) == 0: return l
    return recurseDown(l[indexTracker[0]], indexTracker[1:])


def rightmostNonList(l, num):
    if isinstance(l[-1], list): 
        rightmostNonList(l[-1], num)
    else: l[-1] += num

def leftmostNonList(l, num):
    if isinstance(l[0], list): 
        leftmostNonList(l[0], num)
    else: l[0] += num

def addLeft(l, indexTracker, num):
    # go down to 1
    for i in range(len(indexTracker) - 1, -1, -1):
        if indexTracker[i] > 0: 
            newList = recurseDown(l, indexTracker[:i])
            #find rightmost non-list element in newList[i - 1
            if isinstance(newList[0], list):
                    rightmostNonList(newList[0], num)
            else: newList[0] += num

            break         


#find leftmost element in right list
def addRight(l, indexTracker, num):
    for i in range(len(indexTracker) - 1, -1, -1):
        if indexTracker[i] == 0: 
            newList = recurseDown(l, indexTracker[:i])
            if isinstance(newList[1], list):
                    leftmostNonList(newList[1], num)
            else: newList[1] += num

            break

#given pair of two snailfish nums
def addition(num1, num2):   
    num = [num1, num2]
    while True: 
        indexTracker = [0]
        
        if explode(num, 1, indexTracker, num): 
            continue
        
        if not split(num):
            break
    return num

def magnitude(l):
    num1 = 0
    num2 = 0
    if isinstance(l[0], list): num1 = magnitude(l[0])
    else: num1 = l[0]
    if isinstance(l[1], list): num2 = magnitude(l[1])
    else: num2= l[1]
    return (3 * num1) + (2 * num2)

    
nums = [
[[[[2,5],4],[[1,0],[8,3]]],[[2,[2,4]],[1,[3,3]]]],
[[[2,2],[[4,3],3]],[[[8,6],3],[3,7]]],
[[[9,[4,1]],[9,0]],[6,[6,0]]],
[[[3,9],[[4,4],[2,5]]],[[9,[8,4]],8]],
[[[[0,0],9],[[9,3],[8,2]]],[2,[1,3]]],
[[[8,4],6],[[5,1],[3,6]]],
[[[6,[7,6]],[[2,6],5]],[[6,4],2]],
[[1,[9,7]],[[[5,9],[9,5]],[[7,0],1]]],
[[[[5,8],[9,4]],[[9,3],[7,8]]],8],
[[[0,9],[[6,0],7]],[[[7,7],6],[[9,7],[0,4]]]],
[[[[4,3],[9,5]],[7,[7,3]]],[[[2,8],9],4]],
[[7,5],[8,1]],
[[4,6],[[[0,6],6],[7,4]]],
[[[1,8],[[1,4],[1,6]]],[3,4]],
[[[6,5],[4,[7,3]]],[[[0,1],[8,4]],[4,8]]],
[[5,1],[9,[9,[3,3]]]],
[[[[7,0],[2,5]],1],[9,[[2,7],[4,4]]]],
[[[[5,8],8],0],[8,[1,[2,5]]]],
[8,[[5,4],7]],
[[[9,8],[6,7]],[[2,[2,6]],[9,6]]],
[[[[2,3],7],6],[[8,6],3]],
[[[8,[7,2]],3],[[[3,9],4],[6,8]]],
[9,[[[6,7],[6,0]],[[3,9],8]]],
[[[7,7],[4,7]],[[[9,8],9],[9,[2,4]]]],
[[[[5,0],1],[4,[4,8]]],[9,[6,7]]],
[[[[9,2],5],[1,[5,8]]],[[9,[0,1]],[3,8]]],
[[[5,[2,5]],8],[2,[0,[9,3]]]],
[[7,[[8,4],[8,4]]],4],
[[[[3,3],4],[[0,0],[5,5]]],[4,5]],
[[[[9,3],[9,3]],2],[5,3]],
[[[9,5],[1,4]],[[7,1],[3,[6,5]]]],
[8,[[[1,1],[0,1]],[9,[3,6]]]],
[[[[4,4],7],[0,3]],[1,5]],
[[[3,[0,8]],8],[5,[7,5]]],
[[[[9,6],2],7],[[5,[3,7]],0]],
[4,9],
[[[5,[1,3]],[[9,5],6]],[[[7,9],5],3]],
[[[[3,9],[7,2]],[5,[8,8]]],[1,9]],
[[[[7,8],8],[[9,0],[5,1]]],[6,[[1,0],[3,3]]]],
[[[[5,8],1],[[8,6],[2,9]]],[[5,1],6]],
[[1,7],[[5,[3,2]],4]],
[[[[3,1],2],[0,8]],[3,[4,6]]],
[[9,6],[0,[[5,2],[1,1]]]],
[[[[1,8],8],[[9,0],3]],[[6,[2,8]],[[6,4],[6,0]]]],
[[7,[[3,2],[9,0]]],[[[3,2],[2,8]],[[5,5],[9,2]]]],
[[[[2,5],[3,1]],[7,[9,6]]],[[[7,0],7],[2,[9,1]]]],
[[[[1,6],9],[1,[6,5]]],[[8,[4,1]],6]],
[[[7,[4,6]],[[2,7],[6,6]]],[8,0]],
[[9,7],[[[0,7],5],[[1,4],[1,3]]]],
[[[1,[8,2]],[[0,6],[9,0]]],8],
[[[4,0],[7,[3,3]]],[9,6]],
[0,[[[6,9],7],[[0,6],1]]],
[5,[[4,3],[[8,3],[5,7]]]],
[[9,0],[0,[[7,8],[1,8]]]],
[[[[4,3],[5,6]],2],[[2,3],1]],
[4,[[9,9],[[1,8],[9,2]]]],
[[[[6,9],5],1],[[[7,4],[8,1]],3]],
[[8,[5,[2,6]]],[[[2,7],6],[6,0]]],
[[[[6,8],8],6],[[[5,7],2],[[6,5],[3,0]]]],
[[[1,[2,5]],3],[5,[4,[6,6]]]],
[[[[4,9],8],1],[9,0]],
[[1,[0,[5,7]]],[[1,[5,9]],[[3,2],[1,7]]]],
[[[[2,9],[2,7]],[[4,2],5]],[[[9,1],[7,2]],[2,[7,5]]]],
[[[[5,7],[8,9]],[5,[7,9]]],[[7,[6,6]],[7,[8,0]]]],
[[[[6,6],[4,6]],[4,[7,8]]],[1,[[5,5],[1,9]]]],
[[[[4,3],8],2],[[9,[4,0]],[8,[7,0]]]],
[[2,[7,5]],[[[0,1],1],[8,[3,5]]]],
[[[4,[4,2]],[[0,4],9]],[1,4]],
[[[5,5],[5,6]],[[0,[4,2]],[[7,8],[5,6]]]],
[2,[[0,[9,1]],[[1,7],[0,0]]]],
[[[5,[4,8]],1],9],
[8,[[2,1],[3,0]]],
[[[[6,5],[1,1]],7],[[[7,5],3],[0,1]]],
[[[[0,3],7],7],[[[4,8],[6,1]],[[6,1],9]]],
[[[[4,8],9],[1,0]],[6,[4,[4,8]]]],
[[[[8,0],[5,1]],6],1],
[[[[6,6],[7,7]],[[4,3],[2,6]]],[[3,5],[[7,0],[7,3]]]],
[[1,[5,8]],[[[3,7],[9,6]],[[4,8],[3,4]]]],
[[[1,5],[8,2]],[[[3,1],5],[4,1]]],
[[[[6,3],5],8],[[9,[3,6]],[[3,5],[6,9]]]],
[[[7,[5,4]],[0,[6,0]]],[[[7,7],[1,1]],[[5,1],7]]],
[[[1,5],[[8,6],0]],5],
[[[[0,8],[6,0]],[[3,0],9]],[[[7,1],2],[4,2]]],
[[[6,[8,7]],[2,[2,0]]],[9,[7,[6,6]]]],
[3,[[7,[4,5]],[[8,5],4]]],
[[[[8,0],[8,3]],[[5,4],[1,6]]],[[0,[8,5]],3]],
[[[7,2],1],[9,[[3,8],4]]],
[[4,[7,[9,9]]],[3,8]],
[[[[7,1],9],[[6,9],[9,6]]],[2,0]],
[[[[6,2],9],[3,[3,9]]],[[8,[3,4]],[3,7]]],
[[4,9],[8,[5,[9,8]]]],
[3,[[9,[9,7]],4]],
[[[[5,9],6],[1,[3,1]]],[4,[1,[3,8]]]],
[[[[7,6],2],3],[[0,[1,8]],[[4,9],[4,3]]]],
[[3,[[8,1],[3,8]]],[[[2,0],[0,8]],[[7,0],9]]],
[[[[9,7],[9,3]],[[5,8],6]],[[[6,2],0],[2,4]]],
[[[8,[9,7]],[[5,1],[1,4]]],3],
[[7,[[5,6],[2,7]]],[[[7,3],0],[1,[0,6]]]],
[[2,[[5,5],2]],[[3,[7,2]],[[7,1],8]]],
[[[[2,4],[6,8]],[0,[7,5]]],[[3,[2,5]],[7,7]]]
]




prev = addition(nums[0], nums[1])
for i in range(2, len(nums)): 
    
    prev = addition(prev, nums[i])

print(prev)
print(magnitude(prev))


