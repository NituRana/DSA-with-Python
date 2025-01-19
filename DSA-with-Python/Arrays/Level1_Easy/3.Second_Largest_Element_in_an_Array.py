'''*******************************************************************************************************
second largest element in an array :
Find the second largest element in an array.

Example:
Input: [1, 7, 3, 6, 9, 15, 0, 2]
Output: 9
***********************************************************************************************************'''
arr = [1, 7, 3, 6, 9, 15, 0, 2]
def second_largest(arr):
    largest_ele = second_largest = float('-inf')
    for num in arr:
        if num > largest_ele:
            second_largest = largest_ele
            largest_ele = num
        elif num > second_largest and num != largest_ele:
            second_largest = num
    return second_largest
print(second_largest(arr))
'''**********************************************************************************************************
Bubble Sort - n
***********************************************************************************************************'''