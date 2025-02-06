def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k <= len(left):
        return quickselect(left, k)
    elif k <= len(left) + len(mid):
        return pivot
    else:
        return quickselect(right, k - len(left) - len(mid))

# Example usage
arr = [70, 10, 40, 30, 60, 20, 50]
print(arr)
k = int(input("Enter Kth smallest element you wont to find: "))
print(f"Kth smallest element: {quickselect(arr, k)}")