'''
Merge Sort Algorithm

Problem:  Given an array of size n, sort the array using Merge Sort.

Examples:

Example 1:
Input: N=5, arr[]={4,2,1,6,7}
Output: 1,2,4,6,7,


Example 2:
Input: N=7,arr[]={3,2,8,5,1,4,23}
Output: 1,2,3,4,5,8,23

'''

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]

#     left_sorted = merge_sort(left_half)
#     right_sorted = merge_sort(right_half)

#     return merge(left_sorted, right_sorted)

# def merge(left, right):
#     sorted_array = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             sorted_array.append(left[i])
#             i += 1
#         else:
#             sorted_array.append(right[j])
#             j += 1

#     while i < len(left):
#         sorted_array.append(left[i])
#         i += 1

#     while j < len(right):
#         sorted_array.append(right[j])
#         j += 1

#     return sorted_array



# def merge_sort(unsort_arr):
#     if len(unsort_arr)<= 1:
#         return unsort_arr

#     mid = len(unsort_arr) // 2
#     left_arr = unsort_arr[:mid]
#     right_arr = unsort_arr[mid:]

#     sorted_left = merge_sort(left_arr)
#     sorted_right = merge_sort(right_arr)

#     return merge(sorted_left, sorted_right)

# def merge(left_arr, right_arr):
#     sorted_arr = []
#     i = j = 0
#     while i < len(left_arr) and j < len(right_arr):
#         if left_arr[i] < right_arr[j]:
#             sorted_arr.append(left_arr[i])
#             i += 1
#         else:
#             sorted_arr.append(right_arr[j])
#             j += 1
#     sorted_arr.extend(left_arr[i:])
#     sorted_arr.extend(right_arr[j:])
#     return sorted_arr


def merge_sort(unsort_arr):
    if len(unsort_arr)==1:
        return unsort_arr
    mid = len(unsort_arr) // 2
    left_arr = merge_sort(unsort_arr[:mid])
    right_arr = merge_sort(unsort_arr[mid:])
    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    res_arr = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] > right_arr[j]:
            res_arr.append(right_arr[j])
            j += 1
        else:
            res_arr.append(left_arr[i])
            i += 1
    res_arr.extend(left_arr[i:])
    res_arr.extend(right_arr[j:])
    return res_arr

arr = [13, 46, 24, 52, 20, 9]
print(f"---- input  : {arr}")
sorted_arr = merge_sort(arr)
print(f"---- output : {sorted_arr}")