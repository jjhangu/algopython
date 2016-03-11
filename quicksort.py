arr = [5, 2, 6, 1, 3, 4]

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr, left, right):
    print("")
    position = left
    compare = 0 # 0 인경우 ascending, 1, descending compare

    while True:
        print(arr, "l:",  left,"r:", right, " : p : ", position)
        if compare ==0: ## 오름차순
            if position == right:
                return position

            if arr[position] > arr[right]: #변경해야하는 타이밍

                swap(arr, position, right)

                compare = 1 # descending order change
                position = right
                left = left + 1


            else :
                right = right-1
        else : # 내림차순

            if position == left:
                return left

            if arr[position] < arr[left]: #변경해야하는 타이밍

                swap(arr, position, left)

                compare = 0 # asecnding order change
                position = left
                right= right- 1

            else: # 내림차순이면서 변경해야하는 경우가 아닌경우
                left = left+1


def quicksort(arr, left, right):
    print("")

    if right>left:
        position = partition(arr, left, right)
        print("position, ", position)
        quicksort(arr, left, position-1)
        quicksort(arr, position+1, right)

quicksort(arr, 0, len(arr)-1)

print(arr)


