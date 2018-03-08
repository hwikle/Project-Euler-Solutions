def smallestDiv(n):
    """Returns the smallest number divisible by each of the numbers 1 to n"""
    i = 1
    foundIt = False
    
    while not foundIt:
        divisible = True
        j = 2
        
        while divisible and j <= n:
            if i % j != 0:
                divisible = False
                i += 1
                #if i % 100 == 0:
                    #print('i: ' + str(i))

            if j == n:
                foundIt = True

            j += 1
            #print('j: ' + str(j))

    return i

if __name__ == '__main__':
    print(smallestDiv(10))
    #print(smallestDiv(20))
        
