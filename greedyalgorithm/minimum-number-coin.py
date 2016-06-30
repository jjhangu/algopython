from primesieve import *

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

list = generate_primes(10**10)

print(len(list))
print(list[1000000])


