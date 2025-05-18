n = -10400

def reverseNum(n):
    rev = 0
    
    flag = 0
    if n < 0:
        n = -(n)
        flag = 1

    while(n>0):
        lastDigit = n%10
        rev = rev*10 + lastDigit
        n = n//10

    if flag:
            rev = -(rev)
    
    return rev

print(reverseNum(n))
