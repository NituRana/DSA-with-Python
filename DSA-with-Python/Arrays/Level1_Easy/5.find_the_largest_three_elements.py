'''*******************************************************************************************************
Given an array with all distinct elements, find the largest three elements.

Input: arr = [0, 1, 2, 6, 9]
Output: 9, 6, 2
---------------------------------------------
Input: arr = [4, 5, 10, 11] 
Output: 11, 10, 5


***********************************************************************************************************'''
def ThreeLargestNum(arr):
    arr.sort(reverse=True)
    return arr[:3]

arr = [10, 4, 3, 50, 23, 90]
print(ThreeLargestNum(arr))