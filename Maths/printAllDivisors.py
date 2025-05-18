import math
n = 36
result = []
# time complexity if O(sqrt(n))
for i in range(1,int(math.sqrt(n))): # also i*i <= n (not work in this loop) is as int(math.sqrt(n))
    if n%i == 0:
        result.append(i)
        if ((n//i) != i):
            result.append(n//i)

# time compleity is O(n log n) 
result.sort()
print(f"All Divisors of {n} are {result}")