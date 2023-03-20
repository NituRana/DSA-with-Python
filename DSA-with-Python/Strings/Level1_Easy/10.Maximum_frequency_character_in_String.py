'''*******************************************************************************************************
Maximum frequency character in String

Input : "I am software engineer"
Output : e


***********************************************************************************************************'''
def max_frequency_char(string):
    char_count = {}
    max_char = ''
    max_count = 0
    for char in string:
        if char == ' ':
            continue
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        if char_count[char] > max_count:
            max_count = char_count[char]
            max_char = char
    return max_char

# Example usage:
string = "I am a software engineer"
max_char = max_frequency_char(string)
print(f"The maximum frequency character (excluding spaces) in '{string}' is '{max_char}'")


# def max_frequency_char(string):
#     char_count = {}
#     max_char = ''
#     max_count = 0
#     for char in string:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#         if char_count[char] > max_count:
#             max_count = char_count[char]
#             max_char = char
#     return max_char

# # Example usage:
# string = "I am a software engineer"
# max_char = max_frequency_char(string)
# print(f"The maximum frequency character in '{string}' is '{max_char}'")