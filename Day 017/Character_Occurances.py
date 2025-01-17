def char_Count(text, char, count=0):
    for c in text:
        if c == char:
            count+=1
    return count

text = input("Enter the text: ")
char = input("Enter the character which you want to count: ")
result = char_Count(text, char)
print(f"The {char} is {result} time occur in this text.")