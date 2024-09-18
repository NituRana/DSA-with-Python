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


def reverse_the_arr(arr):
    rev_arr = []
    for i in range((len(arr) - 1), 0):
        rev_arr.append(i)
    return rev_arr
array = [5, 8, 2, 4, 7, 9, 1]
print(f"-------------------- input  :{array}-----")
print("----------  reverse arr :", reverse_arr(array))

'''****************************************
Big O :- n

****************************************'''