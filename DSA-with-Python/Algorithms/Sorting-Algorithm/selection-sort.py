'''
Selection Sort Algorithm

Problem Statement: Given an array of N integers, write a program to implement the Selection sorting algorithm.

Examples:

Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

Example 2:
Input: N=5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting the array is: 1, 2, 3, 4, 5


algo :
step 1 : find the minimal 
step 2 : swap the with the currect element position 
'''
                
# def selection_sort(arr):
#     for i in range(len(arr)):
#         last_ele_of_sort = i
#         for j in range(i+1, len(arr)):
#             if arr[last_ele_of_sort] > arr[j]:
#                 last_ele_of_sort = j
#         arr[i], arr[last_ele_of_sort] = arr[last_ele_of_sort], arr[i]
#     return arr

# arr = [13, 46, 24, 52, 20, 9]
# print(f"---- Input : {arr}")
# print(f"---- output : {selection_sort(arr)}")

def selection_sort(arr):
    for i in range(len(arr)):
        curr_ele = i
        for j in range(i+1, len(arr)):
            if arr[curr_ele] > arr[j]:
                curr_ele = j
        arr[i], arr[curr_ele] = arr[curr_ele], arr[i]
    return arr

array = [46, 28, 23, 15, 56, 90, 42, 12]
print("--------------------- unsorted array :", array)
sorted_array = selection_sort(array)
print("--------------------- sorted array :", sorted_array)
