def InsertionSort(arr):
    Length = len(arr)
    for i in range(1, Length):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90, 7, 111, 66]
print(f"Before Sorting: {arr}")
print(f"After Sorting: {InsertionSort(arr)}")
