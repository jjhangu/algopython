import math

arr = [4, 10, 3, 5, 1]
result = [];

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def createMaxHeap(arr):
    print(arr);

    startIndex = math.floor(len(arr)//2)-1;
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
        if arr[left] < arr[right]:
            largest = right

    if largest != startIndex:

        swap(arr, startIndex, largest)
        maxHeapify(arr, largest)

def heapsort (result, arr):
    while len(arr)>0:
        createMaxHeap(arr)
        print("complete maxheap")
        print(arr)
        ''' result 노드에 추가 '''
        result.append(arr[0])
        '''마지막 노드와 첫번째 노드 교체'''
        if len(arr) != 1:
            arr[0] = arr[len(arr)-1]
        arr.pop()

heapsort(result, arr)

print(result)
