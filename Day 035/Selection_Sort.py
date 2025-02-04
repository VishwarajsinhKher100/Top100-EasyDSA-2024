def SelectionSort(arr):
    length = len(arr)
    for i in range(length):
        MinIndex = i
        for j in range(i+1, length):
            if arr[j] < arr[MinIndex]:
                MinIndex = j
        arr[i], arr[MinIndex] = arr[MinIndex], arr[i]
    return arr

#Example Usage
arr = [64, 34, 25, 12, 22, 11, 90, 7, 111, 66]
print(f"Before Sorting: {arr}")
print(f"After Sorting: {SelectionSort(arr)}")
