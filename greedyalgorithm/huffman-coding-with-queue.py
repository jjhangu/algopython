#this functions for huffman sorted algorithm

import random

dic = {}
class MinHeapNode:
    def setNode(self, left, right, freq, char):
        self.left = left
        self.right = right
        self.freq = freq
        self.char = char
        return self

def huffmanCoding(arr, freq):
    queueA =[]
    queueB = []

    for i in range(len(arr)):
        queueA.append(MinHeapNode().setNode(None, None , freq[i], arr[i]))
        print(queueA[i].freq, queueA[i].char)

    # while(len(heapArr)>1):
    #    left = heapArr.pop(0)
    #    right = heapArr.pop(0)
    #    insertionSort(heapArr, MinHeapNode().setNode(left, right, left.freq+right.freq, left.char + right.char))

    while (len(queueA) == 0 and len(queueB) == 1) ==False:
        left = pickMin(queueA, queueB)
        right = pickMin(queueA, queueB)

        top = MinHeapNode().setNode(left, right, left.freq+right.freq, left.char + right.char)
        queueB.append(top) # enqueue

    rootheap = queueB.pop(0)

    return rootheap


def pickMin(queueA, queueB):

    if len(queueB) == 0:
        return queueA.pop(0)

    if  len(queueA) == 0:
        return queueB.pop(0)

    if queueA[0].freq < queueB[0].freq:
        return queueA.pop(0)
    else:
        return queueB.pop(0)

def printHeap(heap, str):
    if heap.left != None:
        printHeap(heap.left, str + '0')

    if heap.right !=None:
        printHeap(heap.right, str + '1' )

    if heap.left == None:
        print(heap.char, str)
        dic[heap.char] = str

'''
this functions for test
'''

def makeNewString(arr, freq):

    freqcopy = freq[:]
    arrcopy = arr[:]
    strval = ''

    while len(freqcopy) >0:
        number = random.randrange(0,len(freqcopy))
        freqcopy[number] = freqcopy[number]-1
        strval = strval + arrcopy[number]
        if freqcopy[number] == 0:
            freqcopy.pop(number)
            arrcopy.pop(number)
    return strval

def endcoding(str):
    strval = ''
    for i in range(len(str)):
        strval = strval + dic[str[i]]

    return strval

def huffmandecode(rootheap, strvalencoded):

    index = 0;
    orgstr = '';

    while index < len(strvalencoded):
        str = getchar(rootheap, index, strvalencoded)
        index = index + len(dic[str])
        orgstr = orgstr + str
    return orgstr

def getchar(rootheap, index, strvalencoded):
    if rootheap.left == None:
        return rootheap.char

    number = int(strvalencoded[index])
    if number ==0:
        return getchar(rootheap.left, index+1, strvalencoded)

    if number ==1:
        return getchar(rootheap.right, index+1, strvalencoded)

arr = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]
rootheap = huffmanCoding(arr, freq)

printHeap(rootheap, '')

strval  = makeNewString(arr, freq)
print("org     ", strval)

strvalencoded = endcoding(strval)
print("encoded ",strvalencoded)

orgencoded = huffmandecode(rootheap, strvalencoded)
print("decoded ", orgencoded)