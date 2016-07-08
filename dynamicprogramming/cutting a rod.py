def cuttingRod(s, arr):

    m = arr[s-1]
    for i in range(1,int(s/2)+1):
        left=  i
        right =s-i
        val = cuttingRod(left, arr) + cuttingRod(right,arr)
        print(left, right, val)
        m= max(m, val )

    return m

def cuttingRodDP(s, arr):

    m = [0 for i in range(len(arr)+1)]
    for i in range(1, len(arr)+1):
        m[i]= arr[i-1]


    maxValue =0

    for i in range(1, len(arr)+1):
        for j in range(1,i+1):
           maxValue =  max(maxValue, m[j] + m[i-j])
        m[i] = maxValue
        print(m)

    return maxValue


arr= [ 1 ,  5,   8 ,  9 , 10,  17,  17,  20]
print(cuttingRod(len(arr), arr))

print(cuttingRodDP(len(arr), arr))

