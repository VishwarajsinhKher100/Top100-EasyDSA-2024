def Digit_Checker(string):
    if string.isdigit():
        print(f"The given {string} string contains only digits.")
    else:
        print(f"The given {string} string contains non-digit characters.")
    
string = input("Enter the string: ")
result = Digit_Checker(string)
