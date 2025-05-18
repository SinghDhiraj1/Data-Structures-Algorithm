arr = [32,893,73,12,0,37,3]

# Bubble sort
for i in range(len(arr),0,-1):
    swap = 0
    for j in range(i-1):
        if arr[j] > arr[j+1]:
             # pythonic swap
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swap = 1
            # Comman Swap
            # temp = arr[j]
            # arr[j] = arr[j+1]
            # arr[j+1] = temp
    if swap == 0:
        break
print(arr)