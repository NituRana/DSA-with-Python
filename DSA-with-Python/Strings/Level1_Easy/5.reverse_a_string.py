'''*******************************************************************************************************
reverse a string
Input : "This is a test string"
Output : gnirts tset a si sihT


***********************************************************************************************************'''
string = "This is a test string"
reversed_string = string[::-1]
print("The reversed string is:", reversed_string)
 

'''*******************************************************************************************************
reverse a string
Input : "This is a test string"
Output : sihT si a tset gnirts

***********************************************************************************************************'''

def resersed_the_word(input_string):
    words_list = input_string.split()
    output_string = ""
    for word in words_list:
        reverse_word = word[::-1]
        output_string += reverse_word + " "
    return output_string

input_string = "This is a test string"
print("----------------Input string :", input_string)
res = resersed_the_word(input_string)
print("----------------output string :", res)
