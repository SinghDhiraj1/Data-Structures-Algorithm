n = 7789

while (n>0):
    lastDigit = n%10
    print(f"Last digit is {lastDigit}")
    n = n//10 # removeDigit
    print(f"New n is {n}") 

