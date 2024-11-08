#-----------------------------------------------------------------------
#------------------------  approche : In-place algo --------------------
#-----------------------------------------------------------------------

# def quicksort(arr, low, high):
#     if low < high:
#         partition_ele = partition(arr, low, high)
#         quicksort(arr, low, partition_ele - 1) #left side element
#         quicksort(arr, partition_ele + 1, high)

# def partition(arr, low, high):
#     pivot_ele = arr[high]
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] <= pivot_ele:
#             # Increment the index of smaller elements
#             i += 1
#             # Swap current element with the element at index 'i'
#             arr[i], arr[j] = arr[j], arr[i]
#     # Place the pivot element in its correct position (after all smaller elements)
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return i+1

# array = [34, 66, 23, 12, 35, 5, 67, 79, 42, 50, 85]
# print("------------------- unsort array :", array)
# quick_sort(array, 0, len(array)-1)
# print("------------------- sort array :", array)


# arr = [33, 10, 59, 26, 41, 78, 14, 55]
# quicksort(arr, 0, len(arr) - 1)
# print("------------- sorted array :", arr)

#-----------------------------------------------------------------------
#--------------------- Second approche : Non in-place algo--------------
#-----------------------------------------------------------------------
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     # Select the pivot element. In this case, the pivot is the middle element of the array.
#     pivot = arr[len(arr) // 2]
    
#     # Create three lists to partition the array:
#     # 'less' will contain all elements smaller than the pivot
#     less = [x for x in arr if x < pivot]
    
#     # 'equal' will contain all elements equal to the pivot
#     equal = [x for x in arr if x == pivot]
    
#     # 'greater' will contain all elements greater than the pivot
#     greater = [x for x in arr if x > pivot]
    
#     # Recursively sort the 'less' and 'greater' sub-arrays,
#     # and concatenate them with the 'equal' array (pivot element).
#     return quicksort(less) + equal + quicksort(greater)

# arr = [33, 10, 59, 26, 41, 78, 14, 55]

# sorted_arr = quicksort(arr)
# print(sorted_arr)
# Output will be the sorted version of 'arr': [10, 14, 26, 33, 41, 55, 59, 78]

'''
algo :
 step 1. 

'''
def quick_sort(arr, low, high):
    if low < high:
        partition_ele = partition(arr, low, high)
        quick_sort(arr, low, partition_ele-1)
        quick_sort(arr, partition_ele+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

arr = [33, 10, 59, 26, 41, 78, 14, 55]
quick_sort(arr, 0, len(arr) - 1)
print("------------- sorted array :", arr)