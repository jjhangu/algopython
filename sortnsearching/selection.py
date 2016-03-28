arr = [5,2,3,7,1,4]
def selectionSort(arr):
    for i in range(len(arr)-1):
        print(i)
        minimum = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < minimum:
                minimum = arr[j]
                swap(arr, i, j)
                print(arr);

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def selectionSortOnlyOneSwap(arr):
    for i in range(len(arr)-1):
        print(i)

        minimum = arr[i]
        minposition = i
        for j in range(i+1, len(arr)):
            if arr[j] < minimum:
                minimum = arr[j]
                minposition = j

        if minposition != i:
            swap(arr, i, minposition)

        print(arr)

selectionSort(arr)
print(arr)
print("only one time swap")

arr = [5,3,2,7,1,4]
print(arr)
selectionSortOnlyOneSwap(arr)


