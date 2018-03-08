def FibonacciUnder(n):
    if n <= 0:
        fibs = []
    elif n == 1:
        fibs = [0]
    else:
        fibs = [0, 1]
        nextFib = 1
        
        while nextFib < n:
            fibs.append(nextFib)
            nextFib = fibs[-1] + fibs[-2]
        
    return fibs

def sumEvenFibs(n):
    s = 0
    
    for f in FibonacciUnder(n):
        if f % 2 == 0:
            s += f

    return s

if __name__ == '__main__':
    print(sumEvenFibs(4000000))
