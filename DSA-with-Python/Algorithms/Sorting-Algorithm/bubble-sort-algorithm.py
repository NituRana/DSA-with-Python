'''
Bubble Sort Algorithm

Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

Examples:

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52


Input: N = 5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting we get 1,2,3,4,5

'''

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 temp = arr[j +1]
#                 arr[j + 1] = arr[j]
#                 arr[j] = temp
#     return arr

# arr = [13,46,24,52,20,9]
# print("-------------- Before sorting :", arr)
# print("----- After sorting :", bubble_sort(arr))








# def bubble_sort(unsort_array):
#     arr_len = len(unsort_array)
#     for i in range(0, arr_len-1):
#         for j in range(i, arr_len):
#             if unsort_array[i] > unsort_array[j]:
#                 temp = unsort_array[i]
#                 unsort_array[i] = unsort_array[j]
#                 unsort_array[j] = temp
#     return unsort_array





def bubble_sort(unsort_array):
    for i in range(len(unsort_array)-1):
        for j in range(i+1, len(unsort_array)):
            if unsort_array[i] > unsort_array[j]:
                temp = unsort_array[i]
                unsort_array[i] = unsort_array[j]
                unsort_array[j] = temp
    return unsort_array



input_array = [7, 8, 4, 6, 0, 3, 24, 15, 9]
print("--------------- input_array :", input_array)
sorted_array = bubble_sort(input_array)
print("--------------- sorted_array :", sorted_array)