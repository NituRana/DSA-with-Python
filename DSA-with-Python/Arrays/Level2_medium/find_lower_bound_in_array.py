'''
Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.

Pre-requisite: Binary Search algorithm

Examples
Example 1:
Input Format:
 N = 4, arr[] = {1,2,2,3}, x = 2
Result:
 1
Explanation:
 Index 1 is the smallest index such that arr[1] >= x.

Example 2:
Input Format:
 N = 5, arr[] = {3,5,8,15,19}, x = 9
Result:
 3
Explanation:
 Index 3 is the smallest index such that arr[3] >= x.

'''

#1. Brute Force Approach

def lowerBound(arr, n: int, x: int):
    for i in range(n):
        if arr[i] >= x:
            return i
    return n

arr = [3, 5, 8, 15, 19]
n = 5
x = 9
ind = lowerBound(arr, n, x)
print("The lower bound is the index:", ind)