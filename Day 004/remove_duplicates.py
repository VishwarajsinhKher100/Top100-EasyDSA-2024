def remove_duplicates(sorted_arr):
    unique_arr = []
    for num in sorted_arr:
        if not unique_arr or num != unique_arr[-1]:
            unique_arr.append(num)
    return unique_arr

sorted_arr = [1,1,2,2,3,4,4,5]
result = remove_duplicates(sorted_arr)
print(result)