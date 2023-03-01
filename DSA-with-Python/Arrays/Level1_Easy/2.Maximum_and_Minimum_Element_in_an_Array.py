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

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
array = [1, 7, 3, 6, 9, 15, 0, 2]
print(bubble_sort(array))
print("this is the ascending array : ", array)

'''**********************************************************************************************************
Bubble Sort - n^2
***********************************************************************************************************'''

'''*******************************************************************************************************
Reverse an Array:
Write a function that takes an array as input and returns a new array with the elements in reverse order.

Example:
Input: [1, 7, 3, 6, 9, 15, 0, 2]
Output: [2, 0, 15, 9, 6, 3, 7, 1]
********************************************************************************************************'''




def reverse_arr(actual_arr):
    reverse_arr = []
    for i in range((len(actual_arr)-1), -1, -1):
        reverse_arr.append(actual_arr[i])
    return reverse_arr

print(reverse_arr([1, 7, 3, 6, 9, 15, 0, 2]))







'''****************************************
Big O :- n

****************************************'''
