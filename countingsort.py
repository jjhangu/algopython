arr = [1, 4, 1, 2, 9, 5, 2]


def countSort(arr):
    #find max range
    mval =0;
    for i in range(len(arr)):
        mval = max(mval, arr[i])

    # 배열 초기화
    temp = [0]*(mval+1)
    output = [0]*(len(arr))

    # counting
    for i in range(len(arr)):
        temp[arr[i]] =temp[arr[i]] + 1

    print(temp)
    # recounting
    for i in range(1, len(temp)):
        temp[i]= temp[i-1] + temp[i]



    # counting sort
    for i in range(len(arr)):
        output[temp[arr[i]] -1] =  arr[i]
        temp[arr[i]] = temp[arr[i]] -1

    print(temp)
    print(output)

countSort(arr)
