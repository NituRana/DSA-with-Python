'''*******************************************************************************************************
average of all elements :
Find the average of all elements in an array

Example:
Input: [1, 7, 3, 6, 9, 15, 0, 2]
Output: 0
***********************************************************************************************************'''

sum = 0
arr = []
len = int(input("Enter the array length :- "))
for i in range(len):
    element = int(input("Enter the {} element  :- ".format(i)))
    sum = sum + element
    arr.append(element)
print("This is your array :- ",arr)
print("The average of the array is :-",int(sum/len))

'''************************************************************************************************************
Complexcity - n
*************************************************************************************************************'''
