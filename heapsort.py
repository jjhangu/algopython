import math

arr = [4, 10, 3, 5, 1]

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def createMaxHeap(arr):
    print(arr);

    startIndex = math.floor(len(arr)//2);
    while startIndex > -1:
        maxHeapify(arr, startIndex)
        startIndex = startIndex-1

def maxHeapify(arr, startIndex):

    largest = startIndex
    left = (startIndex * 2) +1
    right = (startIndex * 2) +2

    if left < len(arr) and arr[startIndex] < arr[left]:
        largest = left

    if right < len(arr) and  arr[startIndex] < arr[right]:
        largest = right

    if largest != startIndex:
        if arr[left] >  arr[right]:
            largest =left
        else:
            largest = right
        swap(arr, startIndex, largest)
        maxHeapify(arr, largest)

createMaxHeap(arr)
print(arr)