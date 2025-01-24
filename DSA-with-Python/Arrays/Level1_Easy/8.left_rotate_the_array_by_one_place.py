'''*******************************************************************************************************
Problem Statement: Given an array of N integers, left rotate the array by one place.

Example 1:
Input:
 N = 5, array[] = {1,2,3,4,5}
Output:
 2,3,4,5,1
Explanation:
 
Since all the elements in array will be shifted 
toward left by one so '2' will now become the 
first index and and '1' which was present at 
first index will be shifted at last.


***********************************************************************************************************'''
def left_rotate_arr_elements(arr):
    res_arr = []
    element = None
    for i in range (len(arr)):
        if element is None:
            element = arr[i]
        else:
            res_arr.append(arr[i])
    res_arr.append(element)
    return res_arr
print(left_rotate_arr_elements([2, 8, 9, 4, 6, 0]))
        