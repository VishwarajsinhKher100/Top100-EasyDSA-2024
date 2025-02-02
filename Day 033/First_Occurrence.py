numbers = [10, 20, 30, 40, 20, 50]
target = 20

index = next((i for i, num in enumerate(numbers) if num == target), -1)
print(f"The first occurrence of {target} is at index {index}.")