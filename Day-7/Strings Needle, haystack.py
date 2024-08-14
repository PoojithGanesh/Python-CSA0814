def find_index(needle, haystack):
    last_char = haystack[-1]
    index = needle.find(last_char)  
    return index
needle = "NEEDLE"
haystack = "HAYSTACK"
index = find_index(needle, haystack)
print(f"The index of the first occurrence of '{haystack[-1]}' in '{needle}' is: {index}")
