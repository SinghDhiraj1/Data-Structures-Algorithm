a = [1, 3, 8, 9, 2, 4, 5, 7, 6, 0, 90, 2, 1]


def merge(a, low, mid, high):
    temp_arr = []
    left = low
    right = mid+1

    while(left <=  mid and right <= high):
        if (a[left] < a[right]):
            temp_arr.append(a[left])
            left += 1
        else:
            temp_arr.append(a[right])
            right += 1

    while(left <= mid):
        temp_arr.append(a[left])
        left+=1
    while(right <= high):
        temp_arr.append(a[right])
        right+=1
    
    for i in range(len(temp_arr)):
        a[low+i] = temp_arr[i]

def mergeSort(a, low, high):
    if low >= high:
        return
    
    low = low
    high = high
    mid = (low + high)//2
    mergeSort(a, low, mid)
    mergeSort(a, mid+1, high)
    merge(a, low, mid, high)
    
mergeSort(a, 0, len(a)-1)
print(a)