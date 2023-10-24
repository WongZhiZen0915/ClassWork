def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
    print(arr)
arr = [32,43,65,87,3,1,879,123,45,98,651,381,12,23,94,67,27]
insertionSort(arr)

print()

