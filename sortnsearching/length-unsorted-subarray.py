arr =[10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]

def sort(arr):

    # 처음부터시작한다
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            s = i
            break

    for j in range((len(arr)-1), 0, -1):
        if arr[j] < arr[j-1]:
            e = j
            break

    min = arr[s]
    max = arr[s]

    for i in range(s+1, e+1):
        if arr[i]> max:
            max = arr[i]
        if arr[i]<min:
            min = arr[i]

    for i in range(0, s):
        if arr[i]>min :
            s = i

    for i in range((len(arr)-1), e, -1):
        if arr[i]<max :
            e = i

    print(s, e)

sort(arr)

