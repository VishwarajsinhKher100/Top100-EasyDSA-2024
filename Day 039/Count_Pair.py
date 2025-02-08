def count_pairs(arr, target):
    count = 0
    length = len(arr)
    for i in range(length):
        for j in range(i + 1, length):
            if arr[i] + arr[j] == target:
                count += 1
    return count

# Example usage
arr = [1, 5, 7, -1, 5]
target = int(input("Enter numbert as a sum of pairs: "))
print(count_pairs(arr, target))