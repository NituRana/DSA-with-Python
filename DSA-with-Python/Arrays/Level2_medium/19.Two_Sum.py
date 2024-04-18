'''*******************************************************************************************************
Two Sum : Check if a pair with given sum exists in Array

Example 1:
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14
Result: YES (for 1st variant)
       [1, 3] (for 2nd variant)
Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

Example 2:
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 15
Result: NO (for 1st variant)
	[-1, -1] (for 2nd variant)
Explanation: There exist no such two numbers whose sum is equal to the target.

***********************************************************************************************************'''
#1. Brute-force approach
def two_sum(n, arr, target):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return "YES"
    return "NO"

def main():
    n = 5
    arr = [2, 6, 5, 8, 11]
    target = 8
    ans = two_sum(n, arr, target)
    print("This is the answer for variant 1:", ans)

if __name__ == "__main__":
    main()

#2. 


#3. Optimized Approach(using two-pointer): 

def two_sum(n, arr, target):
    arr.sort()
    left = 0
    right = n - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return "YES"
        elif total < target:
            left += 1
        else:
            right -= 1
    return "NO"

def main():
    n = 5
    arr = [2, 6, 5, 8, 11]
    target = 6
    ans = two_sum(n, arr, target)
    print("This is the answer for variant 1:", ans)

if __name__ == "__main__":
    main()
    