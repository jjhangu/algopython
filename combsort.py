arr = [8, 4, 1, 56, 3, -44, 23, -6, 28, 0]

def combsort(arr):

    gap = len(arr)
    swapped = True

    while gap !=1 or swapped:
        gap= int(gap//1.3)
        if gap==0:
            gap =1

        swapped = False
        for i in range(0, len(arr)-gap):
            if arr[i] > arr[i+gap]:
                swap(arr, i , i+gap)
                swapped = True
                print(arr)

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

combsort(arr)

print(arr)