'''*******************************************************************************************************
Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to 
the end of the array and move non-negative integers to the front by maintaining their order.

Example 1:
Input:
 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output:
 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation:
 All the zeros are moved to the end and non-negative integers are moved to front by maintaining order


***********************************************************************************************************'''
# def move_all_zeros_to_the_end(arr):
#     for i in range (len(arr)):
#         if arr[i] == 0:
#             arr.append(arr[i])
#             arr.remove(arr[i])

#     return arr


# print(move_all_zeros_to_the_end([0, 2, 0, 8, 9, 0, 4, 6, 0]))

def move_all_zeros_to_the_end(arr):
    print("---------------- len :", len(arr))
    for i in range (len(arr)):
        print("---------------- i :", i)
        if not (i == ((len(arr))-1)):
            if arr[i] == 0:
                arr[i] = arr[i + 1]
                arr[i + 1] = 0

    return arr


print(move_all_zeros_to_the_end([0, 2, 0, 8, 9, 0, 4, 6, 0]))
