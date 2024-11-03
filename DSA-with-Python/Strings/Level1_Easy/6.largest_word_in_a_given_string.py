'''*******************************************************************************************************
largest word in a given string: 
Input : "Welcome in my data structure repo"
Output : structure


***********************************************************************************************************'''

def largest_word(string):
    list_of_word = string.split()
    max_word = list_of_word[0]

    for word in list_of_word:
        if len(max_word) < len(word):
            max_word = word
    return max_word


s = "Welcome in my data structure repo"
print(largest_word(s))
 
   