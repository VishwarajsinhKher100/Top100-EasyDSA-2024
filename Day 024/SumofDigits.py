def SumOfDigits(num):
    if num == 0:
        return 0
    return num % 10 + SumOfDigits(num // 10)

number = int(input("Enter a number: "))
result = SumOfDigits(abs(number))
print(f"The sum of the digits of {number} is {result}.")
