coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

def find(coins, target):

    list = [];
    for i in reversed(range(len(coins))):
         print(coins[i])
         while target>= coins[i]:
             target = target - coins[i]
             list.append(coins[i])

    return list

list = find(coins, 93 )
print(list)

