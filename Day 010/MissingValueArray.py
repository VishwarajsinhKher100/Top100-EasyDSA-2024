def FindMissingNumber(array, n):
    ExpectedSum = n * (n + 1) // 2
    ActualSum = sum(array)
    MissingNumber = ExpectedSum - ActualSum
    return MissingNumber

n = 5
array = [1, 2, 4, 5]
missing = FindMissingNumber(array, n)
print(f"The missing number is: {missing}")