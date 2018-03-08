def primeFactors(n):
    facts = []
    nPrime = n
    
    i = 2
    while i <= nPrime:
        if nPrime % i == 0:
            if i not in facts:
                facts.append(i)
            nPrime //= i
            i = 1

        i += 1

    return facts

if __name__ == '__main__':
    print(primeFactors(13195))
    print(max(primeFactors(600851475143)))
