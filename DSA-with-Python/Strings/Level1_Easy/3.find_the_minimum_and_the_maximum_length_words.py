'''*******************************************************************************************************
Input : "This is a test string"
Output : Minimum length word: a
         Maximum length word: string


***********************************************************************************************************'''
def find_min_max_words(string):
    words = string.split()
    min_word = max_word = words[0]

    for word in words:
        if len(word) < len(min_word):
            min_word = word
        elif len(word) > len(max_word):
            max_word = word

    return min_word, max_word

string = "The quick brown fox jumps over the lazy dog"
min_word, max_word = find_min_max_words(string)
print(f"Minimum length word: {min_word}")
print(f"Maximum length word: {max_word}")
 
   