def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

# Example usage
string = input("Enter the string: ")
print(f"After Reversing the given String is {reverse_string(string)}.")
