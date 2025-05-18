"""
Euclidean Algorithm
"""
# Time Complexity O(log(min(n1, n2))) Space Complexity O(log(min(n1, n2)))
def euclidean(n1, n2):
    if n2 == 0:
        return n1
    return euclidean(n2, n1 % n2)

# Time Complexity O(log(min(n1, n2))) Space Complexity O(1))
def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1%n2
    return n1

n1 = 20
n2 = 15

print(f"GCD of {n1} and {n2} is {gcd(n1, n2)}")


