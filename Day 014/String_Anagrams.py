def string_anagrams(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string1 = string2.replace(" ", "").lower()
    return sorted(string1) == sorted(string2)

str1 = "listen"
str2 = "silent"
if string_anagrams(str1, str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")
