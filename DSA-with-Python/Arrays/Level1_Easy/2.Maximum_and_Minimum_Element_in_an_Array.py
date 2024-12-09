'''*************************************************************************************************************************
Write a function that takes an array as input and returns a tuple containing the maximum and minimum elements in the array.

Example:
Input: [2, 5, 1, 8, 4]
Output: (8, 1)
************************************************************************************************************************'''

def min_max(arr):
    min = arr[0]
    max = arr[0]
    for i in range (1, len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    return(max, min)

print(min_max([2, 5, 1, 8, 4]))
'''*******************************************************************************************************
Sort an array in ascending order :
Write a function that sort an array in ascending order.

Example:
Input: [1, 7, 3, 6, 9, 15, 0, 2]
Output: [0, 1, 2, 3, 6, 7, 9, 15]
***********************************************************************************************************'''

# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(0, len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
# array = [1, 7, 3, 6, 9, 15, 0, 2]
# print(bubble_sort(array))
# print("this is the ascending array : ", array)

'''**********************************************************************************************************
Bubble Sort - n^2
***********************************************************************************************************'''
'''**********************************************************************************************************
#--------------------------------------- revision ----------------------------------------------------


***********************************************************************************************************'''
# input_array = [2, 5, 1, 8, 4]
# def max_min_element_in_array(input_array):
#     max_element = input_array[0]
#     min_element = input_array[0]
#     for i in input_array:
#         if min_element > i:
#             min_element = i
#         elif max_element < i:
#             max_element = i
#     return min_element, max_element
# min_ele, max_ele = max_min_element_in_array(input_array)
# print("------------------------ min element :", min_ele)
# print("------------------------ max element :", max_ele)








input_array = [2, 5, 1, 8, 4]
def max_min_element_in_array(input_array):
    min_ele = max_ele = input_array[0]

    for i in range(0, len(input_array)-1):
        if min_ele > input_array[i]:
            min_ele = input_array[i]
        elif max_ele < input_array[i]:
            max_ele = input_array[i]
    return min_ele, max_ele
min_ele, max_ele = max_min_element_in_array(input_array)
print("------------------------ min element :", min_ele)
print("------------------------ max element :", max_ele)