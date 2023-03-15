'''*******************************************************************************************************
largest word in a given string: 
Input : "Welcome in my data structure repo"
Output : structure


***********************************************************************************************************'''
def largest_word(s):
    words = s.split()
    return max(words, key=len)

s = "Welcome in my data structure repo"
print(largest_word(s))
 
   