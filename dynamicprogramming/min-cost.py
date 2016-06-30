cost = [ [1, 2, 3],[4, 8, 2],[1, 5, 3] ]
val = [ [0 for col in range(3)] for row in range(3)]

for i in range(len(cost)):
    print(cost[i][1])


val[0][0] = cost[0][0]

# row setting
for i in range (3):
    val[i][0] = cost[i][0] + val[i-1][0]
    val[0][i] = cost[0][i] + val[0][i-1]

for i in range(1 ,3):
    for j in range(1, 3):
        val[i][j] = cost[i][j] + (min(val[i-1][j], val[i][j-1], val[i-1][j-1]))

for i in range(len(val)):
    for j in range(len(val)):
        print(val[i][j], end="")
    print()