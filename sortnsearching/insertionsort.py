arr = [5,2,3,7,1,4]

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def insertionSort(arr):
    for i in range(1, len(arr)):
        index= i
        print("index : " + str(i))
        while index!=0:
            if arr[index] < arr[index-1]:
                temp = arr[index]
                arr[index]= arr[index-1]
                arr[index-1] = temp
                index = index-1
                print(arr)
            else :
                break

insertionSort(arr)
print(arr)







