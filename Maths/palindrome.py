n = 13312
temp = n
rev = 0
while (n>0):
    last = n%10
    rev = rev*10 + last
    n = n//10

if rev != temp:
    print("Not a palindrome number")
else:
    print("Number is an palindrome")
