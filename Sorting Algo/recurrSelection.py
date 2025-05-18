arr = [3, 7, 9, 0, 2, 1, 6, 4, 5]

def recurrSelection(arr, n): # array and start of the array using recursion
    if n == len(arr):
        return
    
    mini = n

    for i in range(n+1, len(arr)):
        if arr[i] <= arr[mini]:
            mini = i

    arr[mini], arr[n] = arr[n], arr[mini]
    
    recurrSelection(arr, n+1)


recurrSelection(arr, 0)
print(arr)