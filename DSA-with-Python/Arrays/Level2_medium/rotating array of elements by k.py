'''*******************************************************************************************************
Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
Output: 6 7 1 2 3 4 5
Explanation: array is rotated to right by 2 position .

Example 2:
Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
Output: 9 10 11 3 7 8
Explanation: Array is rotated to right by 3 position.

***********************************************************************************************************'''

def rotate_the_array(arr, k):
    print("---------------- len :", len(arr))
    for i in range (len(arr)):
        print("---------------- i :", i)
        if not (i == ((len(arr))-1)):
            if arr[i] == 0:
                arr[i] = arr[i + 1]
                arr[i + 1] = 0

    return arr


print(move_all_zeros_to_the_end([0, 2, 0, 8, 9, 0, 4, 6, 0]))
