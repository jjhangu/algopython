from primesieve import *

# a^7, a1b3, a1b1c1
"""
The eight divisors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24.
The ten numbers not exceeding 100 having exactly eight divisors are 24, 30, 40, 42, 54, 56, 66, 70, 78 and 88.
Let f(n) be the count of numbers not exceeding n with exactly eight divisors.

You are given f(100) = 10, f(1000) = 180 and f(10^6) = 224427.

Find f(10^12).
"""



num = 10**12
a7= num**(1/7)
total=0
# a^7
primeL= generate_primes(a7)
#print("primeL", primeL)
total+= len(primeL)

print(1 ,">>", total)

# b3a1

primeB3= generate_primes(num**(1/3) )
#print("primeB3", primeB3)

for i in range(len(primeB3)):
    c =0
    print(2, "#", i)
    val = int(num/(primeB3[i]**3))
    if val > primeB3[i] :
        total+= count_primes(val) -1
        #c = count_primes(val) -1

        print(primeB3[i], c)
    elif val == primeB3[i] :
        #c = count_primes(val) -1
        total+=count_primes(val) -1
        print(primeB3[i], c)
    else:
        #c = count_primes(val)
        total+=count_primes(val)
        print(primeB3[i], c)

print(2 ,">>", total)

primePow= generate_primes(num**(1/2))
#print("primePow", primePow);

# a , b, c
for i in range(len(primePow)):
    for j in range(i+1 , len(primePow)):
        val = num/(primePow[i] * primePow[j])

        if val > primePow[j]:
            total += count_primes(val) - count_primes(primePow[j])
        else :
            break

print(generate_primes(100))
print(3 ,">>", total)












