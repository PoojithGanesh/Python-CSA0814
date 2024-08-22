#Given a string S as input and arrange in ascending order if any repeating character found. Find the first index of repeated element
def first_repeated_char(s):
    seen = set()
    for i, char in enumerate(s):
        if char in seen:
            return i
        seen.add(char)
    return -1

s = input("Enter a string: ")
print(first_repeated_char(s))
