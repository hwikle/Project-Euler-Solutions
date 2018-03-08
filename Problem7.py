from math import sqrt

def isDivisible(n, l):
    i = 0
    
    while i < len(l) and l[i] < sqrt(n) + 1:
        if n % l[i] == 0:
            return True
        i += 1
        
    return False

def nthPrime(n):
    primes = []
    i = 2

    while len(primes) < n:
        if not isDivisible(i, primes):
            primes.append(i)
            #print(primes)
        i+= 1
        
    return primes[-1]
        
if __name__ == '__main__':
    print(nthPrime(6))
    print(nthPrime(10001))
