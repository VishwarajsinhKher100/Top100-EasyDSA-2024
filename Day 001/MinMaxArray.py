arr = [3,5,1,6,8,2]
Max, Min = arr[0], arr[0]

for num in arr:
    if num > Max:
        Max = num
    if num < Min:
        Min = num

print("Maximum number in this array is", Max)
print("Minimum number in this array is", Min)