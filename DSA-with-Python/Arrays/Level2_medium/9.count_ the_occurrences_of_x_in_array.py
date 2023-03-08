'''*******************************************************************************************************
occurrences of x in array :
Find the occurrences of x in sorted array.

Example:
Input array: = [1, 1, 2, 2, 2, 2, 3]   x = 2
Output : 4
***********************************************************************************************************'''
 
def countOccurrences(arr, n, x):
    res = 0
    for i in range(n):
        if x == arr[i]:
            res += 1
    return res
             

arr = [1, 1, 2, 2, 2, 2, 3]
n = len(arr)
x = 2
print (countOccurrences(arr, n, x))