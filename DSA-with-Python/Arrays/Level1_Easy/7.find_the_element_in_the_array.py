'''*******************************************************************************************************
Problem Statement: Given an array, and an element num the task is to find if num is present in the given 
array or not. If present print the index of the element or print -1.

Example:
Example 1:
Input: arr[]= 1 2 3 4 5, num = 3
Output: 2
Explanation: 3 is present in the 2nd index
********************************************************************************************************'''

def is_element_present(arr, element):
    for i in range (len(arr)):
        if element == arr[i]:
            return i
    return -1

array = [8, 3, 1, 9, 5, 7, 14, 20, 6]
print(is_element_present(array, 20))