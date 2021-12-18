target_x = (102, 157)
target_y = (-90, -146)

def hitsTarget(pos, v, tx, ty):
    cur_x  = pos[0]
    cur_y = pos[1]

    vx = v[0]
    vy = v[1]

    #check if on target
    if (cur_x >= tx[0] and cur_x <= tx[1]) and cur_y <= ty[0] and cur_y >= ty[1]:
        return True

    #check case where position is to the left of the target
    if cur_x < tx[0] and vx <= 0: return False

    #check case where pos is to the right of target
    if cur_x > tx[1] and vx >=0: return False

    #probe is directly above target with a 0 x velocity, meaning that it will reach target eventually
    #if cur_x >= tx[0] and cur_x <= tx[1] and cur_y > ty[0] and vx == 0: return True
    if cur_x >= tx[0] and cur_x <= tx[1] and cur_y < ty[1] and vy <= 0 : return False

    cur_x += vx
    cur_y += vy

    if vx > 0: vx -= 1
    elif vx < 0: vx += 1
    vy -= 1

    return hitsTarget((cur_x, cur_y), (vx, vy), tx, ty)

def factorial(n):
    val = n 
    for i in range(n - 1, 0, -1): 
        val += i
    return val

def findMin(x):
    for i in range(x): 
        if factorial(i) >= x: return i

def findMaxHeight(v):
    x = 0
    y = 0
    vx = v[0]
    vy = v[1]
    prev_y = y
    while(1):
        x += vx
        y += vy
        if y <= prev_y: return prev_y
        prev_y = y
        if vx > 0: vx -= 1
        elif vx < 0: vx += 1
        vy -= 1


print(hitsTarget((0, 0), (23, 102), target_x, target_y))


velocities = []


min_x = findMin(target_x[0])
min_y = target_y[1]
max_y = target_y[1]
for i in range(400):
    t = hitsTarget((0, 0), (min_x, min_y), target_x, target_y)
    if t: max_y = min_y
    min_y += 1
    


print(min_x, max_y)
print(findMaxHeight((min_x, max_y)))
