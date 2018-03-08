def isMultiple(a, n):
    if a % n == 0:
        return True
    return False

def multiplesBelow(n, factors):
    multiples = []

    for i in range(1, n):
        for f in factors:
            if isMultiple(i, f):
                multiples.append(i)
                break

    return multiples

if __name__ == '__main__':
    mults = multiplesBelow(1000, [3,5])
    print(mults)
    print(sum(mults))
