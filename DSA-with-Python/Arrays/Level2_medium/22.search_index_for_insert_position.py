'''
Problem Statement: You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.

If the value is present in the array, then return its index. Otherwise, determine the index where it would be inserted in the array while maintaining the sorted order.

Pre-requisite: Lower Bound & Binary Search

Example 1:
Input Format: arr[] = {1,2,4,7}, x = 6
Result: 3
Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.

Example 2:
Input Format: arr[] = {1,2,4,7}, x = 2
Result: 1
Explanation: 2 is present in the array and so we will return its index i.e. 1.

'''

def get_index_for_insert_target_element(arr, target_element):
    arr_len = len(arr)
    min_idx = 0
    max_idx = arr_len - 1
    ans = arr_len
    while min_idx <= max_idx:
        mid = (min_idx + max_idx) // 2
        if target_element <= arr[mid]:
            ans = mid
            min_idx = mid + 1
        else:
            max_idx = mid - 1

    return ans

arr = [1,2,4,7] 
x = 6
res = get_index_for_insert_target_element(arr, x)
print("--------------- res :", res)
