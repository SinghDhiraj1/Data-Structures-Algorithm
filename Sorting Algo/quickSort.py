arr = [1, 3, 8, 9, 2, 4, 5, 7, 6, 0, 90, 2, 1]

def partition(arr, low, high):
    pivot = low

    count = 0
    for i in range(low+1, high+1):
        if arr[i] < arr[pivot]:
            count += 1

    # place pivot at its correct place
    pivotIndex = pivot + count
    arr[pivotIndex], arr[pivot] = arr[pivot], arr[pivotIndex]
    pivot = pivotIndex

    left = low
    right = high
    while(left < pivot and right > pivot):
        while(arr[left] <= arr[pivot] and left < pivot):
            left += 1
        while(arr[right] >= arr[pivot] and right > pivot):
            right -= 1

        if (left < pivot and right > pivot):
            arr[left], arr[right] = arr[right], arr[left]
    
    return pivot


def quickSort(arr, low, high):
    # base case
    if low >= high:
        return
    
    partitionIndex = partition(arr, low, high)

    quickSort(arr, low, partitionIndex-1)
    quickSort(arr, partitionIndex+1, high)


quickSort(arr, 0, len(arr)-1)
print(arr)