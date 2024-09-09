'''*******************************************************************************************************
Input : "This is a test string"
Output : Minimum length word: a
         Maximum length word: string


***********************************************************************************************************'''
def find_min_max_words(string):
    words = string.split() #splits the string at every whitespace and returns a list of words.
    min_word = max_word = words[0]

    for word in words:
        if len(word) < len(min_word):
            min_word = word
        elif len(word) > len(max_word):
            max_word = word

    return min_word, max_word

# revision
# def max_min_word(string):
#     words_list = string.split()
#     min_word = max_word = words_list[0]
#     for word in words_list:
#         if len(min_word) > len(word):
#             min_word = word
#         elif len(max_word) < len(word):
#             max_word = word
#     return min_word, max_word













def max_min_word(string):
    list_of_words = string.split()
    max_len_word = list_of_words[0]
    min_len_word = list_of_words[0]
    for current_word in list_of_words:
        if len(min_len_word) > len(current_word):
            min_len_word = current_word
        elif len(max_len_word) < len(current_word):
            max_len_word = current_word
    return min_len_word, max_len_word


string = "The quick brown fox jumps over the lazy dog"
min_word, max_word = max_min_word(string)
print(f"Minimum length word: {min_word}")
print(f"Maximum length word: {max_word}")
 
   