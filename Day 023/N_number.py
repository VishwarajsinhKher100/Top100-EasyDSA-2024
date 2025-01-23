def PrintNumbers(n):
    if n > 0:
        PrintNumbers(n - 1)
        print(n)

# Example usage
number = int(input("Enter how many number you whan to print: "))
PrintNumbers(number)
