'''*******************************************************************************************************
Given an array A[] consisting of only 0s, 1s, and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.

Example:
Input array: = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]

Input array: =[{0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
***********************************************************************************************************'''
 
def sorted_arr(arr, n):
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = [0, 1, 2, 0, 1, 2]
n = len(arr)
print ("This is the sorted array :- ", sorted_arr(arr, n))