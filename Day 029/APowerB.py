def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

# Example usage
base = int(input("Enter the base value: "))
exponent = int(input("Enter the exponent value: "))
print(f"{base} raised to the power of {exponent} is {power(base, exponent)}")
