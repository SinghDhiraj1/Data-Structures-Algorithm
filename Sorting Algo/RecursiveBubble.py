arr = [93, 29, 12, 93, 0, 23, 48]

def recurrBubble_back(arr, n):
    if n == len(arr):
        return
    
    recurrBubble(arr, n+1)
    for i in range(n):
        if arr[i] >= arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    

def recurrBubble(arr, n):
    if n == 0:
        return
    
    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    recurrBubble(arr, n-1)


recurrBubble(arr, len(arr))
print(arr)