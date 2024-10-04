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
#         key = arr[i]
        
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

#     return arr


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         current_min_ele = i
#         j = i-1
#         while j >= 0 and arr[j] > current_min_ele:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j + 1] = current_min_ele
#     return arr

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         last_sorted_ele_ind = i
#         j = i-1
#         while j >=0 and arr[last_sorted_ele_ind] > arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = last_sorted_ele_ind
#     return arr
# arr = [12, 0, 11, 7, 13, 5, 6, 5, 13]
# print("Un-sort array:", arr)
# sorted_arr = insertion_sort(arr)
# print("Sorted array:", sorted_arr)




def insertion_sort(arr):
    for i in range(1, len(arr)):
        min_ele = arr[i]
        j = i-1
        while j >=0 and min_ele < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = min_ele
    return arr

array = [46, 28, 23, 15, 56, 90, 42, 12]
print("--------------------- unsorted array :", array)
sorted_array = insertion_sort(array)
print("--------------------- sorted array :", sorted_array)