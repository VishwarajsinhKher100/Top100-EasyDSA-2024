def longest_common_prefix(strs):
    if not strs:
        return ""
    
    strs.sort()
    first = strs[0]
    last = strs[-1]
    common_prefix = ""
    
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            common_prefix += first[i]
        else:
            break
    return common_prefix

strings = ["flower", "flow", "flight"]
result = longest_common_prefix(strings)
print(f"Longest Common Prefix is {result}.")