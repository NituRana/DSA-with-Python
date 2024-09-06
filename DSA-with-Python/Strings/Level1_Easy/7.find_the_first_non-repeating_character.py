'''*******************************************************************************************************
Python program to find the first non-repeating character in a given string:- 

Input : "aabbcdefg"
Output : c


***********************************************************************************************************'''
# def first_non_repeating_char(s):
#     counts = {}
#     for char in s:
#         counts[char] = counts.get(char, 0) + 1
    
#     for char in s:
#         if counts[char] == 1:
#             return char
#     return None


# ------------ Bruce force approach ---------------
def first_non_repeating_char(string):
    for i in range(len(string)):
        is_char_dublicate = False
        for j in range(len(string)):
            if i != j and string[i] == string[j]:
                is_char_dublicate = True
                break
        if is_char_dublicate == False:
            return string[i]


# ------------ using dict (optimal one) -----------
# def first_non_repeating_char(string):
#     dict_of_char = {}
#     for char in string:
#         if char in dict_of_char:
#             dict_of_char[char] += 1
#         else:
#             dict_of_char[char] = 1
#     for char in string:
#         if dict_of_char[char] == 1:
#             return char 

s = "aawbbcdefg"
print(first_non_repeating_char(s))

   