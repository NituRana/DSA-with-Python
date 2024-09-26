'''*******************************************************************************************************
Find the second most repeated word in a sequence in a given string,

Input : "Hello here, I'm nitu rana"
Output : l


***********************************************************************************************************'''
# def second_most_repeated_word(strings):
#     count = {}
#     for string in strings:
#         for word in string.split():
#             if word in count:
#                 count[word] += 1
#             else:
#                 count[word] = 1
#     sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
#     if len(sorted_count) < 2:
#         return None
#     else:
#         return sorted_count[1][0]

#-------------------------------- revise ----------------------

def second_most_repeated_word(string):
    stri = 'kjwde ejckc vvevemvev eveve'
    char_dict = {}
    for i in stri:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True ))
    return list(sorted_dict.keys())[0]

# Example usage
string = "Hello here, I'm nitu rana"
result = second_most_repeated_word(string)
print(result)
