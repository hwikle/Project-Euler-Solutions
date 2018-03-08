def sumOfSquares(n):
    total = 0

    for i in range(n + 1):
        total += i * i

    return total

def squareOfSum(n):
    total = 0

    for i in range(n + 1):
        total += i

    return total * total

def differenceOfSquares(n):
    return squareOfSum(n) - sumOfSquares(n)

if __name__ == '__main__':
    print(differenceOfSquares(10))
    print(differenceOfSquares(100))
