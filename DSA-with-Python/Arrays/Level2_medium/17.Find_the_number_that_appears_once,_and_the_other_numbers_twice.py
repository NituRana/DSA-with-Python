'''*******************************************************************************************************
Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

Example 1:
Input Format:
 arr[] = {2,2,1}
Result:
 1
Explanation:
 In this array, only the element 1 appear once and so it is the answer.

Example 2:
Input Format:
 arr[] = {4,1,2,1,2}
Result:
 4
Explanation:
 In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.

***********************************************************************************************************'''
 
def getSingleElement(arr):
    xorr = 0
    for i in arr :
        xorr ^= i
    return xorr
 
# Driver Code
if __name__ == "__main__":
    arr = [3, 6, 6, 4, 5, 4, 5]
    print("This is the single elemnt in the given array :-",getSingleElement(arr))
    