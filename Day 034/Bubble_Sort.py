def BubbleSort(arr):
    length = len(arr)
    for i in range(length):
        swapped = False
        for j in range(0, length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

#Example Usage
arr = [64, 34, 25, 12, 22, 11, 90, 7, 111, 66]
print(f"Before Sorting: {arr}")
print(f"After Sorting: {BubbleSort(arr)}")