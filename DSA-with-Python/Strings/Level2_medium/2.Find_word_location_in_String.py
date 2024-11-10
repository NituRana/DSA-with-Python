'''*******************************************************************************************************
Find Word location in String in the given string.

Input : "Revising The String Concepts"
Output : C


***********************************************************************************************************'''

input_str = '"Revising The String Concepts"'
 
print("The original string is : " + input_str)
 
word = 'c'
 
x=input_str.split()
print(x)
res=x.index(word)+1
print("The location of word is : " + str(res))
