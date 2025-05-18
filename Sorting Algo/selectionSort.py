arr = [32,893,73,12,0,37,3]
n = len(arr)
for i in range(n):
    mini = i
    for j in range(i, n):
        if arr[j] < arr[mini]:
            mini = j

     # pythonic swap
    if i != mini:
        arr[i], arr[mini] = arr[mini], arr[i]
        
    # # Comman Swap
    # temp = arr[i]
    # arr[i] = arr[mini]
    # arr[mini] = temp

   

print(arr)