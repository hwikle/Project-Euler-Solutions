def isPalindrome(s):
    if len(s) < 2:
        return True
    elif s[0] == s[-1]:
        return isPalindrome(s[1:-1])
    else:
        return False

def nDigitPalindromes(n):
    Max = 0
    
    for i in range(10**n, 10**(n - 1), -1):
        for j in range(10**n, 10**(n - 1), -1):
            if isPalindrome(str(i * j)) and i * j > Max:
                Max = i * j

    return Max

if __name__ == '__main__':
    print(nDigitPalindromes(2))
    print(nDigitPalindromes(3))
