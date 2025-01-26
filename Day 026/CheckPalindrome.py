def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

# Example Usage
string = input("Ente the string: ")
if is_palindrome_recursive(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')

