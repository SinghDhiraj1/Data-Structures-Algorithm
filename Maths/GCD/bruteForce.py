"""
 Brute Force
"""
n1 = 9
n2 = 12

gcd = 1
for i in range(min(n1, n2), 1, -1):
    if (n1%i==0 and n2%i==0):
        gcd = i
        break

print(f"GCD of {n1} and {n2} is {gcd}")