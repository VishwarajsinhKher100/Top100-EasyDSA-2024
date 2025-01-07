def SecondLargest(array):
    if len(array) < 2:
        return "Array must have at least two elements."
    
    UniqueElements = list(set(array))

    if len(UniqueElements) < 2:
        return "No Second largest element."

    UniqueElements.sort(reverse=True)
    return UniqueElements[1]

array = [10, 20, 50, 5, 2, 5, 10]
result = SecondLargest(array)
print("Second Largest Element:", result)
