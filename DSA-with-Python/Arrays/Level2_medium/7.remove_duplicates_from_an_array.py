'''*******************************************************************************************************
remove duplicates from an array :
Write a Python program to remove duplicates from an array.

Example:
Input array: [3, 7, 8, 6, 3, 9, 15, 17, 7, 2]
Output array: [3, 7, 8, 6, 9, 15, 17, 2]
***********************************************************************************************************'''

def remove_duplicates(arr):
    unique_arr = []
    for i in range(0, len(arr)):
        if arr[i] in unique_arr:
           pass 
        else:
            unique_arr.append(arr[i])
    return unique_arr

arr = [3, 7, 8, 6, 3, 9, 15, 17, 7, 2]
print(" This is the array list:- ",arr)

print("The array after remove duplicates is :- ", remove_duplicates(arr))

'''************************************************************************************************************
Complexcity - n
*************************************************************************************************************'''