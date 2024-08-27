#Write a function that takes two dictionary and merge them into one, if there are duplicate keys the value in the 2nd dictionary should over write 1st dictionary.
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 2, 'e': 30, 'f': 40}
merged_dict = merge_dicts(dict1, dict2)
print("Merged Dictionary:", merged_dict)  #Output:Merged Dictionary: {'a': 2, 'b': 2, 'c': 3, 'e': 30, 'f': 40}
