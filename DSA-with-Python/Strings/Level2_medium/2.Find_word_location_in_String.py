'''*******************************************************************************************************
Find Word location in String in the given string.

Input : "hello here I am nitu rana"
Output : I


***********************************************************************************************************'''
input_str = '"hello here I am nitu rana"'
 
print("The original string is : " + input_str)
 
wrd = 'I'
 
x=input_str.split()
print(x)
res=x.index(wrd)+1
print("The location of word is : " + str(res))
