arr = [32,893,73,12,0,37,3]

arr = [0, 1, 2, 3, 4, 5]
n = len(arr)
for i in range(1,n):
    # for j in range(i, 0, -1):
    #     print(f" i is {i} and j is {j}")
    #     if arr[j] < arr[j-1]:
    #         arr[j], arr[j-1] = arr[j-1], arr[j]
    #         print("run")

    # Optimized
    j = i
    while(j > 0 and arr[j-1] > arr[j]):
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1
    
    
print(arr)