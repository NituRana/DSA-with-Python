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

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         curr_ele = arr[i]
#         j = i - 1
#         while curr_ele < arr[j] and j >= 0:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j+1] = curr_ele
#     return arr



def insertion_sort(input_arr):
    for i in range(1, len(input_arr)):
        curr_ele = input_arr[i]
        j  = i-1
        while j >= 0 and input_arr[j] > curr_ele:
            input_arr[j+1] = input_arr[j]
            j -= 1
        input_arr[j+1] = curr_ele
    return arr
        
arr = [23, 4, 24, 15, 67, 345, 78, 32]
print("------------------- un-sorted array :", arr)
res = insertion_sort(arr)
print("------------------- sorted array :", res)

# array = [46, 28, 23, 15, 56, 90, 42, 12]
# print("--------------------- unsorted array :", array)
# sorted_array = insertion_sort(array)
# print("--------------------- sorted array :", sorted_array)