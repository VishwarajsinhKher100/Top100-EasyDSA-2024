def MoveZerosToEnd(array):
    NonZeroIndex = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[NonZeroIndex], array[i] = array[i], array[NonZeroIndex]
            NonZeroIndex += 1
    return array
        
array = [1, 0, 0, 1, 1, 0, 1, 1, 0]
result = MoveZerosToEnd(array)
print("Array after moving zeros:", result)