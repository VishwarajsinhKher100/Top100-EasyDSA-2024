def is_subset(A, B):
    return set(B).issubset(set(A))

# Example usage
A = [1, 2, 3, 4, 5, 6]
B = [2, 4, 6]
print(is_subset(A, B))

C = [2, 4, 7]
print(is_subset(A, C))
