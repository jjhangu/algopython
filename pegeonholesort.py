arr = [8, 3, 2, 7, 4, 6, 8]

def pegeonhole(arr):
    #max num
    maxval = max(arr)
    minval = min(arr)

    size = maxval -minval+1
    hole = [[] for i in range(size)]

    #set build pegeonhole
    for i in range(len(arr)):
        hole[arr[i]-minval].append(arr[i])

    print(hole)
    output = []
    for i in range(len(hole)):
        while len(hole[i]) > 0:
            output.append(hole[i].pop(0))

    return output

arr = pegeonhole(arr)
print(arr)