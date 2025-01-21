def factorial(n):
    if n < 0:
        return "not defined"
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}.")
