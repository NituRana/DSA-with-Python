# def binary_search(arr, target_element):
    # arr_len = len(arr)
    # min_index = 0
    # max_index = arr_len - 1
    # while min_index <= max_index:
    #     mid = (min_index + max_index) // 2
    #     if target_element == arr[mid]:
    #         return mid
    #     else:
    #         if target_element > arr[mid]:
    #             min_index = mid + 1
    #         else:
    #             max_index = mid - 1
    # return -1

#     arr_len = len(arr)
#     min_index = 0
#     max_index = arr_len -1
#     while min_index <= max_index:
#         mid = (min_index + max_index) // 2
#         if target_element == arr[mid]:
#             return mid
#         if target_element < arr[mid]:
#             max_index = mid-1
#         else:
#             min_index = mid+1
#     return -1



def binary_search_revisoin(arr, target_element):
    arr_len = len(arr)
    min_range = 0
    max_range = arr_len -1 

    while min_range <= max_range:
        mid = (min_range + max_range) // 2
        if arr[mid] == target_element:
            return mid
        if arr[mid] < target_element:
            min_range = mid + 1
        else:
            max_range = mid - 1
    return -1




arr = [3, 4, 6, 7, 9, 12, 16, 17]
target = 17
# res = binary_search(arr, target)
res = binary_search_revisoin(arr, target)
if res == -1:
    print("The target is not present.")
else:
    print("The target is at index:", res)