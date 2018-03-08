def maxAdjProduct(a, n, row, col):
    """Calculates the maximum of the eight adjacent products of n factors
    around the number in the row and column given in the
    two-dimensional array a. Returns an int."""
    largest = 0

    #Calculate up-product
    p = a[row][col]

    for i in range(1, n + 1):
        try:
            p *= a[row - i][col]
        except IndexError:
            break

    if p > largest:
        largest = p

    #Calculate right-product
    p = a[row][col]

    for i in range(1, n + 1):
        try:
            p *= a[row][col + i]
        except IndexError:
            break

    if p > largest:
        largest = p
        
    #Calculate down-product
    p = a[row][col]

    for i in range(1, n + 1):
        try:
            p *= a[row + i][col]
        except IndexError:
            break

    if p > largest:
        largest = p
        
    #Calculate left-product
    p = a[row][col]

    for i in range(1, n + 1):
        try:
            p *= a[row][col - i]
        except IndexError:
            break

    if p > largest:
        largest = p

    #Calculate up-right-product
    p = a[row][col]

    for i in range(1, n + 1):
        try:
            p *= a[row - i][col + i]
        except IndexError:
            break

    if p > largest:
        largest = p

    #Calculate down-right-product
    p = a[row][col]

    for i in range(1, n + 1):
        try:
            p *= a[row + i][col + i]
        except IndexError:
            break

    if p > largest:
        largest = p

    #Calculate down-left-product
    p = a[row][col]

    for i in range(1, n + 1):
        try:
            p *= a[row + i][col - i]
        except IndexError:
            break

    if p > largest:
        largest = p

    #Calculate up-left-product
    p = a[row][col]

    for i in range(1, n + 1):
        try:
            p *= a[row - i][col - i]
        except IndexError:
            break

    if p > largest:
        largest = p

    return largest

def largestGridProd(a, n):
    """Calculates the largest adjacent product of n factors
    in a two-dimensional array a."""
    largest = 0
    
    for row in range(len(a) - 1):
        for col in range(len(row) - 1):
            p = maxAdjProd(a, n, row, col)
            if p > largest:
                largest = p

    return p
            
