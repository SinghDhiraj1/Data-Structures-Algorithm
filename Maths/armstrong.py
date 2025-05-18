n = 321
temp = n
arm = 0

while(n>0):
    last = n%10
    arm = arm + (last**3)
    n = n//10

if arm != temp:
    print("Not an armstrong number")
else:
    print("Armstrong number")