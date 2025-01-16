def first_not_repreating_char(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None

string = input("Enter the string: ")
result = first_not_repreating_char(string)
print(f"The first non-repeating character is: {result}")