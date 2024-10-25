'''*******************************************************************************************************
reverse a string
Input : "This is a test string"
Output : gnirts tset a si sihT


***********************************************************************************************************'''
string = "This is a test string"
reversed_string = string[::-1]
print("The reversed string is:", reversed_string)
 

#revision 1

'''*******************************************************************************************************
reverse a string
Input : "This is a test string"
Output : sihT si a tset gnirts

***********************************************************************************************************'''

def resersed_the_word(input_string):
    list_of_words = input_string.split()
    output_string = ""
    for current_word in list_of_words:
        output_string += resersed_curr_word + " "
        resersed_curr_word = current_word[::-1]
    return output_string
input_string = "This is a test string"
print("----------------Input string :", input_string)
res = resersed_the_word(input_string)
print("----------------output string :", res)
