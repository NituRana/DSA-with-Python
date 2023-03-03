'''*******************************************************************************************************
smallest element in an array :
Find the smallest element in an array.

Example:
Input: [3, 7, 8, 6, 9, 15, 17, 2]
Output: 0
***********************************************************************************************************'''
def smallest_element(arr):
    sma_element = arr[0]
    for i in range(0, len(arr)):
        if sma_element > arr[i]:
            sma_element = arr[i]
    print("The smallest element in the array is :- ",sma_element)
arr = [3, 7, 8, 6, 9, 15, 17, 2]
smallest_element(arr)

'''************************************************************************************************************
Complexcity - n
*************************************************************************************************************'''