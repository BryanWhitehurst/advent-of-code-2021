f = open("input.txt", "r")

inp = f.readline().strip()
binary = ''
for c in inp: 
    if c == '0':  binary += '0000'
    elif c == '1': binary += '0001'
    elif c == '2': binary += '0010'
    elif c == '3': binary += '0011'
    elif c == '4': binary += '0100'
    elif c == '5': binary += '0101'
    elif c == '6': binary += '0110'
    elif c == '7': binary += '0111'
    elif c == '8': binary += '1000'
    elif c == '9': binary += '1001'
    elif c == 'A': binary += '1010'
    elif c == 'B': binary += '1011'
    elif c == 'C': binary += '1100'
    elif c == 'D': binary += '1101'
    elif c == 'E': binary += '1110'
    elif c == 'F': binary += '1111'

print(binary)
#print(len(binary))
#first three bits of every packet represent version number 
#next three encode type ID
#if type id == 100, then the following bits are groups of 5 bits: if first bit is 1, then
#there will be another group of 5, if first bit is 0, then there will not be another group of 5
#if typeID != 100, then next bit (length type id)
        #0 indicates that the next 15 bits indicate remaining length
        #1 indicates next 11 bits is number of subpackets there are


values = []

def getLength(binary):
    values.append(int(binary[:3], 2))
    type_id = binary[3:6]
    
    if type_id == '100':
        i = 6
        value = ''
        while(1):
            substr = binary[i: i + 5:]
            i += 5
            first = substr[0]
            substr = substr[1:]
            value += substr
            if first == '0': break
        return (i, int(value, 2))
     
    else: 
        vals = []
        length_id = binary[6]
        cur_index = 0
        #next 15 bits indicate remaining length of subpackets
        if length_id == '0': 
            remaining_length = binary[7: 22:]
            remaining_length = int(remaining_length, 2)
            cur_index = 22
            while cur_index < 22 + remaining_length:
                j = getLength(binary[cur_index:])
                cur_index += j[0]
                vals.append(j[1]) 
            
        else: 
            numPackets = binary[7: 18:]
            numPackets = int(numPackets, 2)
            cur_index = 18
            for i in range(numPackets): 
                j  = getLength(binary[cur_index:]) #gets the value of each subpacket
                cur_index += j[0]
                vals.append(j[1])
        

        if type_id == '000':
            sum = 0
            for v in vals:
                sum += v
            return (cur_index, sum)
        elif type_id == '001':
            prod = 1
            for v in vals: 
                prod *= v
            return (cur_index, prod)
        elif type_id == '010':
            return (cur_index, min(vals))
        elif type_id == '011':
            return (cur_index, max(vals))
        elif type_id == '101':
            gt = 0
            if vals[0] > vals[1]: gt = 1
            return(cur_index, gt)
        elif type_id == '110':
            lt = 0 
            if vals[0] < vals[1]: lt = 1
            return (cur_index, lt)
        elif type_id == '111':
            eq = 0
            if vals[0] == vals[1]: eq = 1
            return (cur_index, eq)

a = getLength(binary)
print(a[1])
#print(values)
total = 0
for v in values:
    total += v

    