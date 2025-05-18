import math

n = 18
flag = 0
count = 0
for i in range(2, int(math.sqrt(36))):
    if (n%i) == 0:
        flag = 1
        break

if (flag):
    print("Not a prime number")
else:
    print("Is a prime number")