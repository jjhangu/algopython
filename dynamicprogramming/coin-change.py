def count(arr, n):
    table = [[0 for col in  range(n+1)] for row in range(3) ]

    for i in range(n+1):
        table[0][i] = 1;

    for i in range(1, len(arr)):
        for j in range(n+1):
            if arr[i] == j :
                table[i][j] = table[i-1][j] +1
            elif arr[i] > j :
                table[i][j] = table[i-1][j]
            else :
                table[i][j] = table[i-1][j] + table[i][j-arr[i]]

    print(table)


count([1,2,3],  4)

