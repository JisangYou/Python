def binary_search(arr, value):
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high) // 2

        if arr[mid] > value:
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
        else:
            return mid

    return -1


arr = [1, 5, 7, 10, 25, 32, 79, 80, 125]
print(binary_search(arr, 7))
print(binary_search(arr, 8))
