'''*******************************************************************************************************
K’th smallest element in the given array :
Given an array and a number K where K is smaller than the size of the array. Find the K’th smallest element in the given array.

Example:
Input array: = [7, 10, 4, 3, 20, 15],  k = 3
Output : 7

Input array: = [7, 10, 4, 3, 20, 15],  k = 5
Output : 15
***********************************************************************************************************'''
 
def K_smallest_ele(arr, n, k):
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr[k - 1]
arr = [7, 10, 4, 3, 20, 15]
n = len(arr)
k = 5
print ("This is the k'th smallest element :- ", K_smallest_ele(arr, n, k))