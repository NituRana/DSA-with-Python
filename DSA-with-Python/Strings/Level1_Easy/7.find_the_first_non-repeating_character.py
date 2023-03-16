'''*******************************************************************************************************
Python program to find the first non-repeating character in a given string:- 

Input : "aabbcdefg"
Output : c


***********************************************************************************************************'''
def first_non_repeating_char(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    
    for char in s:
        if counts[char] == 1:
            return char
    return None

s = "aabbcdefg"
print(first_non_repeating_char(s))
 
   