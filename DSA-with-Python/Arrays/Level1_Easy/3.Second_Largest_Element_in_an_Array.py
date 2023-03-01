'''*******************************************************************************************************
second largest element in an array :
Find the second largest element in an array.

Example:
Input: [1, 7, 3, 6, 9, 15, 0, 2]
Output: 9
***********************************************************************************************************'''
arr = [1, 7, 3, 6, 9, 15, 0, 2]
def second_largest(arr):
    largest = second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest
print(second_largest(arr))
'''**********************************************************************************************************
Bubble Sort - n
***********************************************************************************************************'''