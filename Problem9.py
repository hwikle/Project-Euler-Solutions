def triplet(n):
    for c in range(3, n - 2):
        for b in range(2, c):
            a = n - b - c
            if a**2 + b**2 == c**2:
                return (a, b, c)
            
if __name__ == '__main__':
    t = triplet(1000)
    product = 1

    for i in t:
        product *= i
        
    print(t)
    print(product)
