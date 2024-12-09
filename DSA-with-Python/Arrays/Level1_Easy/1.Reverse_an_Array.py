'''*******************************************************************************************************
Reverse an Array:
Write a function that takes an array as input and returns a new array with the elements in reverse order.

Example:
Input: [1, 7, 3, 6, 9, 15, 0, 2]
Output: [2, 0, 15, 9, 6, 3, 7, 1]
********************************************************************************************************'''




# def reverse_arr(actual_arr):
#     reverse_arr = []
#     for i in range((len(actual_arr)-1), -1, -1):
#         reverse_arr.append(actual_arr[i])
#     return reverse_arr

# print(reverse_arr([1, 7, 3, 6, 9, 15, 0, 2]))


# def reverse_the_arr(arr):
#     reverse_arr = []
#     for i in range((len(arr) - 1), -1, -1):
#         reverse_arr.append(arr[i])
#     return reverse_arr

# array = [45, 23, 46, 67, 89, 66, 32, 24]
# res = reverse_the_arr(array)

'''****************************************
Big O :- n

****************************************'''




def reverse_the_array_element(arr):
    res_array = []
    for i in range(len(arr)-1, -1, -1):
        res_array.append(arr[i])
    return res_array
array = [45, 23, 46, 67, 89, 66, 32, 24]
res = reverse_the_array_element(array)