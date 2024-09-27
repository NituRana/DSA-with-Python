'''*******************************************************************************************************
In the given a string and we need to remove all duplicates from it

Input : "Hello here, I'm nitu rana"
Output : c


***********************************************************************************************************'''
# def removeDuplicates(s):
#     return ''.join(set(s))

# s = "Hello here, I'm nitu rana"
# print(removeDuplicates(s))

# def removeDuplicates(s):
#     counts = {}
#     for c in s:
#         counts[c] = counts.get(c, 0) + 1
#     result = ''
#     for c in s:
#         if counts[c] == 1:
#             result += c
#     return result


# def removeDuplicates(s):
#     dict_of_char = {}
#     for i in s:
#         if i in dict_of_char:
#             dict_of_char[i] += 1
#         else:
#             dict_of_char[i] = 1
    
#     result = ''
#     for i in s:
#         if dict_of_char[i] == 1:
#             result += i

#     return result


def removeDuplicates(s):
    char_dict = {}
    for i in s:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    res = ""
    for i in char_dict:
        if char_dict[i] == 1:
            res += i
    return res
s = "Hello here, I'm nitu rana"
res = removeDuplicates(s)
print("-------------------- res : ", res)

   