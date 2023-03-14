'''*******************************************************************************************************
find the first non-repeating character in a string.
Input:  arr[] = ["11", "1"]
Output: "100"


***********************************************************************************************************'''
string = "this is the string"
for char in string:
    if string.count(char) == 1:
        print("The first non-repeating character is:", char)
        break