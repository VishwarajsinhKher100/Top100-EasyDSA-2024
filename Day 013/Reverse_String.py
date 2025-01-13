def reverse_string(string):
    reversed_string = " "
    for char in string:
        reversed_string = char+reversed_string
    return reversed_string

input_string = "Welcome to Python"
reversed_string = reverse_string(input_string)
print(f"Original String: {input_string}")
print(f"Reversed String: {reversed_string}")