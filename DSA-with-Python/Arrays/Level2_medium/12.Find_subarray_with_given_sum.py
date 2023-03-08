'''*******************************************************************************************************
find an array arr[] of non-negative integers and an integer sum, find a subarray that adds to a given sum.

Input: arr[] = [1, 4, 20, 3, 10, 5] sum = 33
Output: Sum found between indexes 2 and 4
Explanation: Sum of elements between indices 2 and 4 is 20 + 3 + 10 = 33
]
***********************************************************************************************************'''
 
def sub_array(arr, n, sum):
    for i in range(0,n):
        currentSum = arr[i]
        if(currentSum == sum):
            print("Sum found at indexes",i)
            return
        else:
            for j in range(i+1, n):
                currentSum += arr[j]
                if(currentSum == sum):
                    print("The sub array found between indexes",i,"and",j)
                    return
    print("No Subarray Found for this sum")
 
# Driver Code
if __name__ == "__main__":
    arr = [15,2,4,8,9,5,10,23]
    n = len(arr)
    sum = 23
    sub_array(arr, n, sum)