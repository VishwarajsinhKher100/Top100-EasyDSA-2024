def RotateLeftByOne(array):
    if len(array) == 0:
        return array
    FirstElement = array.pop(0)
    array.append(FirstElement)
    return array

array = [1,2,3,4,5]
RotatedArray = RotateLeftByOne(array)
print(RotatedArray)