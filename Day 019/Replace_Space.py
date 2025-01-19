def ReplaceSpace(string):
    modify_String = string.replace(" ", "%20")
    return modify_String

string = input("Enter the Text: ")
result = ReplaceSpace(string)
print(string)
