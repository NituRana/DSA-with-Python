'''*************************************************************************************************************************
Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
Output: 6 7 1 2 3 4 5
Explanation: array is rotated to right by 2 position .

Example 2:
Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
Output: 9 10 11 3 7 8
Explanation: Array is rotated to right by 3 position.
************************************************************************************************************************'''
def reverse(arr, start, end):
    while start<=end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_elements_to_left(arr, n, k):
    # Reverse first k elements
    reverse(arr, 0, k - 1)
    print("___________________________ 1. : ", arr)
    # Reverse last n-k elements
    reverse(arr, k, n - 1)
    print("___________________________ 2. : ", arr)
    # Reverse whole array
    reverse(arr, 0, n - 1)
    print("___________________________ 3. : ", arr)

arr = [1, 2, 3, 4, 5, 6, 7]
n = 7
k = 2

print(rotate_elements_to_left(arr, n, k))
print("___________________________ result . : ", arr)

'''**********************************************************************************************************
***********************************************************************************************************'''
