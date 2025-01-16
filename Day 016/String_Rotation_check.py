def is_rotation(s1, s2):
    if len(s1) != len(s2) or not s1:
        return False
    combined = s1 + s1
    return s2 in combined

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print(is_rotation(str1, str2))