def elimMultiples(l):
    """Eliminates multiples from a list. Assumes the list is sorted."""
    print(l)
    result = [l[-1]]
    print(result)

    for i in range(len(l) - 1, 0, -1):
        print('i: %d' % i)
        for j in range(i - 1, 0, -1):
            print('j: %d' % j)
            
            if l[i] != l[j] == 0:
                result.append(l[j])
                print(result)

    return result
    
def isDivisible(x, n):
    """Determines if a number x is divisible by the numbers 1 through n"""
    denoms = [i for i in range(1, n+1)]

    denoms= elimMultiples(denoms)
    
    for d in denoms:
        if x % d != 0:
            return False

    return True

def smallestDiv(n):
    """Returns the smallest number divisible by each of the numbers 1 to n"""
    i = 1
    foundIt = False

    while not foundIt:
        if isDivisible(i, n):
            return i
        i += 1

if __name__ == '__main__':
    print(elimMultiples([2*i for i in range(1, 10)]))
    #print(smallestDiv(10))
    #print(smallestDiv(20))
        
