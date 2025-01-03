def is_sorted(arr):
    for num in range(len(arr)-1):
        if arr[num] > arr[num+1]:
            return False
    return True

arr = [2,5,1,3,4]
print(is_sorted(arr))