'''*******************************************************************************************************
Rearrange the array all negative numbers appear before all positive numbers
An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

Input: arr[] = [12, 11, -13, -5, 6, -7, 5, -3, -6]
Output: [-12 -13 -5 -7 -3 -6 11 6 5]

***********************************************************************************************************'''
 
def Rearrange_arr(arr):
    j = 0
    for i in range(0, len(arr)) :
        if (arr[i] < 0) :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j + 1
    return arr
 
# Driver Code
if __name__ == "__main__":
    arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]
    print("This is the rearrange array :-",Rearrange_arr(arr))
    