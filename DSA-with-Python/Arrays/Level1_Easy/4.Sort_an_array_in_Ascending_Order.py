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
    return arr
array = [1, 7, 3, 6, 9, 15, 0, 2]
print("this is the ascending array using bubble sort : ", bubble_sort(array))

'''**********************************************************************************************************
Bubble Sort - n^2
***********************************************************************************************************'''