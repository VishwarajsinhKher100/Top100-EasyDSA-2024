arr = [1,2,3,4,5]
reversed_arr = []

for num in arr:
    reversed_arr.insert(0, num)

print(f"Before reversing array : {arr}")
print(f"After reversing array : {reversed_arr}")