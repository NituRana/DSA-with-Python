def binary_search_revisoin(arr, sear_ele):
    min_ele = 0
    max_ele = len(arr) - 1
    
    while max_ele >= min_ele:
        mid = (min_ele + max_ele) // 2
        if arr[mid] == sear_ele:
            return mid
        if sear_ele > arr[mid]:
            min_ele = mid + 1
        else:
            max_ele = mid - 1
    return -1

arr = [3, 4, 6, 7, 9, 12, 16, 17]
target = 17
# res = binary_search(arr, target)
res = binary_search_revisoin(arr, target)
if res == -1:
    print("The target is not present.")
else:
    print("The target is at index:", res)



































    # min_ele = 0
    # max_ele = len(arr)-1

    # while min_ele <= max_ele:
    #     mid = (min_ele + max_ele) // 2
    #     if arr[mid] == sear_ele:
    #         return mid
    #     else:
    #         if arr[mid] > sear_ele:
    #             max_ele = mid - 1
    #         else:
    #             min_ele = mid + 1
    # return -1