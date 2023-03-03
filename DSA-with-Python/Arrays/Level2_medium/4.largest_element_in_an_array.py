'''*******************************************************************************************************
largest element in an array :
Find the largest element in an array.

Example:
Input: [1, 7, 3, 6, 9, 15, 0, 2]
Output: 15
***********************************************************************************************************'''
def largest_element(arr):
    lar_element = arr[0]
    for i in range(0, len(arr)):
        if lar_element < arr[i]:
            lar_element = arr[i]
    print("The largest element in the array is :- ",lar_element)
arr = [1, 7, 3, 6, 9, 15, 0, 2]
largest_element(arr)

'''************************************************************************************************************
Complexcity - n
*************************************************************************************************************'''