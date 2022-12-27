from math import ceil as cl
from math import sqrt as sr

def isPrime(num):
    if (num < 2):
        return False
    if (num == 2):
        return True
    for x in range(2, cl(sr(num)) + 1):
        if (num % x == 0):
            return False
    return True

def getPrimesList():
    primes = []
    for x in range(2, 10_000):
        if (isPrime(x)):
            primes.append(x)
    return primes

def prod(pf):
    p = 1
    for x in pf:
        p *= x
    return p

def primeFact(primes, num, pf):
    if (isPrime(num)):
        pf.append(num)
        return pf
    if (prod(pf) == num):
        return pf
    for x in primes:
        if (num % x == 0):
            pf.append(x)
            return primeFact(primes, num // x, pf)
            
if __name__ == "__main__":
    primes = getPrimesList()
    print("Give a number less than 10,000 to prime factorize: ")
    num = int(input())
    pf = primeFact(primes, num, [1])
    pf = pf[1:]
    print("Prime factorization of ", num, ": ", pf)

