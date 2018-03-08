def sumEratosthenes(n):
    """Calculates the sum of all primes less than n"""
    nums = dict()

    for i in range(2, n):
        nums[i] = 'Prime'

    for i in nums:
        #print('i: %d' % i)
        multiplier = i
        x = i * multiplier
        #print('x: %d' % x)

        while x < n:
            if x in nums:
                nums[x] = 'Composite'
                #nums.remove(x)
                #print('Removed')
            multiplier += 1
            x = i * multiplier
            
            if x % 100 == 0:
                pass
                #print('x: %d' % x)

    print('Sieve finished')
    print('Summing primes...')
    
    total = 0
    
    for n in nums:
        if nums[n] == 'Prime':
            total += n

    return total

if __name__ == '__main__':
    print(sumEratosthenes(10))
    print(sumEratosthenes(2000000))
            
        
        
