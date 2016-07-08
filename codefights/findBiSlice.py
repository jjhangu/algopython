def findBiSlice(arr):
    p = 0
    o = 0
    a =-1
    b =-2
    c =1
    m = 0

    for i in range(1, len(arr)):
        if abs(arr[i]-arr[i-1])<2:
            if o ==0:

                a = arr[i]
                b = arr[i-1]

                if a== b:
                    o=1
                else:
                    o=2
                c=c+1
            elif o==1:
                if a== arr[i]:
                    b= arr[i]
                else:
                    b= arr[i]
                o=2
                c=c+1
            else:
                if arr[i] ==a or arr[i] ==b:
                    c=c+1
        else:
            m= max(m, c)
            c=1
            o=0

    m= max(m, c)
    return m


print(findBiSlice([3, 3, 2, 2]))


