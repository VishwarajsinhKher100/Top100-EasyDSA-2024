def find_peak(arr):
    length = len(arr)
    if length == 1:
        return arr[0]
    if arr[0] > arr[1]: 
        return arr[0]
    if arr[length - 1] > arr[length - 2]: 
        return arr[length - 1]
    
    for i in range(1, length - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return arr[i]
    return None

# Example usage
arr = [1, 3, 20, 30, 100, 50]
print(find_peak(arr)) 