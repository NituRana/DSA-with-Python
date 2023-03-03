'''*******************************************************************************************************
index of a given element in an array :
Find the index of a given element in an array.

Example:
array: [3, 7, 8, 6, 9, 15, 17, 2]
Input: 15
Output: 5
***********************************************************************************************************'''
def find_index_of_ele(element):
    for i in range(0, len(arr)):
        if element == arr[i]:
             return i

arr = [3, 7, 8, 6, 9, 15, 17, 2]
print(" This is the array list:- ",arr)
ele = int(input("Enter the element which index you want :- "))
print("The index if this element is :- ", find_index_of_ele(ele))

'''************************************************************************************************************
Complexcity - n
*************************************************************************************************************'''