'''
Insertion Sort Algorithm
Problem Statement: Given an array of N integers, write a program to implement the Insertion sorting algorithm.

Examples:

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: 
After sorting the array is: 9,13,20,24,46,52


Example 2:
Input: N=5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting the array is: 1,2,3,4,5

'''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        for k in range(i - 1, -2, -1):
            if k >= 0 and arr[k] > key:
                arr[k + 1] = arr[k]
            else:
                arr[k + 1] = key
                break
    return arr

arr = [13, 46, 24, 52, 20, 9]
print(f"---- output : {insertion_sort(arr)}")