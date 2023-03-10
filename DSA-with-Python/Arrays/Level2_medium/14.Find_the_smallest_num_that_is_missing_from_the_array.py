'''*******************************************************************************************************
Find the smallest number that is missing from the array
Given a sorted array of n distinct integers where each integer is in the range from 0 to m-1 and m > n. Find the smallest number that is missing from the array.

Input: arr = [0, 1, 2, 6, 9], n = 5, m = 10 
Output: 3
---------------------------------------------
Input: arr = [4, 5, 10, 11], n = 4, m = 12  
Output: 0


***********************************************************************************************************'''
 
def find_missing_number(arr, n, m):
    # Create a set of the numbers in the array
    nums = set(arr)
    
    # Loop through the range of numbers from 0 to m
    for i in range(m+1):
        # If the current number is not in the set, return it as the missing number
        if i not in nums:
            return i

# Example usage:
arr = [0, 1, 2, 6, 9]
n = 5
m = 10
print(find_missing_number(arr, n, m))