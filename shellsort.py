arr = [12, 34, 54, 2, 3]

def shellsort(arr):
    n = len(arr)
    gap = int(n/2)


    while gap > 0 :
        for i in range(gap, n):

            temp = arr[i]

            j = i
            while j>=gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j-= gap

            arr[j] = temp
        gap//=2

shellsort(arr)
print(arr)