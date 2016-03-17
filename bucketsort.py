arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
def bucketSort(arr, size):
    buckets = [[] for i in range(size)]

    # 버킷에 담는다
    for i in range(len(arr)):
        num = size*arr[i]
        buckets[int(num)].append(arr[i])

    output = []
    # sort 한다
    for i in range(len(buckets)):
        insertionSort(buckets[i])

    # buckets 를 더하고 출력한다
    for i in range(len(buckets)):
        while len(buckets[i]) > 0:
            output.append(buckets[i].pop(0))

    return output


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

print(bucketSort(arr, len(arr)))