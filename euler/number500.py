from primesieve import *
from heapq import *

target = 500500

list = generate_n_primes(target)
#print(list)
#print(len(list))

heapify(list)
n=1
for i in range(target):
    val = heappop(list)
    n*=val
    heappush(list, val**2)
    n%=500500507

print(n)

