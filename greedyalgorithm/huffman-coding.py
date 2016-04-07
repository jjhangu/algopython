class MinHeapNode:
    def setNode(self, left, right, freq, char):
        self.left = left
        self.right = right
        self.freq = freq
        self.char = char
        return self

def huffmanCoding(arr, freq):
    heapArr = []

    for i in range(len(arr)):
        heapArr.append(MinHeapNode().setNode(None, None , freq[i], arr[i]))
        print(heapArr[i].freq, heapArr[i].char)

    while(len(heapArr)>1):
       left = heapArr.pop(0)
       right = heapArr.pop(0)
       insertionSort(heapArr, MinHeapNode().setNode(left, right, left.freq+right.freq, left.char + right.char))

    rootheap= heapArr.pop()

    printHeap(rootheap, '')

def printHeap(heap, str):
    if heap.left != None:
        printHeap(heap.left, str + '0')

    if heap.right !=None:
        printHeap(heap.right, str + '1' )

    if heap.left == None:
        print(heap.char, str)

def insertionSort(heapArr, heap):
    index = len(heapArr)
    for i in range(len(heapArr)):
        if heap.freq < heapArr[i].freq:
           index  = i
           break

    heapArr.insert(index, heap)

arr = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]
huffmanCoding(arr, freq)