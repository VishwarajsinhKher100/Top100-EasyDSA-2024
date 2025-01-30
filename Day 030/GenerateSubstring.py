def generate_subsets(string, index=0, current=""):
    if index == len(string):
        print(current)
        return
    
    generate_subsets(string, index + 1, current)
    generate_subsets(string, index + 1, current + string[index])

# Example usage
string = input("Enter the string: ")
generate_subsets(string)
