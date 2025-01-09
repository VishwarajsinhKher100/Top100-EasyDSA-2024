array1 = [10, 20, 30, 40, 50]
array2 = [10, 30, 50, 70, 90]

Union = list(set(array1) | set(array2))
Intersection = list(set(array1) & set(array2))

print(f"Union :- {Union} \nIntersection :- {Intersection}")